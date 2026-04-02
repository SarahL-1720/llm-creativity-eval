import numpy as np
import torch
import torch.nn.functional as F
from torch.nn.functional import cosine_similarity
from rouge_score import rouge_scorer
from nltk.tokenize import sent_tokenize
import math
print("Imports finis")

def tokenize(text,nlp):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

###
### METRIQUES POUR NOUVEAUTE
###

### Mattr

def index_moving_average_ttr(text,nlp,window_size=100):
    tokens = tokenize(text,nlp)
    if len(tokens)==0:
        return 0
    if len(tokens) < window_size:
        return len(set(tokens)) / len(tokens)
    
    ttr_list = []
    n_chunk = len(tokens) // window_size
    
    for i in range(n_chunk):
        window = tokens[i*window_size : (i+1)*window_size]
        ttr_list.append(len(set(window)) / len(window))
    
    if len(tokens) % window_size != 0:
        last_window = tokens[n_chunk*window_size:]
        ttr_list.append(len(set(last_window)) / len(last_window))
    
    return np.mean(ttr_list)

### Implémentation du N-gramme Rarity Score
def corpus_to_Ngram(corpus,N=2):
    corpus_tokenized = [tokenize(text) for text in corpus]
    Ngram_corpus = [
        " ".join(tokens[i:i+N])
        for tokens in corpus_tokenized
        for i in range(len(tokens)-N+1)
    ]
    return set(Ngram_corpus)


def index_N_gram_rarity(text,corpus,N=2):
    Ngram_corpus = corpus_to_Ngram(corpus,N)
    tokens = tokenize(text)
    if len(tokens)==0:
        return 0
    if len(tokens) < N:
        Ngram = [" ".join(tokens)]
    Ngram = [" ".join(tokens[i:i+N]) for i in range(len(tokens)-N+1)]
    vocab = set(Ngram)

    return len(vocab - Ngram_corpus)/len(vocab)

# Distance d'embedding

def get_embedding(text, tokenizer, model, chunk_size=400, overlap=50):
    tokens = tokenizer.encode(text)
    if len(tokens) <= 512:
        return torch.tensor(model.encode(text))
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(tokenizer.decode(chunk, skip_special_tokens=True))
    
    embeddings = model.encode(chunks)
    return torch.tensor(embeddings).mean(dim=0)

def get_corpus_mean_embedding_np(corpus, tokenizer, model):
    embeddings = [get_embedding(text, tokenizer, model) for text in corpus]
    embeddings = torch.cat(embeddings, dim=0)
    mean_embedding = embeddings.mean(dim=0)
    return mean_embedding

def embedding_distance(v1, v2):
    # Convert to tensor if numpy
    if isinstance(v1, np.ndarray):
        v1 = torch.tensor(v1)
    if isinstance(v2, np.ndarray):
        v2 = torch.tensor(v2)
        
    v1 = v1.squeeze().unsqueeze(0)
    v2 = v2.squeeze().unsqueeze(0)
    
    similarity = cosine_similarity(v1, v2)
    return 1.0 - similarity.item()

def index_embedding_distance(text, corpus_mean_embedding, tokenizer, model):
    return embedding_distance(get_embedding(text, tokenizer, model),corpus_mean_embedding)


###
### METRIQUES POUR VALEUR
###

def index_coherence_locale(text,tokenizer,model):
    phrases = sent_tokenize(text)
    phrases_embeddings = [get_embedding(phrase,tokenizer,model) for phrase in phrases]
    sims = []
    for i in range(len(phrases_embeddings)-1):
        sim = cosine_similarity(torch.from_numpy(np.array([phrases_embeddings[i]])), torch.from_numpy(np.array([phrases_embeddings[i+1]]))).item()
        sims.append(sim)
    return np.mean(sims)

def index_rougeL(text,prompt):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    return scorer.score(prompt,text)

###
### METRIQUES POUR SURPRISE
###

def index_surprise_mean(text, tokenizer, model):
    if text is None:
        print("None")
        return None
    text = str(text)
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True
    )
    if inputs["input_ids"].shape[1] == 0:
        print("None")
        return None

    with torch.no_grad():
        logits = model(**inputs).logits

    logits = logits[:, :-1]
    labels = inputs["input_ids"][:, 1:]

    # 🔍 debug sécurité
    if labels.max() >= logits.size(-1):
        raise ValueError("Label index out of vocab range")

    log_probs = torch.log_softmax(logits, dim=-1)
    token_lp = log_probs.gather(2, labels.unsqueeze(-1)).squeeze(-1)

    H = -token_lp.mean() / torch.log(torch.tensor(2.0))
    print("done")
    return H.item()

###
### INDICE DE CREATIVITE
###
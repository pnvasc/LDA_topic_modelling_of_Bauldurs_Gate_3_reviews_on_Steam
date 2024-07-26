from gensim.models import (CoherenceModel, 
                           LdaMulticore)
# Function to train LDA model
def train_lda_model(corpus, dictionary, texts, num_topics, alpha, eta, passes, chunksize):
    """
    Train an LDA model with given parameters
    
    Parameters:
    ----------
    corpus : Gensim corpus
    dictionary : Gensim dictionary
    texts : List of preprocessed texts
    num_topics : int, number of topics
    alpha : float or 'auto', document-topic density
    eta : float or 'auto', topic-word density
    passes : int, number of passes through the corpus during training
    chunksize : int, number of documents to be used in each training chunk
    
    Returns:
    -------
    LDA model, coherence score
    """
    model = LdaMulticore(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=42,
        chunksize=chunksize,
        passes=passes,
        alpha=alpha,
        eta=eta,
        workers=2
    )
    
    coherence_model = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
    coherence_score = coherence_model.get_coherence()
    
    return model, coherence_score
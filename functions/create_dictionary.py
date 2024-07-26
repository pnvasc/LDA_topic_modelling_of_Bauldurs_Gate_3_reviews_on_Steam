from gensim import corpora
def create_dictionary(df, column='processed_review'):
    """
    Convert preprocessed reviews into a list of lists of words, create a dictionary representation of the documents, and create a corpus.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the preprocessed reviews.
    column (str): The name of the column containing the preprocessed reviews.

    Returns:
    texts (list of list of str): The tokenized reviews.
    dictionary (gensim.corpora.Dictionary): The dictionary representation of the documents.
    corpus (list of list of (int, int)): The corpus created from the dictionary and texts.
    """
    # Convert the preprocessed reviews into a list of lists of words
    texts = [review.split() for review in df[column]]
    # Create a dictionary representation of the documents
    dictionary = corpora.Dictionary(texts)
    # Create corpus
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    return texts, dictionary, corpus

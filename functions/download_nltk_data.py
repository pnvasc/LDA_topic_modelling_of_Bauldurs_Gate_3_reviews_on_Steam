import nltk

# Function to download NLTK data, if not already present
def download_nltk_data():
    datasets = [
        'vader_lexicon',
        'stopwords',
        'punkt',
        'wordnet',
        'omw-1.4',
        'averaged_perceptron_tagger'
    ]
    
    for dataset in datasets:
        try:
            nltk.data.find(f'corpora/{dataset}')
        except LookupError:
            nltk.download(dataset, quiet=True)

download_nltk_data()
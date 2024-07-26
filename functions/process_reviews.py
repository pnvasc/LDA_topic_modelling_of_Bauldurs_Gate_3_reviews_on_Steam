import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def process_reviews(df):
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
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove URL addresses
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        # Replace punctuation and hyphens with spaces
        text = re.sub(r'[^\w\s]|_|-', ' ', text)
        # Remove non-alphabetic characters (keeping spaces)
        text = re.sub(r'[^a-z\s]', ' ', text)
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text).strip()
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords, lemmatize, and remove isolated letters
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and len(token) > 1]
        # Join tokens back into a string
        return ' '.join(tokens)
    df['processed_review'] = df['review'].apply(process_text)
    return df
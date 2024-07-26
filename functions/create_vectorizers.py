from sklearn.feature_extraction.text import (CountVectorizer, 
                                             TfidfVectorizer)
def create_vectorizers(df):
    count_vectorizer = CountVectorizer(min_df=0.1, max_df=0.95)
    tf_matrix = count_vectorizer.fit_transform(df['processed_review'])
    tf_feature_names = count_vectorizer.get_feature_names_out()
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['processed_review'])
    
    return count_vectorizer, tfidf_vectorizer, tf_matrix, tfidf_matrix, tf_feature_names
import pandas as pd
import ast
# Extract and process author information
def process_df(df):
    df['author'] = df['author'].apply(ast.literal_eval)
    for key in ['steamid', 'num_games_owned', 'num_reviews', 'playtime_at_review']:
        df[key] = df['author'].apply(lambda x: x.get(key, None))
    df['playtime_at_review'] /= 60
    df['timestamp_created_date'] = pd.to_datetime(df['timestamp_created'], unit='s').dt.strftime('%Y-%m-%d')
    selected_columns=['review','playtime_at_review','num_games_owned','voted_up','timestamp_created_date']
    new_df = df[selected_columns].copy()
    new_df = new_df.drop_duplicates(subset=['review'])
    new_df['review_length'] = new_df['review'].str.split().str.len()
    return new_df
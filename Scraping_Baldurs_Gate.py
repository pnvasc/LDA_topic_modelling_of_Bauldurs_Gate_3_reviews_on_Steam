# Import necessary packages
import requests
import pandas as pd
import time
from config import BG3_data_file_path

# FUnction to fetch reviews
def fetch_steam_reviews(appid, num_reviews=500):
    reviews = []
    cursor = '*'
    language = 'english'
    
    while len(reviews) < num_reviews:
        url = f"https://store.steampowered.com/appreviews/{appid}?json=1&filter=all&language={language}&num_per_page=100&cursor={cursor}&day_range=365"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to get reviews: {response.status_code}")
            break
        
        data = response.json()
        
        if data['success'] == 1:
            reviews += data['reviews']
            cursor = data['cursor']
        else:
            print("Failed to get reviews: API returned unsuccessful status")
            break
        
        if len(reviews) >= num_reviews:
            reviews = reviews[:num_reviews]
        
        # Sleep to avoid Steam rate-limiting
        time.sleep(1)
    
    return reviews

appid = '1086940' # Bauldur's Gate 3
reviews = fetch_steam_reviews(appid)
print(f"Fetched {len(reviews)} reviews.") # Message printed if function successful

# Create pandas dataframe with reviews
review_df = pd.DataFrame(reviews)
# Rename review column
review_df = review_df.rename(columns={'review_text':'review'})
# Export dataframe to csv file 
data_file_path = BG3_data_file_path
review_df.to_csv(data_file_path, index=False)

print("Saved data to directory")
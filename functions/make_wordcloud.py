from wordcloud import WordCloud
import matplotlib.pyplot as plt
def make_wordcloud(df):
    # Word cloud for positive reviews (assuming you have a 'rating' column)
    positive_reviews = ' '.join(df[df['voted_up'] == 1]['processed_review'])
    positive_wordcloud = WordCloud(width=800, height=400, background_color='white', 
                                colormap='Greens').generate(positive_reviews)

    # Word cloud for negative reviews
    negative_reviews = ' '.join(df[df['voted_up'] != 1]['processed_review'])
    negative_wordcloud = WordCloud(width=800, height=400, background_color='white', 
                                colormap='Reds').generate(negative_reviews)

    # Display both word clouds
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    ax1.imshow(positive_wordcloud, interpolation='bilinear')
    ax1.axis('off')
    ax1.set_title('Positive Reviews')
    ax2.imshow(negative_wordcloud, interpolation='bilinear')
    ax2.axis('off')
    ax2.set_title('Negative Reviews')
    plt.tight_layout(pad=0)
    plt.show()
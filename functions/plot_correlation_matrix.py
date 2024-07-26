import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(df):
    df['voted_up'] = df['voted_up'].astype(int)
    # Create a new dataframe with only the numeric columns
    numeric_df = df[['review_length', 'playtime_at_review', 'num_games_owned', 'voted_up']]

    # Compute the correlation matrix
    corr_matrix = numeric_df.corr()

    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
    plt.title('Correlation Matrix of Game Review Variables')
    plt.tight_layout()
    plt.show()
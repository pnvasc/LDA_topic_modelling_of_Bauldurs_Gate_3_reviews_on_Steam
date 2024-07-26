import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df):
    # Create a 2x2 subplot
    fig, axs = plt.subplots(2, 2, figsize=(15, 15))
    fig.suptitle('Distributions of Key Variables', fontsize=16)

    # Make subplots
    sns.histplot(df['playtime_at_review'], bins=50, ax=axs[0, 0], kde=True)
    axs[0, 0].set_title('Distribution of Playtime')
    axs[0, 0].set_xlabel('Playtime (hours)')
    axs[0, 0].set_ylabel('Count')

    sns.histplot(df['review_length'], bins=50, ax=axs[0, 1], kde=True)
    axs[0, 1].set_title('Distribution of Review Length')
    axs[0, 1].set_xlabel('Review Length (characters)')
    axs[0, 1].set_ylabel('Count')

    sns.histplot(df['num_games_owned'], bins=50, ax=axs[1, 0], kde=True)
    axs[1, 0].set_title('Distribution of Games Owned')
    axs[1, 0].set_xlabel('Number of Games Owned')
    axs[1, 0].set_ylabel('Count')

    sns.countplot(x='voted_up', data=df, ax=axs[1, 1])
    axs[1, 1].set_title('Distribution of Votes')
    axs[1, 1].set_xlabel('Voted Up')
    axs[1, 1].set_ylabel('Count')

    # Display plots
    plt.tight_layout()
    plt.show()
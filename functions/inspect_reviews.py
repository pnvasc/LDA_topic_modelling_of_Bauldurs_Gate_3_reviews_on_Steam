def inspect_reviews(df, column=[], search_strings=[]):
    """
    Inspect reviews in a DataFrame for specific search strings.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the reviews.
    column (str): The name of the column to search within.
    search_strings (list): A list of strings to search for.

    Returns:
    row_indices (list): The indices of the rows containing the search strings.
    review_text (pandas.Series): The reviews containing the search strings.
    """
    # Locate the rows containing any of the specific strings
    mask = df[column].str.contains('|'.join(search_strings), case=False, na=False)
    filtered_df = df[mask]

    # Get the row numbers of the filtered rows
    row_indices = filtered_df.index.tolist()
    review_text = filtered_df[column]
    
    return row_indices, review_text

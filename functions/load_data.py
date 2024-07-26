import pandas as pd
# Load data file
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
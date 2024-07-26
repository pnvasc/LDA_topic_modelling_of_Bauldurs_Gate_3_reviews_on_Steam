import pandas as pd
from config import BG3_data_file_path
# Load data file
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
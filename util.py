import pandas as pd
def get_data(PATH):
    df = pd.read_csv(PATH)
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year.astype(str)
    df['month'] = df['date'].dt.month.astype(str)
    return df
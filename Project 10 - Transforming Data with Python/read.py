import pandas as pd

def load_data():
    data = pd.read_csv('hn_stories.csv')
    # Add column names to data
    data.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return data

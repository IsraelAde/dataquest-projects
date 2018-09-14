import read
import pandas as pd
from dateutil.parser import parse

data = read.load_data()

# Extract the hour from the timestamp using parse
def extract_hour(series):
    datetime_obj = parse(series)
    hour = datetime_obj.hour
    return hour

data['hour'] = data['submission_time'].apply(extract_hour)

# Get number of submissions for each hour of the day(24hr)
hours = data['hour'].value_counts()

for name, value in hours.items():
    print("{0}: {1}".format(name, value))
    
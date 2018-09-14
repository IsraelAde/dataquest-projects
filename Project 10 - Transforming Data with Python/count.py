import read
from collections import Counter

data = read.load_data()

# Combine all headlines into one string
# Lowercase each word to ensure capitalised words aren't treated differently
joined_headlines = data['headline'].str.cat().lower().split(' ')

# Get the 100 most common words from the headlines column
common = Counter(joined_headlines).most_common(100)
print(common)

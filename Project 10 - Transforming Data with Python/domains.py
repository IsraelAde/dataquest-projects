import read

data = read.load_data()

# Get the 100 most submitted domains
domains = data['url'].value_counts()
domains = domains[:100]

for name, row in domains.items():
    print("{0}: {1}".format(name, row))
    
import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")

# Find the number of schools that are part of the Juvenile Justice facility (JJ) and Magnet School (SCH_STATUS_MAGNET)
print(data["JJ"].value_counts())
print(data["SCH_STATUS_MAGNET"].value_counts())

# Find total male and female students in these two types of schools
print(pd.pivot_table(data, values = ["TOT_ENR_M", "TOT_ENR_F"], index = "JJ", aggfunc = "sum"))
print(pd.pivot_table(data, values = ["TOT_ENR_M", "TOT_ENR_F"], index = "SCH_STATUS_MAGNET", aggfunc = "sum"))

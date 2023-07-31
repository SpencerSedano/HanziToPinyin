import csv
import pinyin as p
import pandas as pd


print(p.get('我是余胖胖'))

# Read content of csv
file = pd.read_csv("cswords.csv")
print(file)

#Adding the header
headerList = ['character']

# convert data frame to csv
file.to_csv("cswords2.csv", header=headerList, index=False)

file2 = pd.read_csv("cswords2.csv")
print(file2)




import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

dataset = pd.read_csv("")
transcations = []
for i in range(0,7501):
    transcations.append([str(dataset.Value[i,j]) for j in range(0,20)])
    
rules = apriori(transactions=transcations,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2,max_length=2)

results = list(rules)
results

for item in results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule : " + items[0] + " -> " + items[1])
    
    print("Support : " + str(item[1]))
    print("Confidence : " + str(item[2][0][2]))
    print("Lift : " + str(item[2][0][3]))
import numpy as np

from math import sqrt
from collections import Counter
import pandas as pd
import random

df=pd.read_csv('./Assets/data.csv')
df.head()
df.drop(['CustomerID','_id','Age'],1,inplace=True)



df.replace('AC','YES',inplace=True)
df.replace('NON AC','NO',inplace=True)
df.replace('High','HIGH',inplace=True)

df.replace('HIGH','2',inplace=True)
df.replace('MEDIUM','1',inplace=True)
df.replace('LOW','0',inplace=True)

df.replace('YES','1',inplace=True)
df.replace('NO','0',inplace=True)



full_data=df.astype(int).values.tolist()

data={1:[],0:[]}
train_data=full_data
for i in train_data:
        data[i[-1]].append(i[:-1])
     
     
def knn(XX):
    k=5
    distances=[]
    for group in data:
        for features in data[group]:
            euclidean_distance=np.linalg.norm(np.array(features)-np.array(XX))
            distances.append([euclidean_distance,group])
    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

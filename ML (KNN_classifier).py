# library bulana
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np

# hmara data
data = {
    'Budget' : [20,80,40,90,30],
    'Buzz' : [2,9,5,8,4],
    'Result' : [0,1,0,1,1]
}
df = pd.DataFrame(data)
x = df[['Budget','Buzz']]
y = df['Result']

#scaler bnaya taki data ek line mien rhe
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# hmara model bnana aur data stor krana
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_scaled,y)

# ek naya budget bnana aur predict krana
new_budget = scaler.transform([[50,6]])
prediction = knn.predict(new_budget)
print(prediction)

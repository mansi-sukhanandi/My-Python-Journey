# library bulana
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# hmara data
data = {
    'Budget' : [100,20,150,30,80],
    'Star_power' : [9,4,10,5,7],
    'Result' : [1,0,1,0,1]
}
df = pd.DataFrame(data)
X = df[['Budget','Star_power']]
y = df['Result']

# model bnana aur sikhana
model = RandomForestClassifier(criterion='entropy',n_estimators=50)
model.fit(X,y)

# naya data dena aur predict krana
new_data = [[120,2]]
result = model.predict(new_data)
print('hmara naya data',result,'jayega') 

# library bulayi
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#hmara data
data = {
    'Income' : [15,16,17,18,50,55,60,65,90,95,100,105],
    'Spending_score' : [80,85,90,95,40,45,50,55,10,15,20,25]
}
df = pd.DataFrame(data)
inertia_list = []

# 1 se 7 tak dekhna aur model bna kr usse inertia ki value deni
for k in range(1,8):
    model = KMeans(n_clusters=k,n_init='auto')
    model.fit(df[['Income','Spending_score']])
    inertia_list.append(model.inertia_)

#graph bnana
plt.plot(range(1,8),inertia_list,marker='o')
plt.title ('Elbow Method')
plt.xlabel ('Prediction of k value')
plt.ylabel ('Inertia')
plt.show()

#final model bnana
final_model = KMeans(n_clusters=3,n_init='auto')
df['Target_group'] = final_model.fit_predict(df[['Income','Spending_score']])
print(df)

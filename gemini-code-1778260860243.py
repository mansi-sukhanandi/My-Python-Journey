import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. Wahi purana data
data = {
    'CIBIL' : [750, 500, 800, 600, 700],
    'Income' : [50, 20, 100, 30, 45],
    'Approved' : [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
X = df[['CIBIL', 'Income']]
y = df['Approved']

# 2. Model banana (Yahan badlav hai!)
# n_estimators=100 matlab hum 100 trees bana rahe hain
model = RandomForestClassifier(n_estimators=100, criterion='entropy')
model.fit(X, y)

# 3. Prediction
new_data = [[650, 40]]
result = model.predict(new_data)

print('Random Forest ka prediction:', result)
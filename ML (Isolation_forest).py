import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. Fake Data banana (Normal points ek jagah, Anomalies door)
# 55 normal points
X_normal = np.random.normal(size=(55, 2), loc=10) 
# 5 alag/door khade points (Anomalies)
X_outliers = np.random.uniform(low=80, high=100, size=(5, 2)) 

# Dono ko aapas mein milana
X = np.vstack([X_normal, X_outliers])

# 2. Isolation Forest Model taiyar karna
model = IsolationForest(n_estimators=150, contamination=0.08, random_state=24)
model.fit(X)

# 3. Predict karna (Normal = 1, Anomaly = -1)
predictions = model.predict(X)

# 4. Graph par magic dikhana
plt.scatter(X[:, 0], X[:, 1], c=predictions, cmap='coolwarm', edgecolor='k')
plt.title('ATM fraud detection')
plt.xlabel('Amount withdrawn')
plt.ylabel('Transaction speed')
plt.show()

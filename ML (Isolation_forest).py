import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. Fake Data banana (Normal points ek jagah, Anomalies door)
# 50 normal points
X_normal = np.random.normal(size=(50, 2), loc=0) 
# 5 alag/door khade points (Anomalies)
X_outliers = np.random.uniform(low=4, high=6, size=(5, 2)) 

# Dono ko aapas mein milana
X = np.vstack([X_normal, X_outliers])

# 2. Isolation Forest Model taiyar karna
model = IsolationForest(n_estimators=100, contamination=0.10, random_state=42)
model.fit(X)

# 3. Predict karna (Normal = 1, Anomaly = -1)
predictions = model.predict(X)

# 4. Graph par magic dikhana
plt.scatter(X[:, 0], X[:, 1], c=predictions, cmap='coolwarm', edgecolor='k')
plt.title('Isolation Forest Detection')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

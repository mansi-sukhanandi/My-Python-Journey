import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# 1. Data (Humaray 3 types ke Attacks)
# [X-axis: Frequency, Y-axis: Severity]
X = np.array([
    [10, 10], [12, 11],  # A & B (Login Attacks - Paas paas)
    [90, 85], [95, 90]   # C (Database Attacks - Door)
])

# 2. Dendrogram Banana (Tree Generation)
plt.figure(figsize=(10, 7))
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram: Cyber Attack Clusters')
plt.xlabel('Attacks')
plt.ylabel('Distance (Height)')
plt.show()

# 3. Model Fit Karna (Humne 2 Clusters decide kiye)
model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
y_predict = model.fit_predict(X)

print(f"Clusters assigned to attacks: {y_predict}")
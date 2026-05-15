import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Data load karo
X = np.array([[110, 10, 2, 80], [120, 12, 1, 85], [90, 5, 8, 40], [95, 4, 7, 45], [105, 8, 3, 70], [115, 11, 2, 75]])

# 2. Scaling (Dono ke beech ke gap ko khatam karne ke liye)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. PCA Model
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 4. Result dekhna
print("Naye Features (PC1 & PC2):\n", X_pca)
print("\nInformation kitni bachi:", pca.explained_variance_ratio_)

# 5. Graph banana
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='red')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA of Student Data')
plt.show()

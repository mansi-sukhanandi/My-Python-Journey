# 1. Zaruri tools lana
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np

# 2. Data banana (Hours studied vs Pass/Fail)
# X = Ghante, y = Result
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) 

# 3. Model ko banana aur sikhana
model = LogisticRegression()
model.fit(X, y)

# 4. Prediction karna (Socho Mansi ne 4.5 ghante padha)
hours_test = [[4.5]]
prediction = model.predict(hours_test)
probability = model.predict_proba(hours_test)

# 5. Result Card nikaalna
y_pred = model.predict(X)
print("--- Confusion Matrix ---")
print(confusion_matrix(y, y_pred))
print("\n--- Classification Report ---")
print(classification_report(y, y_pred))

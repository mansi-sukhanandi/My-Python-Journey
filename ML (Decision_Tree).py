import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# 1. DATA PREPARATION
# Humne 8 students ka data liya hai
data = {
    'Coding_Skills': [2, 8, 4, 9, 6, 1, 7, 3],
    'Internship_Done': [0, 1, 0, 1, 1, 0, 1, 0], 
    'Result': [0, 1, 0, 1, 1, 0, 1, 0] 
}

df = pd.DataFrame(data)
X = df[['Coding_Skills', 'Internship_Done']] # Sawaal (Features)
y = df['Result'] # Jawab (Target)

# 2. MODEL BUILDING
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)

# 3. VISUALIZATION 
plt.figure(figsize=(12,8))
plot_tree(clf, 
          feature_names=['Coding', 'Internship'], 
          class_names=['Rejected', 'Hired'], 
          filled=True, 
          rounded=True)
plt.show()

# 4. PREDICTION (Naye student ka test)
new_student = [[7, 1]] # Coding=7, Internship=Yes
result = clf.predict(new_student)
print(f"Prediction for the student: {result}")

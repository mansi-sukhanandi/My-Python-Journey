from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Feature (X) aur Target (y) chuna
X = df[['Hours_Studied', 'Attendance']] # Multiple Features!
y = df['Marks']

# 2. Batwara (80-20 Split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Training
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Exam (Prediction)
y_pred = model.predict(X_test)
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Data ko load karna
df = pd.read_csv("student_academic_detail.csv")

# 2. Data ka batwara
x = df[["hours_studied", "attendance"]]
y = df["final_marks"]

# 3. Train-Test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 4. Model training
model = LinearRegression()
model.fit(x_train, y_train)

# 5. Prediction
model_pre = model.predict(x_test)
print("Predicted Marks:", model_pre)

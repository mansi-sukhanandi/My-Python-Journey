# Step 1: Library bulai
from sklearn.linear_model import LinearRegression

# Step 2: Data taiyar kiya 
X = [[1], [2], [3]]  # Experience in years
y = [30000, 45000, 60000] # Salary in Rupees

# Step 3: Model ka Object banaya (OOPS!)
model = LinearRegression()

# Step 4: Machine ko sikhaya (Training)
model.fit(X, y)

# Step 5: Prediction mangi (Test)
exp_saal = [[5]] # Agar 5 saal ka experience ho toh?
salary_prediction = model.predict(exp_saal)

print(f"5 saal experience ki estimated salary hai: {salary_prediction[0]}")

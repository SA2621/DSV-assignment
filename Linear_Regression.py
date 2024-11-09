from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Assuming 'experience_salary_df' is the DataFrame containing 'YearsExperience' and 'Salary'
# Load your dataset here. For this example, I'll create a dummy dataset.

# Replace this with your dataset loading code
experience_salary_df = pd.DataFrame({
    'YearsExperience': [1.1, 2.0, 3.2, 4.5, 5.1, 6.0, 7.3, 8.9, 10.1],
    'Salary': [39343, 46205, 60150, 61111, 67938, 66029, 83088, 101302, 113812]
})

# Split into features and target
X = experience_salary_df[['YearsExperience']]
y = experience_salary_df['Salary']

# Split into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error (MSE) on the test set:", mse)

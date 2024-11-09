from sklearn.model_selection import train_test_split

# Split data into features and target
X = data
y = iris.target

# Split the dataset into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the number of samples in the training and testing sets
print("\nNumber of samples in the training set:", X_train.shape[0])
print("Number of samples in the testing set:", X_test.shape[0])

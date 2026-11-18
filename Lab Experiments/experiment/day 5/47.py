
# Hyperparameter Tuning using Decision Tree

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Define hyperparameters
parameters = {
    'max_depth': [2, 3, 4, 5, None],
    'criterion': ['gini', 'entropy'],
    'min_samples_split': [2, 4, 6]
}

# Perform hyperparameter tuning
grid_search = GridSearchCV(
    estimator=model,
    param_grid=parameters,
    cv=5,
    scoring='accuracy'
)

grid_search.fit(X_train, y_train)

# Get the best model
best_model = grid_search.best_estimator_

# Predict test data
y_pred = best_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display results
print("HYPERPARAMETER TUNING USING DECISION TREE")
print("------------------------------------------")

print("Best Parameters:", grid_search.best_params_)

print("Best Cross Validation Accuracy:",
      grid_search.best_score_)

print("Testing Accuracy:", accuracy)

print("Hyperparameter tuning completed successfully!")

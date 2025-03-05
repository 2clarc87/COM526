from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import pandas as pd
import matplotlib.pyplot as plt

# Load in the dataset from CSV using Pandas
data = pd.read_csv("iris.csv")

X = data.drop(["species"], axis=1)
y = data["species"]

# Split data into training samples and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Decision Tree -----------------------
dt = DecisionTreeClassifier()
dt_model = dt.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)

print(f"Decision Tree accuracy is {accuracy_score(y_test, dt_pred)}")

# plt.figure(figsize=(12, 8))
# plot_tree(dt_model, filled=True, feature_names=X.columns, class_names=y.unique())
# plt.show()

# KNN ---------------------------------
neigh = KNeighborsClassifier(n_neighbors=3)
knn_model = neigh.fit(X, y)
knn_pred = knn_model.predict(X_test)

print(f"KNN accuracy is {accuracy_score(y_test, knn_pred)}")

# Random Forest -----------------------
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model = rf.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

print(f"Random Forest accuracy is {accuracy_score(y_test, rf_pred)}")

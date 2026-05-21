import pandas as pd
from sklearn.tree import DecisionTreeClassifier

print("AI Model Started")

data = {
    "Monthly_Bill": [200, 800, 150, 900],
    "Churn": [0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["Monthly_Bill"]]
y = df["Churn"]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[700]])

if prediction[0] == 1:
    print("Customer may leave the company")
else:
    print("Customer will stay")
import pandas as pd

data = {
    "Transaction": [100, 5000, 200, 10000],
    "Fraud": ["No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print("Fraud Detection System")
print(df)
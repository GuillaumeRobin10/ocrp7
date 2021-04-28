import pandas as pd
budget = 500
cost = 0
total_benefit = 0
shouldbuy = ""
data_frame = pd.read_csv("brut.csv")

for i, row in data_frame.iterrows():
    if row["price"] <= 0:
        data_frame.drop(i, inplace=True)
    if row["profit"] <= 0:
        data_frame.drop(i, inplace=True)

data_frame["benefit"] = data_frame['profit'] * data_frame['price'] * 0.01
sorted_dataset = data_frame.sort_values(by=["profit"], ascending=False)


for i, row in sorted_dataset.iterrows():
    if (cost + row["price"]) <= budget:
        cost += row["price"]
        total_benefit += row["benefit"]
        shouldbuy += f"- {row['name']}-"

print(cost)
print(total_benefit)
print(shouldbuy)
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 170, 160, 180]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Sales"], marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Time Series")
plt.show()

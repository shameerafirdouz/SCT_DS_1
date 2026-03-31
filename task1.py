import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")

# Check columns (important)
print(df.columns)

# Convert column names to lowercase (avoids errors)
df.columns = df.columns.str.lower()

# -----------------------------
# BAR CHART (Gender count)
# -----------------------------
sns.countplot(x='sex', data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# -----------------------------
# HISTOGRAM (Age distribution)
# -----------------------------
plt.hist(df['age'].dropna(), bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
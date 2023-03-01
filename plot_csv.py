import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the CSV file created by the scraper
df = pd.read_csv("states.csv")

# Create a table of the population by state
table = pd.pivot_table(df, values="Population", index="State", aggfunc=sum)

# Create a bar chart of the population by state using seaborn
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=table.index, y=table["Population"], color="blue")
ax.set_xlabel("State")
ax.set_ylabel("Population (in millions)")
ax.set_title("Population by State")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

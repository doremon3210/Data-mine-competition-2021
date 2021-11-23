import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the data and display it
df = pd.read_excel('../Datasets/Dataset_Main.xlsx')
print(df.head())
print("--------------------------------------")

corrMatrix = df.corr()
print(corrMatrix)
print("--------------------------------------")

# Using Heat map to display the correlation between the variables
plt.figure(figsize=(14, 14))
sns.heatmap(corrMatrix, annot = True)
plt.savefig('../Results/correlation.png', bbox_inches = 'tight')
print("Exported the heatmap to correlation.png")
plt.tight_layout()
plt.show()
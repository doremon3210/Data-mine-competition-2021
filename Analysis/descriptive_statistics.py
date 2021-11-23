import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the data and display it
df = pd.read_excel('../Datasets/Dataset_Main.xlsx')

# Summary statistics
df_summary = df.describe().rename(index = {"50%": "median"}).drop('count')
print(df_summary)

# Export the table to an excel file
df_summary.to_excel('../Results/descriptive_statistics_table.xlsx')
print("Exported the table to descriptive_statistics_table.xlsx")
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read the data
df = pd.read_excel('../Data Sets/Dataset_Main.xlsx')

# List the indepdent variables
independent_vars = ['Percentage_Population_Black', 'Median_household_income', 'Renter', 'No_HS', 'Park', 'Fast_food', 'Current_smokers', 'Overweight', 'Sedentary', 'Medical_checkup', 'Food_insecurity']


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Univariate Linear Regression for Primary outcome")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# We use the Ordinary Least Square for each independent variable
for col in independent_vars:
    X = df.loc[:, col]  
    Y = df.loc[:, 'ED_Visits_Diabetes']
    X = sm.add_constant(X)
    result = sm.OLS(Y, X).fit()
    
    print("==============================================================================")
   
    print(result.summary())
    print("\n\n")


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Multivariable Linear Regression for Primary outcome")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# We use the Ordinary Least Square for all independent variables
X = df.loc[:, independent_vars]
Y = df.loc[:, 'ED_Visits_Diabetes']   
X = sm.add_constant(X)
result = sm.OLS(Y, X).fit()

print(result.summary())
print("\n\n")    
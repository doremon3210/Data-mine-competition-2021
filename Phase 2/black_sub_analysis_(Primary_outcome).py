import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read the data and drop NaN rows
sub_black = pd.read_excel('Dataset_Sub_Black.xlsx')
sub_black = sub_black.dropna()

# List the independet variable for Black
black_independent_var = ['Percentage_Population_Black', 'Median_household_income', 'Renter', 'No_HS', 'Current_smokers', 'Overweight', 'Sedentary', 'Medical_checkup']

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Univariate Linear Regression for Primary outcome (Sub Black)")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# We use the Ordinary Least Square for each independent variable
for col in black_independent_var:
    X = sub_black.loc[:, col]
    Y = sub_black.loc[:, 'ED_Visits_Diabetes']
    X = sm.add_constant(X)
    result = sm.OLS(Y, X).fit()
    
    print("==============================================================================")
   
    print(result.summary())
    print("\n\n")


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Multivariable Linear Regression for Primary outcome (Sub Black)")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# We use the Ordinary Least Square for all independent variables
X = sub_black.loc[:, black_independent_var]
Y = sub_black.loc[:, 'ED_Visits_Diabetes']   
X = sm.add_constant(X)
result = sm.OLS(Y, X).fit()

print(result.summary())
print("\n\n")    
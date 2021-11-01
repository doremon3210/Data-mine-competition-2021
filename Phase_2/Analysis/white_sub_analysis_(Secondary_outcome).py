import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read the data
sub_white = pd.read_excel('Dataset_Sub_White.xlsx')

# List the independet variable for White
white_independent_var = ['Percentage_Population_White', 'Median_household_income', 'Renter', 'No_HS', 'Current_smokers', 'Overweight', 'Sedentary', 'Medical_checkup']

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Univariate Analyses for Secondary outcome (Sub White)")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# We use the Ordinary Least Square for each independent variable
for col in white_independent_var:
    X = sub_white.loc[:, col]
    Y = sub_white.loc[:, 'Death_Diabetes']
    X = sm.add_constant(X)
    result = sm.OLS(Y, X).fit()
    
    print("==============================================================================")
    
    print(result.summary())
    print("\n\n")


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Multivariable Analyses for Secondary outcome (Sub White)")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# We use the Ordinary Least Square for all independent variables
X = sub_white.loc[:, white_independent_var]
Y = sub_white.loc[:, 'Death_Diabetes']   
X = sm.add_constant(X)
result = sm.OLS(Y, X).fit()

print(result.summary())
print("\n\n")    
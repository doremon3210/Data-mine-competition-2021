# Project name

Disparities in emergency room utilization due to diabetes across Florida’s counties

**-- Project Status: Active**

# Project Introduction / Relevance

Diabetes is a critical public health concern in the United States affecting 34.2 million Americans (1 in 10). [^1]In Florida, 10.5% of adults over the age of 18 have been diagnosed with diabetes, with averages varying from 6.4% to 23.6% by county. [^2]Patients with poor blood glucose control and diabetes management have a greater risk of acute and chronic complications such as cardiovascular disease, dehydration, ulcers, and kidney problems, resulting in hospitalizations and significant medical expenditures. [^3][^4]The number of emergency department (ED) visits due to diabetes has increased from 2010 to 2019 in Florida. However, it is unclear what is driving the increase in ER utilization. ED utilization among patients with diabetes is likely affected by several factors, including lack of primary care, poor adherence to care plans and lifestyle and community factors. [^5]This study seeks to characterize ED utilization by county using demographic, behavioral, and community indicators.

[^1]: Centers for Disease Control and Prevention. National Diabetes Statistics Report, 2020. Atlanta, GA: Centers for Disease Control and Prevention, U.S. Dept of Health and Human Services; 2020.
[^2]: Florida Diabetes Advisory Council. 2019. Florida Diabetes Legislative Report. Tallahassee, FL
[^3]: Washington RE (AHRQ), Andrews RM (AHRQ), Mutter RL (AHRQ). Emergency Department Visits for Adults with Diabetes, 2010. HCUP Statistical Brief #167. November 2013. Agency for Healthcare Research and Quality, Rockville, MD
[^4]: Centers for Disease Control and Prevention. National Diabetes Fact Sheet: National Estimates and General Information on Diabetes and Prediabetes in the United States, 2011. Atlanta, GA: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention; 2011.
[^5]: Fraze TK, Jiang HJ, Burgess J. Hospital Stays for Patients with Diabetes, 2008. HCUP Statistical Brief #93. August 2010. Agency for Healthcare Research and Quality, Rockville, MD. http://www.hcup-us.ahrq.gov/reports/statbriefs/sb93.pdf.

<br /><br />

# Partner

- [Center for Data Solutions](https://centerfordatasolutions.org/)
- ![CDS](https://centerfordatasolutions.org/wp-content/uploads/2019/06/cropped-site-logo-with-text.png)
- Partner Contract:

  1. Carmen Smotherman, MS, MPH (Carmen.Smotherman@jax.ufl.edu)
  2. Christina Guerrier, MBA (Christina.Guerrier@jax.ufl.edu)
  3. Jennifer Brailsford, PhD (Jennifer.Brailsford@jax.ufl.edu)

# Statistical analysis methods

- The counties’ characteristics were summarized using descriptive statistics.
- Pearson correlation method was used to calculate the correlation coefficient between the variables.
- In the univariate analyses, simple regression models included each outcome (as the dependent variable) and individual predictors, once at the time (as the independent variable). Then, all the independent variables were included in two multiple regression models (one for each outcome) to account for their joint effects. A predictor was considered statistically significant in predicting the outcome if its p-value (p) was less than 0.05. Ordinary least squares was used to calculate p-value

# Technologies

- Python
- Pandas
- Statsmodels
- Numpy
- Seaborn
- Matplotlib

# Project description

- We will explore whether counties’ income compositions are associated with increased utilization of ER due to diabetes. We hypothesize that:

1.  ER visits due to diabetes are higher in counties with higher proportion of low-income people
2.  ER visits due to diabetes are higher in counties with lower proportion of educated people. </p>

- In the main analysis, we examine the overall population in Florida by linear regression if Emergency room visits due to diabetes are influenced by the other variables such food insecurity rates, and other covariates (table1).
- In the sub-analysis, we explore diabetes prevalence for black and white races. We chose only black and white races because other races are not uncompleted data that many variables are missing in the data set. We analyze these covariables (table 2 and table 3).
  <br />
  <br />

# Needs of this project

- [Python](https://www.python.org/downloads/)
- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [Statsmodels](https://www.statsmodels.org/stable/install.html)
- [Numpy](https://numpy.org/install/)
- [Seaborn](https://seaborn.pydata.org/installing.html)
- [Matplotlib](https://matplotlib.org/stable/users/installing.html)
  <br />
  <br />

# Table 1. Description of Data Source and Variables (Main Analysis)

| Data Source                                                                                                          | Variables                                                                      |    Measure Notes    |         Notes         |
| :------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------- | :-----------------: | :-------------------: |
| [FL Charts](https://flhealthcharts.com/ChartsReports/rdPage.aspx?rdReport=ChartsProfiles.HealthEquityMergeMHProfile) | Emergency room visits due to diabetes                                          | Per 100K population |    Primary outcome    |
|                                                                                                                      | Diabetes age-adjusted death rate                                               |          "          |   Secondary outcome   |
|                                                                                                                      | Population                                                                     |  Total Population   |
|                                                                                                                      | Individuals 25 years and over with no high school diplomat Percent             |       Percent       | Independent variables |
|                                                                                                                      | Food insecurity rate                                                           |         ''          |          ''           |
|                                                                                                                      | Proportion of Blacks                                                           |         ''          |          ''           |
|                                                                                                                      | Renter-occupied housing units                                                  |         ''          |          ''           |
|                                                                                                                      | Population living within 1/2 mile of Population living within 1/2 mile of park |         ''          |          ''           |
|                                                                                                                      | Population living within 1/2 mile of fast-food restaurant                      |         ''          |          ''           |
|                                                                                                                      | Adults who are current smokers                                                 |         ''          |          ''           |
|                                                                                                                      | Adults who are obese                                                           |         ''          |          ''           |
|                                                                                                                      | Adults who are sedentary                                                       |         ''          |          ''           |
|                                                                                                                      | Adults who had a medical checkup in the past year                              |         ''          |          ''           |
|                                                                                                                      | Adults who are overweight                                                      |         ''          |          ''           |
|                                                                                                                      | Median household income Dollars                                                |       Dollars       |          ''           |

---

<br />
<br />

# Table 2. Description of Data Source and Variables (sub-Analysis, Blacks)

| Data Source                                                                                                          | Variables                                                          |    Measure Notes    |         Notes         |
| :------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------- | :-----------------: | :-------------------: |
| [FL Charts](https://flhealthcharts.com/ChartsReports/rdPage.aspx?rdReport=ChartsProfiles.HealthEquityMergeMHProfile) | Emergency room visits due to diabetes                              | Per 100K population |    Primary outcome    |
|                                                                                                                      | Diabetes age-adjusted death rate                                   |          "          |   Secondary outcome   |
|                                                                                                                      | Population, Black                                                  |  Total Population   |                       |
|                                                                                                                      | Individuals 25 years and over with no high school diplomat Percent |       Percent       | Independent variables |
|                                                                                                                      | Proportion of Blacks                                               |         ''          |          ''           |
|                                                                                                                      | Renter-occupied housing units                                      |         ''          |          ''           |
|                                                                                                                      | Adults who are current smokers                                     |         ''          |          ''           |
|                                                                                                                      | Adults who are obese                                               |         ''          |          ''           |
|                                                                                                                      | Adults who are sedentary                                           |         ''          |          ''           |
|                                                                                                                      | Adults who had a medical checkup in the past year                  |         ''          |          ''           |
|                                                                                                                      | Adults who are overweight                                          |         ''          |          ''           |
|                                                                                                                      | Median household income                                            |       Dollars       |          ''           |

---

<br />
<br />

# Table 3. Description of Data Source and Variables (sub-Analysis, White)

| Data Source                                                                                                          | Variables                                                          |    Measure Notes    |         Notes         |
| :------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------- | :-----------------: | :-------------------: |
| [FL Charts](https://flhealthcharts.com/ChartsReports/rdPage.aspx?rdReport=ChartsProfiles.HealthEquityMergeMHProfile) | Emergency room visits due to diabetes                              | Per 100K population |    Primary outcome    |
|                                                                                                                      | Diabetes age-adjusted death rate                                   |          "          |   Secondary outcome   |
|                                                                                                                      | Population, White                                                  |  Total Population   |                       |
|                                                                                                                      | Individuals 25 years and over with no high school diplomat Percent |       Percent       | Independent variables |
|                                                                                                                      | Proportion of White                                                |         ''          |          ''           |
|                                                                                                                      | Renter-occupied housing units                                      |         ''          |          ''           |
|                                                                                                                      | Adults who are current smokers                                     |         ''          |          ''           |
|                                                                                                                      | Adults who are obese                                               |         ''          |          ''           |
|                                                                                                                      | Adults who are sedentary                                           |         ''          |          ''           |
|                                                                                                                      | Adults who had a medical checkup in the past year                  |         ''          |          ''           |
|                                                                                                                      | Adults who are overweight                                          |         ''          |          ''           |
|                                                                                                                      | Median household income                                            |       Dollars       |          ''           |

---

<br />
<br />

# Contributing Members

1. [Aishwarya Pawar](n01473252@unf.edu)
2. [Huy Nguyen](n01497488@unf.edu)
3. [Shoto Fukuda](n01494013@unf.edu)

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



# Statistical analysis methods

- The counties’ characteristics were summarized using descriptive statistics.
- Pearson correlation method was used to calculate the correlation coefficient between the variables.
- In the univariate analyses, simple regression models included each outcome (as the dependent variable) and individual predictors, once at the time (as the independent variable). Then, all the independent variables were included in two multiple regression models (one for each outcome) to account for their joint effects. A predictor was considered statistically significant in predicting the outcome if its p-value (p) was less than 0.05. Ordinary least squares was used to calculate p-value

# Technologies

- [Python](https://www.python.org/downloads/)
- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [Statsmodels](https://www.statsmodels.org/stable/install.html)
- [Numpy](https://numpy.org/install/)
- [Seaborn](https://seaborn.pydata.org/installing.html)
- [Matplotlib](https://matplotlib.org/stable/users/installing.html)

# Project description

- We will explore whether counties’ income compositions are associated with increased utilization of ED due to diabetes. We hypothesize that:

1.  ED visits due to diabetes are higher in counties with higher proportion of low-income people
2.  ED visits due to diabetes are higher in counties with lower proportion of educated people. </p>

- In the main analysis, we examine if ED visits due to diabetes are influenced by the other variables such food insecurity rates, and other covariates, within the population in Florida using linear regression (table 1).
- In the sub-analysis, we explore ED visits due to diabetes for black and white races. We chose only black and white races because other races have incomplete data on many variables. We analyze these covariables (table 2).
- Below is a table outlining the data source and variables used in the main analysis and sub analysis. Data for the sub-analysis comes from the same source. There are less variables for sub-analysis due to data availability. 
  <br />
  <br />


# Results
Read more [here](./Phase_2/Results/Results.docx)

<br />
  <br />



# Table 1. Description of Data Source and Variables

<table>
    <thead>
        <tr>
            <th>Data Source</th>
            <th>Variables</th>
            <th>Measure</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=15><a href="https://flhealthcharts.com/ChartsReports/rdPage.aspx?rdReport=ChartsProfiles.HealthEquityMergeMHProfile">  FL chart </a></td>
            <td>Emergency room visits due to diabetes </td>
            <td rowspan = 2> Per 100K population</td>
            <td>Primary outcome</td>
        </tr>
        <tr>
            <td>Diabetes age-adjusted death rate</td>
             <td> Secondary outcome</td>
        </tr>
        <tr>
         <td> Population </td>
         <td> Total population</td>
         <td> </td>
        </tr>
            <td >Individuals 25 years and over with no high school diplomat Percent</td>
            <td rowspan = 11>Percent</td>
            <td rowspan = 11> Independent variables </td>
        </tr>
        <tr> 
           <td>Food insecurity rate</td>
        <tr> 
           <td>Proportion of Blacks</td>
        <tr> 
           <td>Renter-occupied housing units</td>
        <tr> 
           <td>Population living within 1/2 mile of Population living within 1/2 mile of park </td>
        <tr> 
           <td>Population living within 1/2 mile of fast-food restaurant</td>
        <tr> 
           <td>Adults who are current smokers</td>
        <tr> 
           <td>Adults who are obese</td>
        <tr> 
           <td>Adults who are sedentary</td>
        <tr> 
           <td>Adults who had a medical checkup in the past year</td>
        <tr> 
           <td>Adults who are overweight</td>
        <tr> 
           <td>Median household income </td>
           <td> Dollars</td>
        

    
</table>
<br />
<br />

# Table 2. Sub-analysis was performed on data for White and Black races respectively
<table>
    <thead>
        <tr>
            <th>Data Source</th>
            <th>Variables</th>
            <th>Measure</th>
            <th>Notes</th>
        </tr>
    </thead>
    </tbody>
        <tr>
            <td rowspan=16><a href="https://flhealthcharts.com/ChartsReports/rdPage.aspx?rdReport=ChartsProfiles.HealthEquityMergeMHProfile">  FL chart </a></td>
            <td>Emergency room visits due to diabetes </td>
            <td rowspan = 2> Per 100K population</td>
            <td>Primary outcome</td>
        </tr>
        <tr>
            <td>Diabetes age-adjusted death rate</td>
             <td> Secondary outcome</td>
        </tr>
        </tr>
         <td> Population </td>
         <td rowspan = 4> Total population<td>
       </tr> 
          <td>Population, Black</td>
      <tr>
      <tr>
       <td> Population, White </td>
        </tr>
            <td >Individuals 25 years and over with no high school diplomat Percent</td>
            <td rowspan = 8>Percent</td>
            <td rowspan = 9> Independent variables </td>
        </tr> 
           <td>Proportion of Blacks</td>
        <tr> 
           <td>Renter-occupied housing units</td> 
         <tr>
           <td>Adults who are current smokers</td>
        <tr> 
           <td>Adults who are obese</td>
        <tr> 
           <td>Adults who are sedentary</td>
        <tr> 
           <td>Adults who had a medical checkup in the past year</td>
        <tr> 
           <td>Adults who are overweight</td>
         <tr>
        <tr> 
             <td>Median household income </td>
           <td> Dollars</td>
         
 </table>
<br />
<br />
       



# Contributing Members

1. Aishwarya Pawar (n01473252@unf.edu)
2. Huy Nguyen (n01497488@unf.edu)
3. Shoto Fukuda (n01494013@unf.edu)

# Partner

- [Center for Data Solutions](https://centerfordatasolutions.org/)
- ![CDS](https://centerfordatasolutions.org/wp-content/uploads/2019/06/cropped-site-logo-with-text.png)
- Partner Contact:

1. Carmen Smotherman, MS, MPH (Carmen.Smotherman@jax.ufl.edu)
2. Christina Guerrier, MBA (Christina.Guerrier@jax.ufl.edu)
3. Jennifer Brailsford, PhD (Jennifer.Brailsford@jax.ufl.edu)
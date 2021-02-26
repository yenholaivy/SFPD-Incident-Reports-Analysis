# SFPD Incident Reports Analysis

## Overview
From 2018/01/01 to 2021/02/20, San Francisco Police Department (SFPD) tracked over 436K incident reports with over 30 attributes. The data is publicly available on [DataSF](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783) and is automatically updated daily.

For the SF residents and the people that frequent SF, I would like to find our the following questions for you:
1. What are the top incident categories in SF?
2. Where do the incidents more likely to occur?
3. How do the incidents trend over time?

## EDA
#### Incident Category
Based on the data, there are 51 incident categories, and the top 5 are:
1. Larceny Theft - 131316 (30%)
2. Other Miscellaneous - 32171 (7%)
3. Malicious Mischief - 27830 (6%)
4. Non-Criminal - 26480 (6%)
5. Assault - 25794 (6%)

![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/incident-category-pie.png)
 

#### Larceny Theft

#### Incident Subcategory

#### Incident Neighborhood

#### Incident Trend Over Time


## Hypothesis Testing
#### Rate of Larceny Theft Between 2018 vs 2019

<b> Null Hypothesis</b>: The rate of larceny theft in 2018 is equal to the rate of larceny theft in 2019. 

<b> Alternative Hypothesis</b>: The rate of larceny theft in 2018 is different from the rate of larceny theft in 2019.

#### Assumptions:
1. Each larceny incident is an independent event. One larceny incident doesn't lead to another, or prevent another to happen.
2. Each larceny incident is committed by a different resident in SF.

#### Two Samples:
2018 Incident Reports: 
- SF Population in 2018 is 870,044.
- The number of larceny incident reports is 48,841.

2019 Incident Reports: 
- SF Population in 2019 is 874,961.
- The number of larceny incident reports is 48,898.

#### Perform both Two Sample T-Test and Mann-Whitney U-Test.

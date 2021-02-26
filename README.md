# SFPD Incident Reports Analysis

## Overview
From 2018/01/01 to 2021/02/20, San Francisco Police Department (SFPD) tracked over 436K incident reports with over 30 attributes. The data is publicly available on [DataSF](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783) and is automatically updated daily.

For the SF residents and the people that frequent SF, I would like to find out the following questions for you:
1. [What are the top incident categories in SF?](#incident-category)
2. [Where do the incidents more likely to occur?](#incident-neighborhood)
3. [How do the incidents trend over time?](#incident-trend-over-time)


## Exploratory Data Analysis
#### Incident Category
Based on the data, there are 51 incident categories, and the top 5 are:
1. Larceny Theft - 131,316 (30%)
2. Other Miscellaneous - 32,171 (7%)
3. Malicious Mischief - 27,830 (6%)
4. Non-Criminal - 26,480 (6%)
5. Assault - 25,794 (6%)

![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/incident-category-pie.png)
 
Based on the pie chart and data above, larceny theft category made up 30% of the incident reports. I found this number quite large, and decided to focus on the this category to find out more information about larceny theft in San Francisco.


#### Larceny Theft
Different from robbery or burglary, larceny theft involves unlawfully taking property without force and breaking into a structure. There is a local threshold that determine if an incident is grand larceny, which can be charged as a felony, or petty larceny. For California, that threshold is $950.

Looking at the data, the number of grand larceny incidents is much larger than the number of petty larceny incidents.
- Grand larceny - 81,240 (62%)
- Petty larceny - 40,483 (31%)
- Unknown - 9,593 (7%)

![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/larceny-amount-bar.png)

This is a worrisome observation because grand larceny is much more serious. But at the same time, if someone has to commit larceny with the risk of getting arrested, perhaps it makes more sense to target the more valuable properties. 


#### Incident Subcategory
Digging into the larceny category, there are total 8 subcategories, and the top 4 are:
1. Larceny - From Vehicle - 73,844 (56%)
2. Larceny Theft - Other - 32,443 (24%)
3. Larceny Theft - From Building - 7,999 (6%)
4. Larceny Theft - Shoplifting - 7,313 (5%)

![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/larceny-subcat-pie.png)

The number one subcategory - Larceny From Vehicle - is not a big surprise to me. I always hear about how you should never leave anything in the car in San Francisco, not even a jacket. And the data here is really supporting that statement. 


#### Incident Neighborhood
Moving to the incident neighborhoods, there are 41 neighborhoods in San Francisco. In the graph below, we can see that there are a lot of dots (i.e. incidents) on the top right corner, which is the downtown, the business center and the touristy areas. In other words, there are a lot more people coming in and out, which could explain why the rate of larceny theft is much higher. On the next graph, we can see similar patterns on the top 4 larceny theft subcategories.


![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/neighborhood.png)

![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/nbhood-subcat.png)



#### Incident Trend Over Time
The last attribute I want to explore is time. Based on the graph below, 2018 and 2019 had almost same number of larceny incidents, where there is a big drop in 2020. According to the dataset, there are no changes in the number of police stations. And there were no new laws on larceny that got passed last year, either. So, the most possible reason for the drop might be Covid-19.

![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/larceny-year-bar.png)

In this next graph, we can see a big drop in 2020 March, which is when we started sheltering at home, and people started moving out of the city. The pandemic and the changes in people's living habits could all contribute to the drop in the number of incidents.

![alt text](https://github.com/yenholaivy/SFPD-Incident-Reports-Analysis/blob/main/img/larceny-month-bar.png)

## Hypothesis Testing
For my hypothesis testing, I want to know, prior to the Covid influence, if there is a significant difference in the rate of larceny between 2018 and 19. 

<b> Null Hypothesis</b>: The rate of larceny theft in 2018 is equal to the rate of larceny theft in 2019. </br>
<b> Alternative Hypothesis</b>: The rate of larceny theft in 2018 is different from the rate of larceny theft in 2019. </br>
<b> Alpha</b>: 0.05

#### Assumptions:
To perform the testing, I have 2 assumptions: 
1. Each incident is an independent event (i.e. one incident doesn't lead to another or prevent another to happen).
2. Each incident is committed by a different person in SF.


#### Two Samples:
2018 Sample: 
- SF Population in 2018 is 870,044.
- The number of larceny incident reports is 48,841.

2019 Sample: 
- SF Population in 2019 is 874,961.
- The number of larceny incident reports is 48,898.

#### Result
I performed the test with both two sample t-test and Mann-Whitney u-test, and got the same p-value 0.47. As the p-value is much higher than alpha, I failed to reject the null hypothesis. I am not able to conclude that the rate of larceny theft is different between 2018 and 2019.

![Screen Shot 2021-02-26 at 10 51 13 AM](https://user-images.githubusercontent.com/77142026/109352283-68ae9500-782f-11eb-9cbd-de633fcb8bbb.png)


## Next Steps
There are so much more we can do on the subject of SF incident reports. Some topics that I am interested in taking on next are:
1. Look into how Covid affects the incident reports?
2. Look into other incident categories.
3. Compare SF incident reports to other big cities such as Chicago, New York.

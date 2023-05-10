# Cognizant: Gala Groceries Predicting Stock Executive Summary

## Overview
This project seeks to optimize grocery store stock through machine learning to balance perishability, minimize waste, and prevent stockouts.

## The Problem

Gala Groceries is an innovative new chain of grocery stores that have grown in stature within the last 5 years across the U.S. They compete with Wholefoods, and they pride themselves in being the best quality produce on the market. They rely heavily on new technologies, such as IoT to give them a competitive edge over other grocery stores. 

They pride themselves on providing the best quality, fresh produce from locally sourced suppliers. However, this comes with many challenges to consistently deliver on this objective year-round. Gala Groceries approached Cognizant to help them with a supply chain issue. Groceries are highly perishable items. If you overstock, you are wasting money on excessive storage and waste, but if you understock, then you risk losing customers. **They want to know how to better stock the items that they sell.**

## The Solution

By utilizing machine learning models and data provided by Gala Groceries, it was possible to predict the estimated stock percentage of each product at unique hours. The data was trained using Linear Regression, Decision Tree Regressor, and Random Forest Regressor, with Linear Regression demonstrating superior performance.

<br>

## Details
### Keys to sucess
<img align='right' src="https://github.com/biancaportela/cognizant_virtual_experience/blob/main/tasks/task_3/output.png" width="330">

- **More data is required**: Approximately 50% accuracy with the current set of data and features that were created. Ind order to test this model for production, we need larger samples.
- **Price is important**: Price was an important feature in the model, but category was not.
- **Built on IoT**: Temperature was significant within the model but lacked statistical significance in a linear model. More IoT data across a alarger time period could potentially yield better results.
<br>


<br><br><br>

## Next Steps/Reflections


 Since I am working with a linear model, I used the `statsmodels` module as it provides more statistical information about the model, allowing for a better understanding of the relationship between the variables.

- The results obtained are not promising as none of the features have demonstrated statistical significance. 
- This implies that we cannot confidently conclude that any of these features have a substantial impact on the `estimated_stock_pct`. The feature `day_of_month` shows some level of statistical importance with a p-value of 0.105, but it is still relatively high. Ideally, we would prefer a p-value to be as low as possible and closer to 0.001. 
- Since we only have a small sample size of data, it is advisable to report these findings to the business and recommend **further dataset engineering or additional data collection to obtain more reliable results**.
 <br><br>
<img align='center' src='https://github.com/biancaportela/cognizant_virtual_experience/blob/main/tasks/task_3/ols%20results.png'>

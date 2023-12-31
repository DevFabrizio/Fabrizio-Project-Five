# Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

- 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
- 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Dataset Content

This dataset is sourced at [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data) and it comprises of a list of characteristics and features of houses in AMes, Iowa (U.S.A.). The features are divided in numerical and categorical type. The various features describe things like surface area in square feet for different sections of the house (wooden porch, 1st floor, etc) and quality of living conditions or construction status.

| Column Name   | Description                                                            | Range                                                                                                                         |
| ------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1stFlrSF      | First Floor square feet                                                | 334 - 4692                                                                                                                    |
| 2ndFlrSF      | Second floor square feet                                               | 0 - 2065                                                                                                                      |
| BedroomAbvGr  | Bedrooms above grade (not including basement)                          | 0 - 8                                                                                                                         |
| BsmtExposure  | Basement Exposure                                                      | Good, Average, Minimum, None                                                                                                  |
| BsmtFinType1  | Basement Finished Area Rating                                          | Good Living Quarters, Average Living Quarters, Below Average Living Quarters, Average Rec Room, Low Quality, Unfinished, None |
| BsmtFinSF1    | Type 1 finished square feet                                            | 0 - 5644                                                                                                                      |
| BsmtUnfSF     | Unfinished square feet of basement area                                | 0 - 2336                                                                                                                      |
| TotalBsmtSF   | Total square feet of basement area                                     | 0 - 6110                                                                                                                      |
| GarageArea    | Size of garage in square feet                                          | 0 - 1418                                                                                                                      |
| GarageFinish  | Interior finish of the garage                                          | Finished, Rough Finished, Unfinished, None                                                                                    |
| GarageYrBlt   | Year garage was built                                                  | 1900 - 2010                                                                                                                   |
| GrLivArea     | Above grade (ground) living area square feet                           | 334 - 5642                                                                                                                    |
| KitchenQual   | Kitchen quality                                                        | Excellent, Good, Typical/Average, Fair, Poor                                                                                  |
| LotArea       | Lot size in square feet                                                | 1300 - 215245                                                                                                                 |
| LotFrontage   | Linear feet of street connected to property                            | 21 - 313                                                                                                                      |
| MasVnrArea    | Masonry veneer area in square feet                                     | 0 - 1600                                                                                                                      |
| EnclosedPorch | Enclosed porch area in square feet                                     | 0 - 286                                                                                                                       |
| OpenPorchSF   | Open porch area in square feet                                         | 0 - 547                                                                                                                       |
| OverallCond   | Rates the overall condition of the house                               | Very Poor, Poor, Fair, Below Average, Average, Good, Very Good, Excellent, Very Excellent                                     |
| OverallQual   | Rates the overall material and finish of the house                     | Very Poor, Poor, Fair, Below Average, Average, Good, Very Good, Excellent, Very Excellent                                     |
| WoodDeckSF    | Wood deck area in square feet                                          | 0 - 736                                                                                                                       |
| YearBuilt     | Original construction date                                             | 1872 - 2010                                                                                                                   |
| YearRemodAdd  | Remodel date (same as construction date if no remodeling or additions) | 1950 - 2010                                                                                                                   |
| SalePrice     | Sale Price                                                             | 34900 - 755000                                                                                                                |

## Hypothesis and how to validate?

- 1 - There should be a good correlation with the quality of the construction with Sale Price
  - A Correlation study can help in this investigation
- 2 - Within the features we should be able to identify a hierarchy for the correlation of the features
  - A Correlation study can help in this investigation
- 3 - The features containing 'square feet' as a metric could be strong predictors of Sale Price
  - A ML model (regression) can identify the best sale price predicting features

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1:** Data Visualization and Correlation study

  - We will inspect the datset.
  - We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Sale Price.
  - We will plot the main variables against Sale Price to visualize insights.
  - We will use the Predictive Power Score tool to investigate non linear correlations
  - We will plot the findings from the PPS analysis in a heatmap

- **Business Requirement 2:** Regression Model
- We will clean and feature engineer the dataset according to the necessity of the regression model and dataset
- We will split the dataset into train and test set
- We will train and analyze the performance of the model
- We will generate plots to visually describe out results

## ML Business Case

### Predict Sale Price

#### Regression Model

- We want an ML model to predict sale price for the inherited houses and other future properties. The target variable is a continous number.
- The objective is to provide the Lydia with a competitive price which will maximize her profit for the properties in her possession and help her establish prices for future properties she might own or want to acquire.
- The target variable is the Sale Price
- The model success metrics are
  - At least 0.75 for R2 score, on train and test set
  - The ML model is considered a failure if: The perfomance for the R2 score is not met.
- The output will be a continuous value corresponding to the price for the given property. We are going to run the prediction in the app for Lydia, but she will be able to also input new data and get a prediction of any new property she might acquire in the future.
- Heuristics: Due to the complexity of the task, a heuristic method for determining a price for the customer properties would be inefficient. Most modern day practices for determing sale prices in the real estate market rely on data analysis and comparison. A ML model will prove more reliable and precise compared to these methods.
- The training data to fit the model comes from a public dataset. The dataset is also processed in order to make it viable for the mathematical analysis provided by the technologies used in the project.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary

- Quick project summary
  - Project Terms & Jargon
  - Describe Project Dataset
  - State Business Requirements
  - Dashboard navigation guide

### Page 2: Correlation Study for Sale Price

- This page answers the Business Requirements 1
- General explaination for correlation (created for non-technical users)
- Textual explaination of the correlation levels
- Checkbox: Show the plots for the correlation level for the single features. These plots are a visual representation of the Spearman correlation study which is shown in the checkbox above

### Page 3: Sale Price prediction

- This page answers Business Requirements 2
- Results of the ML pipeline on Lydia's houses
- Input widgets for data prediction for any new property

### Page 4: Project Hypothesis and Validation

With this page we want to delineate the main hypothesis:

- We suspect that the variable Overall Quality is indicative or directly proportional of the sale price.
  - That is correct. Although it is important to remember that Overall Quality is not the only variable correlated with sale price. This means that different levels on the other variables can influence the final sale price even if Overall Quality is high.
- We suspect that the Square Feet variables like: 1st Floor SF, 2nd Floor SF, Total Porch SF and similar might be correlated to the sale price.
  - This is partially true. Not all features which take square feet as a measure are strong predictors of the sale price.

In this page a plot for the best feature found by the model is also shown. Along with the comparison and conclusion between the hypothesis and results.

### Page 5: Predict Sale Price

- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance plot. This shows the different performance of the model between the train and test set

## Deployment

### Heroku

- The App live link is [this](https://lydia-predictive-app-d788e0d6fee3.herokuapp.com/)
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. Once the deployment has succesfully completed click the 'Open app' button.

## Technologies Used

This is a list of all the different technologies and libraries used in the project:

- Python
- Jupyter Notebooks
- Pandas
- Numpy
- Seaborn
- Matplot
- Power Predictive Score
- Streamlit
- Feature Engine
- Sci-Kit Learn
- XGBoost
- Joblib
- os
- Git
- GitHub
- Codeanywhere (CDE)

## Additional

The process for the hyperparameter optimization was the following:

- select hyperparameters from the Churnometer Walkthrough Project
- Increase Cross Validation Folds from 5 to 20
- Initial hyperparameters:

  - 'model**n_estimators': [10, 50, 100, 200, 300],
    'model**max_depth': [None, 10, 20, 30],
    'model\_\_min_samples_split': [2, 5, 10, 20]

- New hyperparameters:

  - 'model**n_estimators': [10, 50, 100],
    'model**max_depth': [10, 20, 30],
    'model\_\_min_samples_split': [2, 5, 10, 20]

- Decrease Cross Validation Folds from 20 to 5
- Set the threshold value for the Smart Correlated Selection from 0.5 to 0.8
  These changes allowed me to reach the 0.75 value on the r2 score for train and
  test set.

### Bugs

- During the development of page 3 of the streamlit app I noticed that my ML
  pipeline couldn't predict on the inherited houses dataset. This was because I
  had previously feature engineered the original dataset by one hot encoding the
  categorical variables. I did this in order to run the correlation studies since
  the correlation functions need to have numerical data. When I used the pipeline
  on the inherited houses dataset the categorical features were not one hot
  encoded. To fix this I just added the Ordinal Encoder to my Pipeline. This also
  created a cascade of other bugs for which I had to run the notebook and modify
  where I placed the code to save the train and test set and where I saved the pi
  pipeline.

- During the development of page 3 I noticed that when placing a series of input
  widgets inside a conditional block (if statement) the app would just re-run the
  page once the user input the first few data points. In order to fix that I
  explored the possibility to add a streamlit session state in order to store all
  the results from the input widgets in an object and to change that object into
  a pandas dataframe. In the end I simply removed the conditional statement and
  the page worked just fine.

### Credits

- In the Correlation study notebook (cell 44) I copied the mask shown below from the
  seaborn documentation:
  "mask = np.triu(np.ones_like(df_spearman_corr, dtype=bool))"

- In the Correlation study notebook (cell 42) I copied the pps score code from
  the Churnometer Walkthrough project.

- In the Model and Evaluation notebook the cells 7, 8, 10, 11, 15, 28, 40

**This second README file will be used through development to describe the project and also as a notebook to keep track of tasks and feautures to implement**

## Dataset Content

This dataset is sourced at [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)and it comprises of a list of characteristics and features of houses in AMes, Iowa (U.S.A.). The features are divided in numerical and categorical type. The various features describe things like surface area in square feet for different sections of the house (wooden porch, 1st floor, etc) and quality of living conditions or construction status.

| Column Name     | Description                                           | Range                |
|-----------------|-------------------------------------------------------|-----------------------|
| 1stFlrSF        | First Floor square feet                              | 334 - 4692            |
| 2ndFlrSF        | Second floor square feet                             | 0 - 2065              |
| BedroomAbvGr    | Bedrooms above grade (not including basement)       | 0 - 8                 |
| BsmtExposure    | Basement Exposure                                    | Good, Average, Minimum, None |
| BsmtFinType1    | Basement Finished Area Rating                        | Good Living Quarters, Average Living Quarters, Below Average Living Quarters, Average Rec Room, Low Quality, Unfinished, None |
| BsmtFinSF1      | Type 1 finished square feet                         | 0 - 5644              |
| BsmtUnfSF       | Unfinished square feet of basement area             | 0 - 2336              |
| TotalBsmtSF     | Total square feet of basement area                   | 0 - 6110              |
| GarageArea      | Size of garage in square feet                        | 0 - 1418              |
| GarageFinish    | Interior finish of the garage                         | Finished, Rough Finished, Unfinished, None |
| GarageYrBlt     | Year garage was built                                  | 1900 - 2010           |
| GrLivArea       | Above grade (ground) living area square feet          | 334 - 5642            |
| KitchenQual     | Kitchen quality                                       | Excellent, Good, Typical/Average, Fair, Poor |
| LotArea         | Lot size in square feet                               | 1300 - 215245         |
| LotFrontage     | Linear feet of street connected to property           | 21 - 313              |
| MasVnrArea      | Masonry veneer area in square feet                     | 0 - 1600              |
| EnclosedPorch   | Enclosed porch area in square feet                    | 0 - 286               |
| OpenPorchSF     | Open porch area in square feet                        | 0 - 547               |
| OverallCond     | Rates the overall condition of the house              | Very Poor, Poor, Fair, Below Average, Average, Good, Very Good, Excellent, Very Excellent |
| OverallQual     | Rates the overall material and finish of the house    | Very Poor, Poor, Fair, Below Average, Average, Good, Very Good, Excellent, Very Excellent |
| WoodDeckSF      | Wood deck area in square feet                         | 0 - 736               |
| YearBuilt       | Original construction date                             | 1872 - 2010           |
| YearRemodAdd    | Remodel date (same as construction date if no remodeling or additions) | 1950 - 2010 |
| SalePrice       | Sale Price                                           | 34900 - 755000        |

## Business Requirements

The business requirements established with Lydia Doe, after the initial meeting are the following:

* The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
  
* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

## Hypothesis and how to validate?

* 1 - There should be a good correlation with the quality of the construction with Sale Price
  * A Correlation study can help in this investigation
* 2 - Within the features we should be able to identify a hierarchy for the correlated features
  * A Correlation study can help in this investigation

## The rationale to map the business requirements to the Data Visualizations and ML tasks

* **Business Requirement 1:** Data Visualization and Correlation study
  * We will inspect the datset.
  * We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Sale Price.
  * We will plot the main variables against Sale Price to visualize insights.

* **Business Requirement 2:** Regression Model
* We will clean and feature engineer the dataset according to the necessity of the regression model
* We will split the dataset into train and test set
* We will train and analyze the performance of the model

## ML Business Case

### Predict Sale Price for the inherited houses

### Predict Sale Price

#### Regression Model

* We want an ML model to predict sale price for the inherited houses. The target variable is a continous number. 
* The objective is to provide the customer with a price which will maximize her profit for the properties in her possession
* The model success metrics are
  * At least 0.75 for R2 score, on train and test set
  * The ML model is considered a failure if:
        * The perfomance for the R2 score is not met.
* The output is defined as a continuous value for tenure in months. It is assumed that this model will predict tenure if the Predict Churn Classifier predicts 1 (yes for churn). If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).
* Heuristics: Due to the complexity of the task, a heuristic method for determining a price for the customer properties would be inefficient and definitely closer to guessworl.
* The training data to fit the model comes from a public dataset. 



## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary

* Quick project summary
  * Project Terms & Jargon
  * Describe Project Dataset
  * State Business Requirements

### Page 2: Correlation Study for Sale Price

* State business requirement 1

### Page 3: Sale Price prediction

* State business requirement 2


### Page 4: Project Hypothesis and Validation

* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:


### Page 5: Predict Sale Price

* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance



# EDA and Feature Engineering

## Where does EDA fit in the Data Science Process

![image](https://user-images.githubusercontent.com/71754779/135961119-28954e0b-a18f-4ff0-824d-13d54ce20e93.png)


## Resources
* data_cleaning_template.py is designed for you to be able to do base-line data preprocessing and cleaning on the datasets provided through Omdena. Please let me know if you have any other suggestions on what we should do to add to this file as the collaborative effort on this is key to our success.

* EDA_Template.py is designed for all of us to be able to do baseline EDA part of dataset without wasting lot of time writing the same code. 
  
* Projects Tab
  * Has tasks in the form of "Notes" that you can grab, drag, and drop in different lists, as well as iterate over with your work completed
  * This is a great way for us to also keep track of contributions and keep redundancy to a minimum.  

## What is EDA? 
Check [this link here](https://www.ibm.com/cloud/learn/exploratory-data-analysis) for some more information on exactly what we mean when we say EDA. We are focused on analyzing the data, summarizing the main features, and use visualizations to show the data. Feature Engineering, Statistical Modeling, Hypothesis Testing, and Dimensionality Reduction. These all fall under our category. We will need to understand the data and how everything correlates in order to effectively accomplish this task. 

## Task & Task List
Our task is to complete the EDA so that our Modeling team can intake the data and run it into their models and focus on hyperparameter tuning. We will complete this by splitting the work flow as follows:
* Data Visualization and Normalizing
  * Data Visualizations
    * ***This is one of the most key factors in EDA***
    * Can we create visualizations that we can show to a consumer or marketing supervisor(basically anyone with little knowledge of DS) and get them to understand the data?
    * Using these visualizations, what insights do we gain from the data? Do we need to manipulate our data anymore than we already have?
  * Normalization vs. Scaling
    * As we create these visualizations, we need to think about how the data falls. Are we going to experience a skew that can lead to data leakage down the road? How does the data from this set fall on the map as opposed to the other data sets? Is it well-generalized or is this only specific to a certain circumstance? How is everything intraconnected? These are the key points in this subtask.
* Feature Engineering and Dimension Reduction
  * Target Identification and Feature Identification. What works with the data, what doesn't?
    * Do we need to create a target? How can we given the data provided?
    * If provided a target, are we sure that there isn't any columns in the data associated with the calculation of that target that can lead to Data Leakage?
    * What features are present in the data? Given these features, can we combine into one that may hold more significance than the two seperately?
    * Can we merge/join any of these sets together to give a stronger sense of the data? Some of these are short and small, what can we do with them?
  * Dimension Reduction
    * How does the data look? Is it a wide dataset? Long dataset? How is that going to work for our Modeling Task?
    * Low Variance: Should we filter out the variables that have a low variance compared to others? 
    * Decision Tree vs FillNA: Is it better for us to use a decision tree to deal with our NaN values in some of the datasets? Why?
    * PCA: Map the data to lower dimensional space in a linear fashion as to maximize the variance of the data
* Insights and DataSet Summarizations
  * When we have the Data all pieced together, what does that look like? What is included in each of these data sets? The more information we can pass along to the next team about our data, the better
  * We can submit this in the form of a .txt doc or markdown file
* Statistical Model Testing of Data
  * Ensure data fits into a model and can attain higher than baseline accuracy.
  * Once that is achieved, we would consider that a "win" that we can pass along to Task 3 for deployment modeling
  * Anyone who is in Task 3 as well is encouraged to take on this task!

# Usage

- `EDA.py`  

    To run the EDA script to see the analysis, you could use the following code:

    ```python
    # Performs EDA
    import EDA
    EDA.eda(df_2)
    ```
    
    Output:  
    
    ```python
    Preview of data:
    Unnamed: 0	your_type_of_document	your_nationality	your_gender	your_birthdate	your_foreigner	period	your_consecutive	your_marital_status	your_student	...
    0	0	TI	COLOMBIA	M	30/07/1996	NaN	20134	EK201340233804	Single	STUDENT	...
    1	1	CC	COLOMBIA	M	13/04/1994	NaN	20133	EK201330220754	Single	STUDENT	...
    2	2	CC	COLOMBIA	F	08/12/1991	NaN	20134	EK201340246502	Single	STUDENT	...
    3 rows × 142 columns

    To check: 
     (1) Total number of entries 
     (2) Column types 
     (3) Any null values

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Columns: 142 entries, Unnamed: 0 to optative_category_saber_11
    dtypes: float64(28), int64(7), object(107)
    memory usage: 5.7+ KB
    None
    
    ...
    
    ```

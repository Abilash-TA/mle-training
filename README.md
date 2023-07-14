# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To excute the script
 - Create a virtual environment and activate it:
   - If you don't have the mle-dev environment set up, you can create it using the provided env.yml file.
   Run the following command to create the environment from the env.yml file:
   - *conda env create -f env.yml*
 - Activate the environment:
   - Once the environment is created, activate it using the following command
   - *conda activate mle-dev*
 - With the virtual environment activated, you can run the script using the following command:
   - python nonstandardcode.py


      


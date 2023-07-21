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

## To create and activate the environment
 - Create a virtual environment and activate it:
   - If you don't have the mle-dev environment set up, you can create it using the provided env.yml file.
   Run the following command to create the environment from the env.yml file:
   - *conda env create -f env.yml*
 - Activate the environment:
   - Once the environment is created, activate it using the following command
   - *conda activate mle-dev*


## To install the housinglib library
First, download the wheel file from the repo, then run the following command.
```
pip install housinglib-0.1.0-py3-none-any.whl
```
Import the housinglib library by using
```
import housinglib
```

## The scripts folder contains the scripts to download data, train and check scores of the model
To load the data and create training and testing set, use the ingest_data.py script by running following command in the shell:
```
python ingest_data.py
```
To train the model using the training data, use train.py
```
python train.py
```
To see the performance of the model, use score.py
```
python score.py
```

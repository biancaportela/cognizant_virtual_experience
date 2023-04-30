# ---- 1) IMPORTING THE PACKAGES

import pandas as pd
import numpy as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression


# ---- 2) DEFINE GLOBAL CONSTANTS
# K is used to define the number of folds that will be used for cross-validation
k = 5


# --- 3) ALGORITHM CODE
#load data
def load_data(file_path):
    """
    Load a CSV file from the specified file path using pandas.

    Args:
        file_path (str): The file path of the CSV file to load.

    Returns:
        df: A pandas DataFrame containing the data from the CSV file.
    """
    
    df = pd.read_csv(file_path)
    df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
    return df

#create target variables and predictor variable

def create_target_and_predictors(df, target_col):
    """
    Splits a pandas DataFrame into predictor and target variables.

    Args:
        df (pandas.DataFrame): The DataFrame to split.
        target_col (str): The name of the target variable column.

    Returns:
        tuple: A tuple containing two DataFrames. The first DataFrame contains
            the predictor variables and the second DataFrame contains the target
            variable.
    """
    # Check to see if the target variable is present in the data
    if target not in data.columns:
        raise Exception(f'Target: {target} is not present in the data')
    
    # Extract the target variable
    y = df[target_col]
    
    # Extract the predictor variables
    X = df.drop(target_col, axis =1)
    
    return X, y

# Train algorith

def linear_regression_cross_validation(X, y):
    """
    Performs k-fold cross-validation on a linear regression model.

    Args:
        X (numpy array): The input features for the model.
        y (numpy array): The target variable for the model.

    Returns:
        tuple: A tuple containing two lists, the MAE and MSE for each fold.
    """
    
    # Initialize KFold cross-validation object with 5 folds
    kfold = KFold(n_splits=k)
    # Linear Regression
    model = LinearRegression()
    # Initialize empty lists for storing MAE and MSE for each fold
    fold_mae_ = []
    fold_mse_ = []
    
    # Loop through each fold
    for idx, (idx_train, idx_validation) in enumerate(kfold.split(X)):
        
        # Split data into training and validation sets
        X_train_split = X[idx_train]
        y_train_split = y[idx_train]
        
        # Fit model on training set
        model.fit(X_train_split, y_train_split)
        
        # Get validation set data
        X_validation_split = X[idx_validation]
        y_validation_split = y[idx_validation]

        # Make predictions on validation set
        predictions = model.predict(X_validation_split)
        
        # Calculate and store MAE and MSE for fold
        fold_mae = mean_absolute_error(y_validation_split, predictions)
        fold_mse = mean_squared_error(y_validation_split, predictions)
        fold_mae_.append(fold_mae)
        fold_mse_.append(fold_mse)
        
        # Print fold results
        print(f"Fold {idx + 1}: MAE = {fold_mae:.3f}")
        print(f"Fold {idx + 1}: MSE = {fold_mse:.3f}")
        print('**************')

    # Calculate and print overall MAE and MSE
    print(f'Overall MAE: {np.mean(fold_mae_)}')
    print(f'Overall MSE: {np.mean(fold_mse_)}')

    # Return tuple of MAE and MSE for each fold
    return fold_mae_, fold_mse_
    
    
# --- 4) MAIN FUNCTION

def run():
    """
    This function executes the training pipeline of loading the prepared
    dataset from a CSV file and training the machine learning model

    :param

    :return
    """
    
    # Load the data first
    df = load_data()
    
    # Now split the data into predictors and target variables
    X, y = create_target_and_predictors(data=df)
    
    # Finally, train the machine learning model
    linear_regression_cross_validation(X=X, y=y)
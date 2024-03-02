import joblib
import pandas as pd
import numpy as np
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

loaded_model = joblib.load('linear_regression_model.pkl')
prediction_file = 'data/filtered_prediction_data.csv'

# Load the prediction data
predictions = pd.read_csv(prediction_file)
predictions['Home/Away'] = 'H'

drop_features = [
    'ConSOSRemain', 'rank', 'rank.1', 'proj. W', 'Proj. L', 'USU_ConSOSRemain', 
    'USU_rank', 'USU_team', 'USU_conf', 'USU_rank.1', 'USU_proj. W', 'USU_Proj. L',
    'record', 'Con Rec.', 'USU_record', 'USU_Con Rec.'
]

# Get all numeric features
numeric_features = predictions.select_dtypes(include=[np.number]).columns.tolist()
# Get all categorical features
categorical_features = predictions.select_dtypes(exclude=[np.number, 'bool']).columns.tolist()
binary_features = ['Home/Away']

# Filter out the drop_features
numeric_features = [feature for feature in numeric_features if feature not in drop_features and feature not in binary_features]
categorical_features = [feature for feature in categorical_features if feature not in drop_features and feature not in binary_features]

# Create a preprocessor using make_column_transformer
preprocessor = make_column_transformer(
    (
        make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown='ignore')),
        categorical_features + binary_features
    ),
    (
        make_pipeline(SimpleImputer(strategy="median"), MinMaxScaler()),
        numeric_features
    ),
    ("drop", drop_features)
)

# Preprocess the prediction data
X_pred = preprocessor.fit_transform(predictions)

# Make predictions
predictions['Prediction'] = loaded_model.predict(X_pred)

# Save the predictions to a new CSV file
predictions.to_csv('predictions_output.csv', index=False)

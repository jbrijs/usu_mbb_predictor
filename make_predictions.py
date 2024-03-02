import pandas as pd
import joblib

loaded_model = joblib.load('linear_regression_model.pkl')
loaded_preprocessor = joblib.load('preprocessor.pkl')  # Load the preprocessor
prediction_file = 'data/filtered_prediction_data.csv'

# Load the prediction data
predictions = pd.read_csv(prediction_file)

# Add a 'Home/Away' column filled with 1s if it's missing
if 'Home/Away' not in predictions.columns:
    predictions['Home/Away'] = 1

# List of features expected by the preprocessor (you need to fill this based on your training data)
expected_features = [
    "rank", "team", "conf", "record", "adjoe", "oe Rank", "adjde", "de Rank", "barthag", "rank.1", "proj. W", "Proj. L", "Pro Con W", "Pro Con L", "Con Rec.", "sos", "ncsos", "consos", "Proj. SOS", "Proj. Noncon SOS", "Proj. Con SOS", "elite SOS", "elite noncon SOS", "Opp OE", "Opp DE", "Opp Proj. OE", "Opp Proj DE", "Con Adj OE", "Con Adj DE", "Qual O", "Qual D", "Qual Barthag", "Qual Games", "FUN", "ConPF", "ConPA", "ConPoss", "ConOE", "ConDE", "ConSOSRemain", "Conf Win%", "WAB", "WAB Rk", "Fun Rk, adjt", " new", "USU_rank", "USU_team", "USU_conf", "USU_record", "USU_adjoe", "USU_oe Rank", "USU_adjde", "USU_de Rank", "USU_barthag", "USU_rank.1", "USU_proj. W", "USU_Proj. L", "USU_Pro Con W", "USU_Pro Con L", "USU_Con Rec.", "USU_sos", "USU_ncsos", "USU_consos", "USU_Proj. SOS", "USU_Proj. Noncon SOS", "USU_Proj. Con SOS", "USU_elite SOS", "USU_elite noncon SOS", "USU_Opp OE", "USU_Opp DE", "USU_Opp Proj. OE", "USU_Opp Proj DE", "USU_Con Adj OE", "USU_Con Adj DE", "USU_Qual O", "USU_Qual D", "USU_Qual Barthag", "USU_Qual Games", "USU_FUN", "USU_ConPF", "USU_ConPA", "USU_ConPoss", "USU_ConOE", "USU_ConDE", "USU_ConSOSRemain", "USU_Conf Win%", "USU_WAB", "USU_WAB Rk", "USU_Fun Rk, adjt", "USU_ new", "EFG_O", "EFG_D", "TOR", "TORD", "ORB", "DRB", "FTR", "FTRD", "2P_O", "2P_D", "3P_O", "3P_D", "ADJ_T", "USU_EFG_O", "USU_EFG_D", "USU_TOR", "USU_TORD", "USU_ORB", "USU_DRB", "USU_FTR", "USU_FTRD", "USU_2P_O", "USU_2P_D", "USU_3P_O", "USU_3P_D", "USU_ADJ_T"
]


# Drop any features from the prediction data that are not expected by the preprocessor
predictions = predictions[expected_features]
predictions["Home/Away"] = 'H'
predictions['Season'] = 2024

# Preprocess the prediction data using the loaded preprocessor
X_pred = loaded_preprocessor.transform(predictions)
 
# Make predictions
predictions['Prediction'] = loaded_model.predict(X_pred)

# Save the predictions to a new CSV file
predictions.to_csv('predictions_output.csv', index=False)

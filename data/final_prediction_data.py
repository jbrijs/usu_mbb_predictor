import pandas as pd

# Load the prediction data and combined merged stats data
prediction_data_file = 'data/prediction_data.csv'
combined_stats_file = 'data/combined_merged_stats_all_teams_updated.csv'

prediction_data = pd.read_csv(prediction_data_file)
combined_stats = pd.read_csv(combined_stats_file)

# Get the common columns between prediction data and combined stats
common_columns = set(prediction_data.columns).intersection(combined_stats.columns)
print(len(common_columns))

# Filter the prediction data to include only common columns
filtered_prediction_data = prediction_data[common_columns]

# Save the filtered prediction data to a new CSV file
filtered_prediction_data.to_csv('data/filtered_prediction_data.csv', index=False)

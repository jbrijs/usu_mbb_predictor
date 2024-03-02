import pandas as pd
import glob

# Define the path to the directory containing your merged stats CSV files
merged_stats_dir = 'data/'

# Use glob to get a list of all merged stats CSV files
merged_stats_files = glob.glob(merged_stats_dir + 'merged_stats_*.csv')

# Initialize an empty list to store the DataFrames
dfs = []

# Iterate through the list of files and read each one into a DataFrame
for file in merged_stats_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all the DataFrames into one long DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined DataFrame to a new CSV file
output_file = 'data/combined_merged_stats.csv'
combined_df.to_csv(output_file, index=False)

print(f'Combined merged stats CSV file created at {output_file}')

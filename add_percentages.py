import pandas as pd
import os

def update_all_teams_stats(combined_stats_file, cbb_files, new_features, output_file, usu_team_name='Utah St.'):
    # Load the combined merged stats CSV file
    combined_stats_df = pd.read_csv(combined_stats_file)

    # Iterate over the cbb files and update the combined stats dataframe
    for cbb_file in cbb_files:
        # Load the cbb data
        cbb_df = pd.read_csv(cbb_file)

        # Fix the column name in cbb22.csv if necessary
        if 'cbb22.csv' in cbb_file:
            cbb_df.rename(columns={'EFGD_D': 'EFG_D'}, inplace=True)

        # Check if the YEAR column is present, if not, infer the year from the file name
        if 'YEAR' not in cbb_df.columns:
            # Extract the year from the file name (e.g., 'cbb24.csv' will be 2024)
            file_year = os.path.basename(cbb_file).replace('cbb', '').replace('.csv', '')
            # Ensure the year is four digits, assuming all years are in the 2000s
            year = int("20" + file_year if len(file_year) == 2 else file_year)
            cbb_df['YEAR'] = year


        # Iterate over each row in the cbb dataframe
        for index, row in cbb_df.iterrows():
            team = row['TEAM']
            year = row['YEAR']
            print("Year", str(year))

            # Update the combined stats dataframe with the new features for all teams
            for feature in new_features:
                combined_stats_df.loc[(combined_stats_df['Season'] == year) & (combined_stats_df['team'] == team), feature] = row[feature]

            # Update the combined stats dataframe with the USU_ prefixed features for Utah State
            if team == usu_team_name:
                for feature in new_features:
                    combined_stats_df.loc[combined_stats_df['Season'] == year, f'USU_{feature}'] = row[feature]

    # Save the updated combined stats dataframe to the specified output file
    combined_stats_df.to_csv(output_file, index=False)
    print(f'Updated combined stats saved to {output_file}')

# Define the list of new features to add
new_features = ['EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T']

# Define the list of cbb files (including cbb20.csv to cbb24.csv)
cbb_files = [
    'data/cbb.csv',
    'data/cbb20.csv',
    'data/cbb21.csv',
    'data/cbb22.csv',
    'data/cbb23.csv',
    'data/cbb24.csv'  # Added the new file for the year 2024
]

# Specify the output file name (the updated combined_merged_stats_all_teams_updated.csv file)
output_file = 'data/combined_merged_stats_all_teams_updated.csv'

# Update the stats for all teams and add USU_ prefixed stats for Utah State
update_all_teams_stats(output_file, cbb_files, new_features, output_file)

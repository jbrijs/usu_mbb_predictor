import pandas as pd

def update_all_teams_stats(combined_stats_file, cbb_files, new_features, output_file, usu_team_name='Utah St.'):
    # Load the combined merged stats CSV file
    combined_stats_df = pd.read_csv(combined_stats_file)

    # Iterate over the cbb files and update the combined stats dataframe
    for cbb_file in cbb_files:
        # Load the cbb data
        cbb_df = pd.read_csv(cbb_file)

        # Iterate over each row in the cbb dataframe
        for index, row in cbb_df.iterrows():
            team = row['TEAM']
            year = row['YEAR']

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

# Define the list of cbb files (assuming cbb.csv contains data from 2013 to 2019)
cbb_files = ['data/cbb.csv']

# Specify the output file name
output_file = 'data/combined_merged_stats_all_teams_updated.csv'

# Update the stats for all teams and add USU_ prefixed stats for Utah State
update_all_teams_stats('data/combined_merged_stats.csv', cbb_files, new_features, output_file)

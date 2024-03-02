import pandas as pd
from fuzzywuzzy import process

def combine_csvs(pe_path, team_results_path, output_path):
    pe_stats_df = pd.read_csv(pe_path)
    team_results_df = pd.read_csv(team_results_path)

   
    pe_stats_df.rename(columns={'EFGD_O': 'EFG_D'}, inplace=True)

    truncate_features = ['EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T']

    trunc_features(pe_stats_df, truncate_features)

    pe_stats_df.rename(columns={'Team': 'team'}, inplace=True)
    merged_df = pd.merge(team_results_df, pe_stats_df[['team'] + truncate_features], on='team')

    merged_df.to_csv(output_path, index=False)

    #merge the values from pe_stats_df for truncated features into the team results_df into a new csv file

def trunc_features(df, features):
    for feature in features:
        for index, row in df.iterrows():
            string_value = str(row[feature])
            if '.' in string_value:
                df.at[index, feature] = float(string_value[:4])
            else:
                df.at[index, feature] = float(string_value[:2])


pe_path = 'data/2024_pe.csv'
team_results_path = 'data/2024_team_results.csv'
output_path = 'database_data.csv'

combine_csvs(pe_path,team_results_path,output_path)


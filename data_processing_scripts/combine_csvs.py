import pandas as pd
from fuzzywuzzy import process

for i in range(8,25):
    if i < 10:
        team_file_name = "200" + str(i) + "_team_results.csv"
    else:
        team_file_name = "20" + str(i) +  "_team_results.csv"
    team_stats_df = pd.read_csv(team_file_name)

    # Load the CSV file containing win/loss data
    win_loss_df = pd.read_csv('win_loss.csv')

    # Function to find the closest match for a team name
    def find_closest_match(team, choices, threshold=80):
        match, score = process.extractOne(team, choices)
        if score >= threshold:
            return match
        return None

    # Create a list to store teams not found in the team data
    teams_not_found = []

    # Update the 'Opponent' column in win_loss_df with the closest match from team_stats_df
    for index, row in win_loss_df.iterrows():
        closest_match = find_closest_match(row['Opponent'], team_stats_df['team'])
        if closest_match:
            win_loss_df.at[index, 'Opponent'] = closest_match
        else:
            teams_not_found.append(row['Opponent'])

    # Merge the dataframes based on the opponent name
    merged_df = pd.merge(team_stats_df, win_loss_df, left_on='team', right_on='Opponent', how='inner')

    # Select and rename columns as per the required format
    final_df = merged_df[['team', 'Opponent', 'adjoe', 'adjde', 'Season', 'Home/Away', 'Win/Loss']]

    # Save the final dataframe to a new CSV file
    final_df.to_csv('combined_stats.csv', index=False)

    # Print the list of teams not found in the team data
    print("Teams not found in team data:", teams_not_found)
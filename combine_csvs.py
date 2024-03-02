import pandas as pd
from fuzzywuzzy import process

def merge_stats_and_results(stats_file, schedule_file, output_file, threshold=82):
    # Load the CSV files
    stats_df = pd.read_csv(stats_file)
    schedule_df = pd.read_csv(schedule_file)

    # Get Utah State's stats
    usu_stats = stats_df[stats_df['team'] == 'Utah St.'].iloc[0]

    # Get the list of team names for matching
    team_names = stats_df['team'].tolist()

    # Initialize an empty list to store the merged data
    merged_data = []

    # Iterate through each row in the schedule dataframe
    for index, row in schedule_df.iterrows():
        opponent = row['Opponent']
        home_away = row['Home/Away']
        win_loss = row['Win/Loss']

        # Find the best match for the opponent's name using fuzzy matching
        best_match, match_score = process.extractOne(opponent, team_names)

        # Check if the match score is above the threshold
        if match_score >= threshold:
            # Get the opponent's stats based on the best match
            opponent_stats = stats_df[stats_df['team'] == best_match]

            # Add the home/away and win/loss columns
            opponent_stats = opponent_stats.copy()
            opponent_stats['Home/Away'] = home_away
            opponent_stats['Win/Loss'] = win_loss

            # Add Utah State's stats to the row
            for col in usu_stats.index:
                opponent_stats[f'USU_{col}'] = usu_stats[col]

            merged_data.append(opponent_stats)
        else:
            print(f"No close match found for {opponent} (best match: {best_match} with score {match_score})")

    # Check if merged_data is empty
    if not merged_data:
        raise ValueError("No matching opponents found after fuzzy matching.")

    # Concatenate all the merged data into a single dataframe
    merged_df = pd.concat(merged_data, ignore_index=True)

    # Write the merged data to a new CSV file
    merged_df.to_csv(output_file, index=False)


for i in range(8,25):
    if i < 10:
        stats_file_path = 'data/200' + str(i) + '_team_results.csv'
        schedule_file_path = 'data/usu_sched_0' + str(i) + '.csv'
        output_file_path = 'data/merged_stats_0' + str(i) + '.csv'
    else:
        stats_file_path = 'data/20' + str(i) + '_team_results.csv'
        schedule_file_path = 'data/usu_sched_' + str(i) + '.csv'
        output_file_path = 'data/merged_stats_' + str(i) + '.csv'
    merge_stats_and_results(stats_file_path, schedule_file_path, output_file_path)
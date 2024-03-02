import pandas as pd

def combine_usu(input_file, output_file):
    stats = pd.read_csv(input_file)

    # Assuming 'Team' is the column name containing team names
    usu_stats = stats[stats['team'] == 'Utah St.'].iloc[0]

    # Add the USU stats to every row in the input CSV
    for col, value in usu_stats.items():
        stats['USU_' + col] = value

    # Save the updated DataFrame to a new CSV file
    stats.to_csv(output_file, index=False)

# Example usage
input_file = 'data/database_data.csv'
output_file = 'data/prediction_data.csv'
combine_usu(input_file, output_file)

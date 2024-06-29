import pandas as pd

# Define the input file path
input_file_path = 'cleaned_data.txt'
output_file_path = 'fetched_table.csv'

# Read the data from the file
with open(input_file_path, 'r') as infile:
    lines = infile.readlines()

# Initialize lists to store the table data
cycles = []
instructions = []
stages = []

# Iterate through the lines and extract necessary information
for line in lines:
    parts = line.split(':')
    cycle = int(parts[0].strip())
    stage = parts[1].strip()
    instruction = line

    cycles.append(cycle)
    instructions.append(instruction)
    stages.append(stage)

# Create a DataFrame to represent the table
data = {
    'Cycle': cycles,
    'Instruction': instructions,
    'Stage': stages
}

df = pd.DataFrame(data)

# Create a DataFrame to hold the final table
max_cycle = max(cycles)
header = list(range(max_cycle + 1))
final_table = pd.DataFrame(columns=header)

# Populate the final table with the stages
for index, row in df.iterrows():
    cycle = row['Cycle']
    instruction = row['Instruction']
    stage = row['Stage']

    if instruction not in final_table.index:
        final_table.loc[instruction] = [''] * (max_cycle + 1)

    final_table.at[instruction, cycle] = stage

# Save the DataFrame to a CSV file for review
final_table.to_csv(output_file_path)

print(f"Table has been written to {output_file_path}")

import csv

# Input and output file paths
input_file = 'fetched_table.csv'
output_file = 'fetched_table_1.csv'


# Function to modify the instruction part of each line
def modify_instruction(line):
    # Find the position of the first space after the bracket (indicating the end of the instruction)
    first_space_index = line.find(' ', line.find(']'))

    # Extract the instruction part from the line
    if first_space_index != -1:
        instruction_part = line[first_space_index + 1:].strip()  # Extracting from the space onwards
        return instruction_part.split(' [')[0].strip()


# Read CSV file, modify the instruction part, and write to a new CSV file
with open(input_file, 'r', newline='') as csv_file, open(output_file, 'w', newline='') as output:
    reader = csv.reader(csv_file)
    writer = csv.writer(output)

    for row in reader:
        if row:  # Ensure row is not empty
            # Extract the modified instruction part
            modified_instruction = modify_instruction(row[0])
            # Create a new row with the modified instruction part and the rest unchanged
            modified_row = [modified_instruction] + row[1:]
            # Write the modified row to the output file
            writer.writerow(modified_row)

print(f"Modified data saved to '{output_file}'.")

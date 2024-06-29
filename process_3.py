import csv

# Input and output file paths
input_file = 'fetched_table_1.csv'
output_file = 'fetched_table_2.csv'

# Function to modify the CSV rows
def modify_rows(row):
    modified_row = []
    for cell in row:
        if cell.strip() == 'fetch':  # Replace 'fetch' with 'IF	ID	EX	Mem	WB'
            modified_row.extend(['IF', 'ID', 'EX', 'Mem', 'WB'])
        else:
            modified_row.append(cell.strip())
    return modified_row

# Read CSV file, modify each row, and write to a new CSV file
with open(input_file, 'r', newline='') as csv_file, open(output_file, 'w', newline='') as output:
    reader = csv.reader(csv_file)
    writer = csv.writer(output)

    for row in reader:
        if row:  # Ensure row is not empty
            modified_row = modify_rows(row)  # Modify the row
            writer.writerow(modified_row)  # Write the modified row to the output file

print(f"Modified data saved to '{output_file}'.")

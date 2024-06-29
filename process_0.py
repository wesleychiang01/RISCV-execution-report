# Open and read the text file
with open('ori_data.txt', 'r') as file:
    log_data = file.readlines()

# Extract lines with only the fetch stage
fetch_lines = [line for line in log_data if 'fetch :' in line]

# Write the fetch lines to a new file
with open('cleaned_data.txt', 'w') as file:
    file.writelines(fetch_lines)

# Print the fetch lines
for line in fetch_lines:
    print(line.strip())

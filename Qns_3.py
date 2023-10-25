
# Specify the file name
file_name = 'sample-file.txt'

# Initialize a counter to keep track of the lines with 'q'
count = 0

# Open the file and read it line by line
with open(file_name, 'r') as file:
    for line in file:
        # Check if 'q' is in the line (case-insensitive)
        if 'q' in line.lower():
            # If 'q' is found, increment the counter
            count += 1

# Print the result
print(f"Number of lines with 'q': {count}")

# Initialize a counter to keep track of the lines with 'q'
count = 0

# Open the file and read it line by line
with open(file_name, 'r') as file:
    for line in file:
        # Check if 'q' is in the line (case-insensitive)
        if 'q' in line.lower():
            # If 'q' is found, increment the counter
            count += 1

# Print the result
print(f"Number of lines with 'q': {count}")

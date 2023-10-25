from random import sample

for i in range(0,100):

    a= sample (['1','2','3'],1)
    b= sample (['1','2','3'],1)

    file_a = open (file='file1.txt', mode='a')
    file_b = open (file='file2.txt', mode='a')

    file_a.write('\n'+ a[0])
    file_b.write('\n'+ b[0])

    file_a.close()
    file_b.close()

#you need to write a  for loop to read the files line by line and compare the values


# Files are automatically closed when exiting the 'with' block

# Now, you can use the code below to read and compare the values in the files.
# This code assumes that both files have the same number of lines.

# Open the files for reading
with open('file1.txt', 'r') as file_a, open('file2.txt', 'r') as file_b:
    # Read all lines from 'file1.txt' and 'file2.txt'
    lines_a = file_a.readlines()
    lines_b = file_b.readlines()

# Check if both files have the same number of lines
if len(lines_a) != len(lines_b):
    print("The files have a different number of lines.")
else:
    # Loop through each line and compare the values
    for i in range(len(lines_a)):
        # Remove any leading or trailing whitespace and store the values
        value_a = lines_a[i].strip()
        value_b = lines_b[i].strip()

        # Compare the values and print the result
        if value_a == value_b:
            print(f"Line {i + 1}: Values match - '{value_a}' in file1.txt and '{value_b}' in file2.txt")
        else:
            print(f"Line {i + 1}: Values do not match - '{value_a}' in file1.txt and '{value_b}' in file2.txt")

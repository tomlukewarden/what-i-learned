# Open the file in read mode ('r')
# This allows us to read the contents of the file.
with open('example.txt', 'r') as text:
    
    # Read the file line by line into a list using readlines()
    # The readlines() method reads the entire file, but it returns it as a list of strings.
    # Each string in the list represents a single line in the file, including the newline character '\n' at the end of each line.
    lines = text.readlines()

    # The 'lines' variable is now a list, where each item corresponds to a line from the file.
    print("File content (line by line):")
    
    # Iterate over the list of lines and print each one
    # The for loop will go through each line (which is a string) in the 'lines' list
    for line in lines:
        # Use strip() to remove the newline character '\n' from the end of each line
        # Without strip(), the print() would display each line with an extra blank line due to the '\n'.
        print(line.strip())  # .strip() removes the newline character, leaving just the text

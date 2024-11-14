# Open a text file in write mode ('w')
# The 'with' statement ensures the file is properly closed after we're done writing to it.
with open('example.txt', 'w') as text:  
    # Write content to the file. Each write adds the text as a new line in the file.
    text.write("Hello, this is a sample text written to the file.\n")
    # Adding a second line of text
    text.write("This is the second line of the file.\n")
    # Adding a third line of text
    text.write("We can write as many lines as we want.\n")

# Print confirmation message after the file has been written.
print("Text has been written to the file.")


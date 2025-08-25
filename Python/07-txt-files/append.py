# Open a text file in append mode ('a')
# This will allow you to add content to the end of the file without modifying the existing content.
with open('example.txt', 'a') as text:  
    # Append a new line of text to the file
    text.write("This is an additional line added to the file.\n")
    # Adding another line of text
    text.write("Appending more content is possible without erasing previous data.\n")

# Print confirmation message after appending text to the file.
print("Text has been appended to the file.")

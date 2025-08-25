# Open the file in read mode ('r')
# This will allow you to read the contents of the file.
with open('example.txt', 'r') as text:
    # Read the entire content of the file into a single string
    content = text.read()
    print("File content:")
    print(content)

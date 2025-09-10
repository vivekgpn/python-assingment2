# Read from a file program

# Open the file in read mode ("r")
file = open("myfile.txt", "r")

# Read content
content = file.read()

# Close the file
file.close()

# Display content
print("File content is:\n")
print(content)


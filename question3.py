# Write to a file program

# Open a file in write mode ("w")
file = open("myfile.txt", "w")  # agar file exist nahi karti to create ho jaayegi

# Write content to file
file.write("Hello, this is a sample file.\n")
file.write("Python makes file handling easy!\n")

# Close the file
file.close()

print("File written successfully.")



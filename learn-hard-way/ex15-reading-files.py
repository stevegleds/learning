#import the argv from sys to allow the passing of parameters
from sys import argv

#Assign names to the arguments passed to the script when started
script, filename = argv

#open the file whose parameter was passed and assign the txt' variale name
txt = open(filename)

#prints out a message including the filename
print("Here's your file {} " .format(filename))
#print out the contexts of the file . The read command with no parameters
print(txt.read())

#Print a statement
print("Type the filename again:")
#prompt for the filename and display a prompt. Assign to variable
file_again = input("> ")

#assign the contents of the filename to a variable
txt_again = open(file_again)

# Print the content of the file using read command with no parameters.
print(txt_again.read())

#now we close the files
txt.close()
txt_again.close()
"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# 'r' when the file will only be read, 
# 'w' for only writing (an existing file with the same name will be erased)
# 'a' opens the file for appending; any data written to the file is automatically added to the end 
# 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.
# 'x' will create a file, returns an error if the file exist
# 'w' will create a file if the specified file does not exist
# YOUR CODE HERE
f = open('foo.txt', "r")
print(f.read())
f.close

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
doc = open("bar.txt", "w")
doc.write("THis is a line of text.  This is another line of text.  This is yet another line of text")
doc.close()
doc = open("bar.txt", "r")
print(doc.read())
doc.close()
doc = open("bar.txt", "w")
doc.write('I changed the text to check what I did')
doc.close()
doc = open("bar.txt", "r")
print(doc.read())
doc.close()
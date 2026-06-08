# What is a Context Manager - A cleanup friend which gets called automatically if developer forgets  to cleanup
# Eg: In File I/O, without the "with" statement , we have to manually close the file using f.close(), with the help of context manager "with open" it is not needed to close the file, CM automatically handels the cleanup
# Useful case when needed - automatic cleanup, avoiding resource leakage
# Also can be used for Database Connection Management

# A class-based context manager called FileManager:

# It should:
# open a file in write mode
# write some text inside
# close file automatically
# Even if an error happens inside with block

class FileManager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.filename = open(self.filename, self.mode)
        return self.filename
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.filename:
            self.filename.close()
        return False
    

try:
    with FileManager("testfile.txt","r") as r:
        print(r.read())
except FileNotFoundError:
    print("file not found")



# def __exit__ - always gets 3 args + 1 self = 4 args as parameters
# else it throws error
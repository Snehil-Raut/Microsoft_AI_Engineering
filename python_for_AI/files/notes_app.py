# Features: add note ,view notes ,delete all notes 
# You’ll practice: append mode reading menus loops
from pathlib import Path   # this is new approach to delete a file
import logging

logging.basicConfig(filename='app_error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def notes():
    print("Choose option:\n 1) View notes\n 2) Add/append notes\n 3) Delete notes\n 4) exit")

    choice = int(input("Enter your choice (1,2,3,4,5) "))
    print("\n")

    if(choice==1):
        view_notes()
    elif(choice==2):
        add_notes()
    elif(choice==3):
        delete_notes()
    elif(choice==4):
        exit_notes()
    else:
        print("Please enter valid choice")

# this function is to read from the notes if the notes exist , else it shows file is not present
def view_notes():
    file_path = input("Give the name of file you want to read ")
    try:
        with open(file_path,"r") as read:
            print(f"Your Notes file is opened\n")
            print(read.read())
            

    # Logging error to app_error.log file
    except FileNotFoundError as e:
        logging.error(f"Falied to process the: {file_path}. Error details {e} ")
        

# this function will Append to exisitng file or Overwrite the exisitng file with new data or create a new file and write to it
def add_notes():

    print("Choose 1) Append to exisiting file\n 2) Overwrite an exising file(old content will be deleted)\n 3) create a new file and write to it")
    choice = int(input("Enter your choice (1,2,3) "))
    

    if (choice==1):
        file_path1 = input("Provide the name of file you want to edit ")
        try:
            with open(file_path1, "a") as appending:
                appending.write("rice\nwheat\ncar wash\nnotebooks purchase\ngym")
            print("New notes are appended")

        except FileNotFoundError as e:
            logging.error(f"Falied to process the: {file_path1}. Error details {e} ")

    elif(choice==2):
        file_path2 = input("Provide the name of file you want to edit ")
        try:
            with open(file_path2, "w") as overwrite:
                overwrite.write("Day 1 - beach\nDay 2 - sight seeing\nDay 3 - petrol refilling\nDay 4 - clubbing\nDay 5 - Home")
            print("New content is over-written")

        except FileNotFoundError as e:
            logging.error(f"Falied to process the: {file_path2}. Error details {e} ")
            
    else:
        file_path3 = input("Provide the name of file you want to edit ")
        try:
            with open(file_path3, "x") as newfile:
                newfile.write("Trekking\nnight out\nbday party\nstudying")
            print("File created successfully.")
            

        except FileExistsError as e:
            logging.error(f"Falied to process the: {file_path3}. Error details {e} ")
            

# delete notes 
def delete_notes():
    file_path = Path(input("Provide the name of file you want to delete "))
    file_path.unlink(missing_ok=True)
    

# Exit the app
def exit_notes():
    exitnotes = (input("Exit?, Yes/No ")).lower()
    if(exitnotes=="yes"):
        print("App EXIT")
    else:
        notes()

notes()


# put the error of filenot found in logs.txt
# importing the necessary modules from tkinter
import tkinter
from tkinter import *

#creates the main pop-up window
root = Tk()
root.title("CheckMate - Brooklyn and Hope")
root.geometry("400x650+400+100")
root.resizable(False,False)
root.configure(bg="#0b283c")

# list to store tasks
task_list = []

# function to add a task to the list
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        # adding a task to the list and writing to a file
        with open("tasklist.text", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

# function to delete a selected task
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        # updating the file after removing the task
        with open("tasklist.txt", 'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        
        listbox.delete( ANCHOR)

# function to open and load tasks from a file
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks: 
            if task != '\n':
                task_list.append(task)
                listbox.inset(END , task)

    except:
        # creating the file if not found
        file = open('tasklist.txt', 'w')
        file.close()

# setting up icon 
Image_icon = PhotoImage(file = "Image/task.png")
root.iconphoto(False, Image_icon)

# setting up dock image position
dockImage = PhotoImage (file = "Image/dock.png")
Label(root, image = dockImage, bg = "#0b283c").place(x = 30, y = 25)

# setting up logo position and color 
logoImage = PhotoImage(file = "Image/task.png") 
Label(root, image = logoImage, bg = "#0b283c").place(x=340, y= -2)

# setting up App name: Check Mate 
heading = Label(root, text = "Check Mate", font = ("Marker Felt", 40, "bold"), fg = "#c7d5d8", bg = "#0b283c")
heading.place(x = 100, y = 10)


#main section

# Entry bar
frame = Frame(root, width = 400, height = 50, bg = "#8aa6b8")
frame.place(x = 0, y = 180)

task = StringVar()
task_entry = Entry(frame, width = 22, font = ("Times New Roman", 20), bd = 0)
task_entry.place(x = 10, y = 10)
task_entry.focus()

# "ADD" button
button = Button(frame, text = "ADD", font = ("MS Serif", 20, "bold"), width = 6, bg = "#3c5d7c", fg = "#c7d5d8", bd = 0, command =  addTask)
button.place(x = 270, y = 10)


#list box

# frame for the list box
frame1 = Frame(root, bd = 3, width = 700, height = 280, bg = "#3c5d7c")
frame1.pack(pady = (250, 0))

listbox = Listbox(frame1, font = ('times new roman', 14), width = 40, height = 16, bg = "#3c5d7c", fg = "#c7d5d8", cursor = "star", selectbackground = "#5a95ff")
listbox.pack(side = LEFT , fill = BOTH,  padx = 2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

# loading tasks from file
openTaskFile()

#delete button
Delete_icon = PhotoImage(file = "Image/delete.png")
Button(root, image = Delete_icon, bg = "#32405b", bd = 0, command = deleteTask).pack(side = BOTTOM, pady = 13)


# running the main event loop
root.mainloop()
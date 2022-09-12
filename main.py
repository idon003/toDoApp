from tkinter import *       # import everything from tkinter library
import json                 # import json to memoize completed and uncompleted tasks even after closing app

# Let me now create a window where tasks will appear
general_window = Tk()                    # general window where will be created sub windows
general_window.geometry('500x600')       # width and height of window
general_window.title('Notes to do')      # creates title in out window
general_window.config(bg='#F5F5DC')      # sets background color
# windw.resizable(width=False, height=False)      # don't allow resizing

# firstly it'll show text uncompleted taks
title1 = Label(text=" Uncompleted tasks ", fg="black", bg="#9370DB", font=("Times", 20), relief='solid')
title1.pack(pady = 10)

# first child window for showing uncomplted tasks
windw2 = Frame(general_window)       # this child window contains uncompleted tasks
windw2.pack(pady = 10)

# this is for our completed tasks (logic is the same)
title2 = Label(text=" Completed tasks ", fg="black", bg="#00FA9A", font=("Times", 20),relief='solid')
title2.pack(pady = 10)
windw3 = Frame(general_window)       # this child window contains un completed tasks
windw3.pack(pady = 10)

# for now skip functions and look main code
def addTaskFunc():
    button_frame1.pack_forget()         # pack_forget is used to hide buttons
    button_frame3.pack_forget()

    button_frame2 = Frame(general_window)   # create new button that do same as "Submit" buttons
    button_frame2.pack(pady=20)
    
    # Give some details for button
    newTask = Button(
        button_frame2,
        text = 'Add task',
        font = ('Times', 15),
        bg='#c5f776',
        padx=20,
        pady=10,
        command=lambda: newTaskFunc(new_task.get(), new_task, button_frame2) # we called function and gave 3 arguments
        # new_task.get() after we press button new_task.get() will get what is written in entry
        # new_task because after using it we must hide it
        # same as new_task we must hide out button
    )

    # there is an entry function, here user will write task
    new_task = Entry(general_window, font = ('Times', 18))
    new_task.pack(pady=10)
    newTask.pack(side=LEFT, fill=BOTH)

def newTaskFunc(new_task, hide1, hide2):
    # as it was previously mentioned we must hide
    hide1.pack_forget()
    hide2.pack_forget()

    uncmplBox.insert(END, '❑' + new_task) # inserts new task
    data = []

    # now we must save our entered new task to the file (tasks.json)
    # first save data in the file to the dict named data
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    # then as we created uncompleted task we append new task there
    data["uncompleted"].append(new_task)
        
    # finaly we overwrite information in the file using json.dump
    with open('tasks.json', 'w') as f:
        json.dump(data, f)

    # after saving and inserting we again rehide(show) out buttons (new task / mark completed)
    button_frame1.pack(pady=10)
    button_frame3.pack(pady=10)


def deleteTask():
    # get the text where cursor selects and sets it to x without suare box at the beginning
    x = uncmplBox.get(uncmplBox.curselection())[1:]
    # inserts it to completed box
    cmplBox.insert(END, '☑' + x)

    # not the mission is to delete from uncompleted and insert to completed
    # similar approach that was used
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    data["uncompleted"].remove(x) #removes the task from uncompleted
    data["completed"].append(x)   #appends to completed
    
    #overwrites data
    with open('tasks.json', 'w') as f:
        json.dump(data, f)
    uncmplBox.delete(ANCHOR) #anchor is where cursor is deletes what is locating there



# displays uncompleted tasts (listbox)
uncmplBox = Listbox(
    windw2,                      # lisbox located in child window(frame)
    width=25,
    height=6,
    bg='#F5F5DC',                # same background color will be used
    font = ('Times', 16),        # font size and font family
    bd = 0,                      # no borders
    fg = '#2F4F4F',              # color of the text
    highlightthickness = 0,      
    selectbackground = '#4B0082',   # targeted task will be highlighted with another color
    activestyle = 'none'            # no underlines
)
uncmplBox.pack(side=LEFT, fill=BOTH)


# completed tasks list
cmplBox = Listbox(
    windw3,                      # lisbox located in child window(frame)
    width=25,
    height=6,
    bg='#F5F5DC',                # same background color will be used
    font = ('Times', 16),        # font size and font family
    bd = 0,                      # no borders
    fg = '#2F4F4F',              # color of the text
    highlightthickness = 0,      
    selectbackground = '#4B0082',   # targeted task will be highlighted with another color
    activestyle = 'none'            # no underlines
)
cmplBox.pack(side=LEFT, fill=BOTH)

# Creates list of tasks
with open('tasks.json', 'r') as f:
  data = json.load(f)
  cmpl_tasks = data['completed']
  uncmpl_tasks = data['uncompleted']

# inserts data in arrays to listbox
for task in uncmpl_tasks:
    uncmplBox.insert(END, '❑' + task)

for task in cmpl_tasks:
    cmplBox.insert(END, '☑' + task)


# Scrollbar
sBar = Scrollbar(windw2)                # creates scrollbar on window2
sBar.pack(side=RIGHT, fill=BOTH)        # places it in the right of child window

uncmplBox.config(yscrollcommand=sBar.set)
sBar.config(command=uncmplBox.yview)


sBar2 = Scrollbar(windw3)                # creates scrollbar on window2
sBar2.pack(side=RIGHT, fill=BOTH)        # places it in the right of child window

cmplBox.config(yscrollcommand=sBar2.set)
sBar2.config(command=cmplBox.yview)


# button to add task
button_frame1 = Frame(general_window)
button_frame1.pack(pady=10)

button_frame3 = Frame(general_window)
button_frame3.pack(pady=10)

addTask = Button(
    button_frame1,
    text = 'New task',
    font = ('Times', 15),
    bg='#c5f776',
    padx=20,
    pady=10,
    command = addTaskFunc # calls function
)
addTask.pack(side=LEFT, fill=BOTH)


delTask = Button(
    button_frame3,
    text='Mark completed',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask.pack(fill=BOTH, expand=True, side=LEFT)

general_window.mainloop()        # infinite loop that holds window opened
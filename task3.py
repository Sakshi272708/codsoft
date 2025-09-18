#TO-DO-LIST
from tkinter import*
win=Tk()
win.title("TO-DO-LIST")
win.geometry("300x400")
#to show task
listbox=Listbox(win,width=40,height=30)
listbox.pack(pady=10)
entry_task=Entry(win,width=35)
entry_task.pack(pady=5)
#add task
def add_task():
    task=entry_task.get()
    if task != "":
        listbox.insert(END,task)
        entry_task.delete(0,END)
def delete_task():
    try:
        selected_task=listbox.curselection()
        listbox.delete(selected_task)
    except:
        pass
add_button=Button(win,text="Add task",command=add_task)
add_button.pack(pady=5)
delete_button=Button(win,text="delete Task",command=delete_task)
delete_button.pack(pady=5)
win.mainloop()
import tkinter
import tkinter.messagebox
root=tkinter.Tk()
root.title("To-Do List by apeksha")

def add_task():
    task=Entry_task.get()
    if task != " ":
     Listbox_task.insert(tkinter.END, task)
     Entry_task.delete(0,tkinter.END)

    else:
       tkinter.messagebox.showwarning(title="warning!", message="you must enter a task.")

def delete_task ():
 try:
   task_index = Listbox_task.curselection()[0]
   Listbox_task.delete(task_index)   
 except:
   tkinter.messagebox.showwarning(title="warning!", message="you must select a task.")   
    
#creat GUI
frame_tasks = tkinter.Frame(root) 
frame_tasks.pack()

Listbox_task = tkinter.Listbox(frame_tasks,height=8,width=55)
Listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_tasks)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

Listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=Listbox_task.yview)

Entry_task=tkinter.Entry(root,width=60,text=" ")
Entry_task.pack()

button_add_task=tkinter.Button(root,height=2, text="Add task", width=24,bg="red", command=add_task)
button_add_task.pack(side=tkinter.RIGHT)

button_delete_task=tkinter.Button(root,height=2, text="Delete task", width=24,bg="blue", command=delete_task)
button_delete_task.pack(side=tkinter.LEFT)


root.mainloop()
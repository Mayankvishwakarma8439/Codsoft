from tkinter import *
import tkinter.messagebox
from tkinter.font import Font
import pickle
root=Tk()
root.title('To-Do List')
root.geometry("500x600")
root.configure(bg="#99dee7")
icon=PhotoImage(file="pythonprojects/bg2.png")
root.iconphoto(FALSE,icon)

my_entry= Entry(root,font=("Century Schoolbook",25))
my_entry.pack(pady=40)

button_frame=Frame(root)
button_frame.pack(pady=5)

def add_item():
    the_list.insert(END,my_entry.get())
    my_entry.delete(0,END)
def delete_item():
        the_list.delete(ANCHOR)

def save_item():
    items=the_list.get(0,the_list.size())
    pickle.dump(items,open("saved.file","wb"))
def load_item():
   try:
       items=pickle.load(open("saved.file","rb"))
       the_list.delete(0,END)
       for i in items:
          the_list.insert(END,i)
   except:
       tkinter.messagebox.showwarning(title="Warning!", message="Can't find any saved item.")

    
add_button=Button(button_frame,text="Add item",background="#fcd07b",font=("arial",12,"bold"),width=50,command=add_item)
delete_button=Button(button_frame,text="Delete item",font=("arial",12,"bold"),background="#fcd07b",width=50,command=delete_item)
exit_button=Button(button_frame,font=("arial",12,"bold"),text="Exit",width=50,background="#fcd07b",command=exit)
save_button=Button(button_frame,font=("arial",12,"bold"),text="Save item",background="#fcd07b",width=50,command=save_item)
load_button=Button(button_frame,font=("arial",12,"bold"),text="Load item",background="#fcd07b",width=50,command=load_item)

add_button.pack(pady=5)
delete_button.pack(pady=5)
save_button.pack(pady=5)
load_button.pack(pady=5)
exit_button.pack(pady=5)

frame=Frame(root)
frame.pack(pady=20)
scro_ll=Scrollbar(frame)
scro_ll.pack(side=RIGHT,fill="both")


the_list=Listbox(frame,width=70,height=50,font=("Lucida Calligraphy Italic",20),bd=0 ,highlightthickness=0,selectbackground="#4bbedb")
the_list.pack(pady=10)
the_list.config(yscrollcommand=scro_ll.set)
scro_ll.config(command=the_list.yview)
root.mainloop()
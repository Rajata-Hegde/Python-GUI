from tkinter import *
from tkinter import messagebox
def clear():
    window.destroy()
    create_main_window()
def exo():
    window.destroy()
    create_main_window()
def show():
    global f_entry,tuple_data
    a = f_entry.get()
    set_data.add(a)
    result_label.config(text=f"the set is {set_data}",font=("arial black",25),bg="#97eb9d")
def addition():
    global f_entry
    add_label=Label(window,text="enter the elements to add",font=("arial black",20))
    add_label.pack()
    f_entry=Entry(window)
    f_entry.pack()
    display_button=Button(text="display the set",command=show,font=("times new horizon",15),bg="sky blue")
    display_button.pack(pady=10)
def remove():
    global f_entry
    a = f_entry.get()
    if a in set_data:
        set_data.discard(a)
        result_label.config(text=f"the set is {set_data}",bg="#97eb9d")
    else:
        messagebox.showinfo(title="warning",message="Error")
def dele():
    global f_entry
    add_label = Label(window, text="enter the element to delete",font=("arial black",20))
    add_label.pack()
    f_entry = Entry(window)
    f_entry.pack()
    display2_button = Button(text="display the set after deleting", command=remove,font=("arial black",20),bg="sky blue")
    display2_button.pack(pady=10)
def set_operations():
    add_button=Button(window,text="insert",command=addition,font=("times new roman",15),bg="sky blue")
    add_button.pack()
    del_button=Button(window,text="delete",command=dele,font=("times new roman",15),bg="sky blue")
    del_button.pack()
    clear_button = Button(window, text="exit from set", command=clear,font=("times new roman",15),bg="sky blue")
    clear_button.pack()
def see():
    global f_entry,tuple_data
    a = f_entry.get()
    tuple_data= tuple_data + (a,)
    result_label.config(text=f"the tuple is {tuple_data}",font=("arial black",25),bg="#97eb9d")
def insertion():
    global f_entry
    add_label = Label(window, text="enter the elements to add",font=("arial black",20))
    add_label.pack()
    f_entry = Entry(window)
    f_entry.pack()
    display_button = Button(text="display the tuple",font=("times new horizon",15), command=see,bg="yellow")
    display_button.pack()
def deletion():
    global tuple_data
    del(tuple_data)
    result_label.config(text="the entire tuple is deleted",font=("arial black",25),bg="#97eb9d")
def tuple_operations():
    add_button = Button(window, text="insert",command=insertion,bg="yellow",font=("times new roman",15))
    add_button.pack()
    del_button = Button(window, text="delete",command=deletion,bg="yellow",font=("times new roman",15))
    del_button.pack()
    exit_button = Button(window, text="exit from tuple",command=exo,bg="yellow",font=("times new roman",15))
    exit_button.pack()
def exit_op():
    exit(0)
def create_main_window():
    global window, result_label, set_data,tuple_data
    window=Tk()
    photo=PhotoImage(file="C:\\Users\\rajat\\OneDrive\\Desktop\\first sem\\coding\\Python-GUI\\rv new logo.png").subsample(2,2)
    set_data = set()
    tuple_data = tuple()
    window.title("python GUI programme for set and tuple operations")
    window.config(background="#ff9999")
    label=Label(window,
                image=photo,
                compound="left",
                 text="This is the gui programme to implement set and tuple operations"
                      "\n by clicking on set you will get options like insert and delete insert helps to add elements to set\nand delete option used to delete the particular value from set"
                      "\n tuple has options like adding values and delete the entire tuple \n terminate will exit the screen"
                      "\n CLICK ON THE OPTION YOU WANT",font=("Calibri",14),bg="#ffe6e6")
    label.pack()
    label2 = Label(window, text="click on the choice you want",font=("arial black",20),bg="yellow")
    label2.pack(side="left")
    set_button=Button(window,
           text="set",command=set_operations,bg="violet",font=("arial black",20))
    set_button.pack(side="left",pady=5,padx=10)
    tup_button=Button(window,
           text="tuple",command=tuple_operations,bg="violet",font=("arial black",20))
    tup_button.pack(side="left",pady=5,padx=10)
    exit_button=Button(window,
           text="terminate",command=exit_op,bg="violet",font=("arial black",20))
    exit_button.pack(side="left",pady=5,padx=10)
    result_label = Label(window)
    result_label.pack()
    window.mainloop()
create_main_window()

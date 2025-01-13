from tkinter import *
from tkinter import messagebox
window = Tk()
photo=PhotoImage(file="C:\\Users\\rajat\\OneDrive\\Desktop\\first sem\\coding\\Python-GUI\\rv new logo.png").subsample(2,2)
window.geometry("1500x880")
window.title("python gui programme for experiential learning to find largest prime factor")
window.config(background="#e6b67c")
f_label = Label (window,
                 image=photo,
                 compound="left",
                text="This is the G U I programme to find largest prime factor:\n "
                     "A prime factor is a prime number that divides another number without leaving a remainder."
                     "\n for example the prime factors of 18 are 2*3*3 in which 3 is the largest prime factor. "
                     "\n \n **Do not enter 0 and 1 as they are not prime numbers."
                 "\n \n  enter the number which you have to find prime factor.",
                 font=(" Cambria Math",15),
                bg="skyblue",fg="indigo")
f_label.pack(side="top", pady=10)
def delete():
    f_entry.delete(0, END)
    result_label.config(text="")
def largest_prime_factor(a):
    max = -1
    while a % 2 == 0:
        max = a
        a = a / 2
    for i in range(3, int(a ** 0.5) + 1, 2):
        while a % i == 0:
            max = i
            a = a / i
    if a>2:
        max = a
    return int(max)
def click():
    try:
        a = int(f_entry.get())
        if(a==0 or a==1 or a<0):
            messagebox.showwarning(title="warning",
                                   message="ERROR")
        result = largest_prime_factor(a)
        result_label.config(text=f"Largest Prime Factor of {a} is {result}")
    except ValueError:
        messagebox.showwarning(title="warning",
                               message="enter a valid input")
f_label = Label (window,
                text="enter the number to find largest prime factor:",
                 font=("arial black",35),
                bg="violet")
f_label.pack(side="top", pady=15)
f_entry = Entry(window,width=20,font=35,borderwidth=25)
f_entry.pack(side='top',padx=20,pady=10)
cal = Button(window,
             text="calculate",
             command=click,
             bg="yellow",
             fg="black",
             font=("cooper black",25))
cal.pack(anchor="center",pady="10")
del_button = Button(window,
                    text="clear",
                    command=delete,
                    bg="violet",
                    font=12)
del_button.pack(anchor="se")
result_label = Label(window,
                     font=("arial black",35),bg="light green")
result_label.pack(anchor="center",pady="10")
window.mainloop()

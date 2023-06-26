import tkinter
from tkinter import messagebox


l = tkinter.Tk()
l.title("Dashboard form")
l.geometry('500x750')
l.configure(bg='#333333')



frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Dashboard in progress", bg='#333333', fg="#FF3399", font=("Arial", 30))

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

frame.pack()

l.mainloop()
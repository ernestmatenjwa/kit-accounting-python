import tkinter
from tkinter import messagebox


l = tkinter.Tk()
l.title("Login form")
l.geometry('500x750')
l.configure(bg='#333333')

def login():
    if username_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror(title="Error", message="All Fields are required.")
    else:
        frame.destroy()
        l.destroy()
        import dashboad
def login_p():
    frame.destroy()
    l.destroy()
    import signup

def forgot():
    if username_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror(title="Error", message="All Fields are required.")
    else:
        messagebox.showinfo(title="do something", message="do something")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 22))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="             Login                 ", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)
f_button = tkinter.Button(
    frame, text="Forgoten password?", bg="#333333", fg="#FFFFFF", highlightthickness=0, borderwidth=0, font=("Arial", 11), command=forgot)
c_button = tkinter.Button(
    frame, text="Dont have an account? create", bg="#333333", fg="#FFFFFF", highlightthickness=0, borderwidth=0, font=("Arial", 11), command=login_p)
# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0, pady=10)
username_entry.grid(row=2, column=0)
password_label.grid(row=3, column=0, pady=10)
password_entry.grid(row=4, column=0)
login_button.grid(row=6, column=0, columnspan=2, pady=10)
f_button.grid(row=5, column=0, columnspan=2, pady=10)
c_button.grid(row=7, column=0, columnspan=2)
frame.pack()

l.mainloop()
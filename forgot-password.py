import tkinter
from tkinter import messagebox


fp = tkinter.Tk()
fp.title("Reset form")
fp.geometry('500x750')
fp.configure(bg='#333333')

def forgot():
    if username_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror(title="Error", message="All Fields are required.")
    else:
        fpp.destroy()
        fp.destroy()
        import login

fpp = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    fpp, text="Reset Password", bg='#333333', fg="#FF3399", font=("Arial", 22))
username_label = tkinter.Label(
    fpp, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(fpp, font=("Arial", 16))
password_entry = tkinter.Entry(fpp, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    fpp, text="New Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
password1_entry = tkinter.Entry(fpp, show="*", font=("Arial", 16))
password1_label = tkinter.Label(
    fpp, text="Confirm Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    fpp, text="             Submit               ", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=forgot)
# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0, pady=10)
username_entry.grid(row=2, column=0)
password_label.grid(row=3, column=0, pady=10)
password_entry.grid(row=4, column=0)
password1_label.grid(row=5, column=0, pady=10)
password1_entry.grid(row=6, column=0)
login_button.grid(row=7, column=0, columnspan=2, pady=10)
fpp.pack()

fp.mainloop()
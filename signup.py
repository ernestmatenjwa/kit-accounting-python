import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("Signin form")
window.geometry('500x750')
window.configure(bg='#333333')


def reg():
    if username_entry.get()=="" or password_entry.get()=="" or e_entry.get()=="" or p_entry.get()=="" or ph_entry.get()=="" or bs_entry.get()=="" or fn_entry.get()=="":
        messagebox.showerror(title="Error", message="All Fields are required.")
    else:
        messagebox.showinfo(title="do something", message="do something")

def sign_p():
    s.destroy()
    window.destroy()
    import login
s = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    s, text="Register", bg='#333333', fg="#FF3399", font=("Arial", 22))
username_label = tkinter.Label(
    s, text="Business Name", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
username_entry = tkinter.Entry(s, font=("Arial", 16))
password_entry = tkinter.Entry(s, font=("Arial", 16))
password_label = tkinter.Label(
    s, text="Phone Number", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
e_label = tkinter.Label(
    s, text="Email Address", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
e_entry = tkinter.Entry(s, font=("Arial", 16))
p_label = tkinter.Label(
    s, text="Postal Address", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
p_entry = tkinter.Entry(s, font=("Arial", 16))
ph_label = tkinter.Label(
    s, text="Physical Address", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
ph_entry = tkinter.Entry(s, font=("Arial", 16))
bs_label = tkinter.Label(
    s, text="Business Slogan", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
bs_entry = tkinter.Entry(s, font=("Arial", 16))
fn_label = tkinter.Label(
    s, text="Fax Number", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
fn_entry = tkinter.Entry(s, font=("Arial", 16))
login_button = tkinter.Button(
    s, text="            Register             ", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=reg)
c_button = tkinter.Button(
    s, text="Have an account? Login", bg="#333333", fg="#FFFFFF", highlightthickness=0, borderwidth=0, font=("Arial", 11), command=sign_p)
# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
username_label.grid(row=1, column=0)
username_entry.grid(row=2, column=0)
password_label.grid(row=3, column=0)
password_entry.grid(row=4, column=0)
e_label.grid(row=5, column=0)
e_entry.grid(row=6, column=0)
p_label.grid(row=7, column=0)
p_entry.grid(row=8, column=0)
ph_label.grid(row=9, column=0)
ph_entry.grid(row=10, column=0)
bs_label.grid(row=11, column=0)
bs_entry.grid(row=12, column=0)
fn_label.grid(row=13, column=0)
fn_entry.grid(row=14, column=0)
login_button.grid(row=15, column=0, columnspan=2, pady=10)
c_button.grid(row=16, column=0, columnspan=2)
s.pack()

window.mainloop()
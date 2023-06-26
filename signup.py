import tkinter
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


window = tkinter.Tk()
window.title("Signin form")
window.geometry('500x750')
window.configure(bg='#333333')

def reg():
    if (
        username_entry.get() == ""
        or password_entry.get() == ""
        or e_entry.get() == ""
        or p_entry.get() == ""
        or ph_entry.get() == ""
        or bs_entry.get() == ""
        or fn_entry.get() == ""
    ):
        messagebox.showerror(title="Error", message="All Fields are required.")
    else:
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='kit_accounting',
                user='root',
                password=''
            )
            if connection.is_connected():
                print('Connected to MySQL database')

            cursor = connection.cursor()

            c_name = username_entry.get()
            c_phone = password_entry.get()
            c_email = e_entry.get()
            c_postal = p_entry.get()
            c_physicalAd = ph_entry.get()
            c_slogan = bs_entry.get()
            c_fax_no = fn_entry.get()
            password = pw_entry.get()

            # Check if any record with the same c_email, c_phone, or c_name already exists
            check_query = "SELECT * FROM business WHERE c_email = %s OR c_phone = %s OR c_name = %s"
            check_values = (c_email, c_phone, c_name)
            cursor.execute(check_query, check_values)
            existing_records = cursor.fetchall()

            if existing_records:
                # Error: Record with the same c_email, c_phone, or c_name already exists
                messagebox.showerror(title="Error", message="Company name, phone number or email already exist in our database.")
            else:
                query = "INSERT INTO business (c_name, c_phone, c_email, c_postal, c_physicalAd, c_slogan, c_fax_no, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (c_name, c_phone, c_email, c_postal, c_physicalAd, c_slogan, c_fax_no, password)

                cursor.execute(query, values)

                connection.commit()
                connection.close()
                messagebox.showinfo(title="Success", message="Business registered successfully")
                s.destroy()
                window.destroy()
                import login
        except Error as e:
            print('Error while connecting to MySQL', e)


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
pw_label = tkinter.Label(
    s, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
pw_entry = tkinter.Entry(s, font=("Arial", 16))
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
pw_label.grid(row=15, column=0)
pw_entry.grid(row=16, column=0)
login_button.grid(row=17, column=0, columnspan=2, pady=10)
c_button.grid(row=18, column=0, columnspan=2)
s.pack()

window.mainloop()
from http import server
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pyodbc

IMAGE_PATH = 'login.jpg'
WIDTH, HEIGHT = 1350, 900

root = Tk()
root.title("Register")
root.geometry('{}x{}'.format(WIDTH, HEIGHT))

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
#canvas.resizable(False, False)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=NW, image=img)

# Register frame

register_frame = Frame(root, bg="white")
register_frame.place(x=580, y=60, height=690, width=660)
#title

title1 = Label(register_frame, text="Register Here", font="Impact 30 bold", fg="#d77337", bg="white").place(x=150, y=20)
# first name
first_name_var = StringVar()
first_name = Label(register_frame, text="First Name",  font="Arial 15", fg="grey", bg="white").place(x=50, y=80)
first_name_entry = Entry(register_frame, font=("Times new roman", 15), textvariable=first_name_var, bg="light grey")
first_name_entry.place(x=50, y=120, width=550, height=35)


# last name
last_name_var = StringVar()
last_name = Label(register_frame, text="Last Name", font="Arial 15", fg="grey", bg="white").place(x=50, y=160)
last_name_entry = Entry(register_frame, font=("Times new roman", 15), textvariable=last_name_var, bg="light grey")
last_name_entry.place(x=50, y=200, width=550, height=35)

# contact no.
contact_var = StringVar()
contact = Label(register_frame, text="Contact No.", font="Arial 15", fg="grey", bg="white").place(x=50, y=240)
contact_entry = Entry(register_frame, font=("Times new roman", 15), textvariable=contact_var, bg="light grey")
contact_entry.place(x=50, y=280, width=550, height=35)

# email id
email_id_var = StringVar()
email_id = Label(register_frame, text="Email_Id", font="Arial 15", fg="grey", bg="white").place(x=50, y=320)
email_id_entry = Entry(register_frame, font=("Times new roman", 15), textvariable=email_id_var, bg="light grey")
email_id_entry.place(x=50, y=360, width=550, height=35)

# Addresss
address_var = StringVar()
address = Label(register_frame, text="Address", font="Arial 15", fg="grey", bg="white").place(x=50, y=400)
address_entry = Entry(register_frame, font=("Times new roman", 15),textvariable=address_var, bg="light grey")
address_entry.place(x=50, y=440, width=550, height=35)

#password
pwd_var = StringVar()
pwd = Label(register_frame, text="Password", font="Arial 15", fg="grey", bg="white").place(x=50, y=480)
pwd_entry = Entry(register_frame, font=("Times new roman", 15),textvariable=pwd_var, bg="light grey")
pwd_entry.place(x=50, y=520, width=550, height=35)

#confirm password
c_pwd_var = StringVar()
c_pwd = Label(register_frame, text="Confirm Password", font="Arial 15", fg="grey", bg="white").place(x=50, y=560)
c_pwd_entry = Entry(register_frame, font=("Times new roman", 15),textvariable=c_pwd_var, bg="light grey")
c_pwd_entry.place(x=50, y=600, width=550, height=35)

def register_data():
    if first_name_var == "" or last_name_var.get()=="" or contact_var.get()=="" or email_id_var.get()=="" or address_var.get() == "" or pwd_var.get() =="" or c_pwd_var.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=root)
    elif pwd_var.get() != c_pwd_var.get():
        messagebox.showerror("Error", "Password does not match", parent=root)
    else:
        try:
            server = 'DESKTOP-G6HANB8'
            database = 'Register'
            # defining our connection string
            conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server}; \
                                   Server=' + server + '; \
                                   Database='+ database +'; \
                                   Trusted_Connection=yes;'
                                  )

            # create the connection cursor
            cursor = conn.cursor()

            # define our insert query and insert the values into the table
            cursor.execute('INSERT INTO User_detail (first_name, last_name, contact, email_id, address, pwd) VALUES(?,?,?,?,?,?)',
                           (first_name_var.get(),
                           last_name_var.get(),
                           contact_var.get(),
                           email_id_var.get(),
                           address_var.get(),
                           pwd_var.get()
                           ))
            # commit the query
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successfull", parent=root)
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

register_bth = Button(root, text="Register Now", bg="#d77337", fg="white", font=("Times new roman", 20), command=register_data).place(x=300, y=690, width=190, height=40)


root.mainloop()
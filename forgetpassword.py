from tkinter import *
from PIL import Image, ImageTk
import pyodbc
from tkinter import messagebox
from tkinter import ttk

IMAGE_PATH = 'login.jpg'
WIDTH, HEIGHT = 900, 700

def forget_password():
        def reset():
            securityquescombo.current(0)
            newpassEntry.delete(0, END)
            answerforgetEntry.delete(0, END)
            txt_user.delete(0, END)
            txt_pwd.delete(0, END)

    # reset password

        def reset_password():
            if securityquescombo.get() == 'Select' or answerforgetEntry.get() == '' or newpassEntry.get() == '':
                messagebox.showerror('Error', 'All Fields Are Required', parent=root3)
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
                    cur = conn.cursor()
                    cur.execute('select * from employee where email=? and question=? and answer=?',
                            (txt_user.get(), securityquescombo.get(), answerforgetEntry.get()))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror('Error', 'Security Question or Answer is Incorrect\n\n\tPlease Try Again ', parent=root3)

                    else:
                       cur.execute('update employee set password=? where email=?', (newpassEntry.get(), txt_user.get()))
                       conn.commit()
                       conn.close()
                       messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=root3)
                       reset()
                       root3.destroy()


                except Exception as e:
                    messagebox.showerror('Error', f"Error due to: {e}", parent=root)
        
        if txt_user.get() == '':
            messagebox.showerror('Error', 'Please enter the email address to reset your password', parent=root)
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

                cur = conn.cursor()
                cur.execute('select * from User_detail where email_id=?', txt_user.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Please enter the valid email address', parent=root)

                else:
                    conn.close()
                    root3 = Toplevel(root)
                    root3.title('Forget Password')
                    root3.geometry('470x560+400+150')
                    root3.config(bg='white')
                    root3.focus_force()
                    root3.grab_set()
                    forgetLabel = Label(root3, text='Forget Password', font=('times new roman', 22, 'bold'), fg="#d77337", bg='white')
                    forgetLabel.place(x=130, y=10)
                    securityquesLabel = Label(root3, text='Security Questions', font=('times new roman', 19, 'bold'),
                                          fg='grey',
                                          bg='white')
                    securityquesLabel.place(x=60, y=80)
                    securityquescombo = ttk.Combobox(root3, font=('times new roman', 19), state='readonly', justify=CENTER,
                                                 width=28)
                    securityquescombo['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your Best Friend Name?',
                    'Your Favourite Teacher?', 'Your Favourite Hobby?')
                    securityquescombo.place(x=60, y=140)
                    securityquescombo.current(0)
                    answerforgetLabel = Label(root3, text='Answer', font=('times new roman', 19, 'bold'), fg='grey',
                                          bg='white')
                    answerforgetLabel.place(x=60, y=180)
                    answerforgetEntry = Entry(root3, font=('times new roman', 19,), fg='black', width=30,
                                          bg='white')
                    answerforgetEntry.place(x=60, y=240)

                    newpassLabel = Label(root3, text='New Password', font=('times new roman', 19, 'bold'), fg='grey',
                                     bg='white')
                    newpassLabel.place(x=60, y=280)
                    newpassEntry = Entry(root3, font=('times new roman', 19,), fg='black', width=30,
                                     bg='white')
                    newpassEntry.place(x=60, y=320)

                    changepassbutton = Button(root3, text='Change Password', font=('arial', 17, 'bold'), bg="#d77337",
                                          fg='white', cursor='hand2', activebackground="#d77337",
                                          activeforeground='black',
                                          command=reset_password)
                    changepassbutton.place(x=130, y=450)
                    root3.mainloop()
                    
            except Exception as e:
                messagebox.showerror('Error', f"Error due to: {e}", parent=root)
    




def login_data():
        if txt_user.get() == '' or txt_pwd.get() == '':
            messagebox.showerror('Error', 'All fields are required')
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

                # define validation to check if email already exist
                # welcome the user to the website to order food
                cursor.execute("select * from User_detail where email_id=? and pwd=?", (txt_user.get(), txt_pwd.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid email or password')
                else:
                    messagebox.showinfo('Success', 'Welcome to MB Foods')
                conn.close()
            except Exception as e:
                messagebox.showerror('Error', f"Error due to : {e}", parent=root)


root = Tk()
root.title("Login Page")
root.geometry('{}x{}'.format(WIDTH, HEIGHT))

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
#canvas.resizable(False, False)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=NW, image=img)

# Login frame

login_frame = Frame(root, bg="white")
login_frame.place(x=290, y=150, height=340, width=500)
title = Label(login_frame, text="Login Here", font="Impact 30 bold", fg="#d77337", bg="white").place(x=90, y=30)
desc = Label(login_frame, text="Don't have an account? Go to register", font="Arial 15", fg="#d77337", bg="white").place(x=90, y=100)
user_name = Label(login_frame, text="Username", font="Arial 15", fg="grey", bg="white").place(x=90, y=140)
txt_user = Entry(login_frame, font=("Times new roman", 15), bg="light grey")
txt_user.place(x=90, y=170, width=350, height=35)
pwd = Label(login_frame, text="Password", font="Arial 15", fg="grey", bg="white").place(x=90, y=210)
txt_pwd = Entry(login_frame, font=("Times new roman", 15), bg="light grey")
txt_pwd.place(x=90, y=240, width=350, height=35)
forget_btn = Button(login_frame, text="Forget Password?", bd=0, fg="#d77337", bg="white", font=("Times new roman", 12), command=forget_password).place(x=90, y=290)
login_bth = Button(root, text="Login", bg="#d77337", fg="white", font=("Times new roman", 20), command=login_data).place(x=450, y=570, width=140, height=40)


root.mainloop()
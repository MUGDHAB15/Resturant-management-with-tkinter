from tkinter import *
from PIL import Image, ImageTk

IMAGE_PATH = 'login.jpg'
WIDTH, HEIGHT = 900, 700

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
forget_btn = Button(login_frame, text="Forget Password?", bd=0, fg="#d77337", bg="white", font=("Times new roman", 12)).place(x=90, y=290)
login_bth = Button(root, text="Login", bg="#d77337", fg="white", font=("Times new roman", 20)).place(x=450, y=570, width=140, height=40)


root.mainloop()
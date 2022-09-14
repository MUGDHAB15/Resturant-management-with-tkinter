from fileinput import filename
from textwrap import fill
from tkinter import *
from PIL import Image, ImageTk
import pyodbc

root = Tk()
root.geometry("1000x783")
root.title("MB FOODS")

#adding title frame to have the name of thr restuarant to be displayed

title_frame = Frame(root, bg="orange", relief=SUNKEN, padx=2, pady=2)
title_frame.pack(side=TOP, fill="x")
title=Label(title_frame, text="MB FOODS", font="Helvetica 16 bold", bg="Orange", fg="black", padx=2, pady=2)
title.pack(side=TOP, fill="x")

# frame to have various buttons to operate on the GUI such as login, register, menu etc.
second_frame = Frame(root, bg="grey", relief=SUNKEN, padx=2, pady=2)
second_frame.pack(side=TOP, fill="x")
login=Button(second_frame, text="Login", bg="grey", fg="white", relief=SUNKEN, borderwidth=0, padx=2, pady=2)
login.pack(side=LEFT, fill="x")
register=Button(second_frame, text="Register", bg="grey", fg="white", relief=SUNKEN, borderwidth=0, padx=2, pady=2)
register.pack(side=LEFT, fill="x")
menu=Button(second_frame, text="Menu", bg="grey", fg="white", relief=SUNKEN, borderwidth=0, padx=2, pady=2)
menu.pack(side=LEFT, fill="x")
contact=Button(second_frame, text="Contact", bg="grey", fg="white", relief=SUNKEN, borderwidth=0, padx=2, pady=2)
contact.pack(side=LEFT, fill="x")
about=Button(second_frame, text="About Us", bg="grey", fg="white", relief=SUNKEN, borderwidth=0, padx=2, pady=2)
about.pack(side=LEFT, fill="x")

# frame to have the backgroung image to be displayed

third_frame=Frame(root, bg="grey", relief=SUNKEN, padx=2, pady=22)
third_frame.pack(side=TOP, fill="x")
image1 = Image.open("background.jpg")
photo1 = ImageTk.PhotoImage(image1)
background_label1=Label(third_frame, image=photo1, bg="grey")
background_label1.place(x=1, y=15, relwidth=1, relheight=1)

welcome_text = Label(third_frame, text="Welcome to MB FOOD \n ENJOY HOME COOKED FOOD OUTSIDE HOME", font="Halvetice 20 bold")
welcome_text.pack(pady=68)

#fourth frame 

fourth_frame = Frame(root, bg="orange", relief=RAISED, padx=2, pady=2)
fourth_frame.pack(side=TOP, fill="x", pady=22)
text_label = Label(fourth_frame, text="DINE IN OR TAKE AWAY", font="Arial 20 bold", fg="black", bg="orange")
text_label.pack(side=TOP, fill="x")
image2 = Image.open("biryani.jpg")
photo2 = ImageTk.PhotoImage(image2)
image_label2=Label(fourth_frame, image=photo2)
image_label2.pack(side=LEFT, padx=12, pady=7)
image3 = Image.open("panner.jpg")
photo3 = ImageTk.PhotoImage(image3)
image_label3=Label(fourth_frame, image=photo3)
image_label3.pack(side=LEFT, padx=12, pady=7)
image4 = Image.open("daal.jpg")
photo4 = ImageTk.PhotoImage(image4)
image_label4=Label(fourth_frame, image=photo4)
image_label4.pack(side=LEFT, padx=12, pady=7)
image5 = Image.open("samosa.jpg")
photo5 = ImageTk.PhotoImage(image5)
image_label5=Label(fourth_frame, image=photo5)
image_label5.pack(side=LEFT, padx=12, pady=7)

root.mainloop()

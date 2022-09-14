

from sre_parse import State
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import random
import time
from PIL import Image, ImageTk
from tkinter import messagebox
import requests
import pyodbc

# functions

# check button functions

def frenchfries():
    if var1.get() == 1:
        ff_entry.configure(State='normal')
        ff_entry.delete(0, END)
        ff_quantity.focus()
    elif var1.get() == 0:
        ff_entry.configure(State='disbaled')
        e_ff.set('0')

# save the bill to the database

def save():
   server = 'DESKTOP-G6HANB8'
   database = 'orders'
   # defining our connection string
   conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server}; \
                        Server=' + server + '; \
                        Database='+ database +'; \
                        Trusted_Connection=yes;'
                        )

   # create the connection cursor
   cursor = conn.cursor()
   cursor.execute('INSERT INTO order_db (Bill_number, Date, Frenchfries, Crispycorn, samosa, AlooTikki, MushroomTikka, PaneerTikka, PaneerButterMasala, MixedVegetable, DalFry, Naan, Chapati, Rice, Icecream, Lassi, Colddrink, Totalcost) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                                  (billnumber, date,
                                  int(e_ff.get()) * 15,
                                  int(e_cc.get()) * 25,
                                  int(e_samosa.get()) * 15,
                                  int(e_at.get()) * 15,
                                  int(e_mt.get()) * 15, 
                                  int(e_pt.get()) * 15,
                                  int(e_pb.get()) * 15,
                                  int(e_mv.get()) * 15,
                                  int(e_df.get()) * 15,
                                  int(e_n.get())* 15,
                                  int(e_c.get()) * 15,
                                  int(e_r.get()) * 15,
                                  int(e_l.get()) * 15,
                                  int(e_cd.get()) * 15,
                                  int(e_ic.get()) * 15,
                                  total + 50
                                  ))
   # commit the query
   conn.commit()
   conn.close()
   messagebox.showinfo("Success", "Bill data saved")
   #clear_data()
   #messagebox.showinfo("Success", "PAGE REFRESHED")             

# function to place an order and generate a bill

def bill():
    root4= Toplevel(root3)
    root4.title("Reciept")
    IMAGE_PATH = 'login.jpg'
    WIDTH, HEIGHT = 700, 500
    root4.geometry('{}x{}'.format(WIDTH, HEIGHT))

    canvas = Canvas(root4, width=WIDTH, height=HEIGHT)
    #canvas.resizable(False, False)
    canvas.pack()

    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)

    #TEXT AREA FOR RECEIPT

    txtBill_frame = Frame(root4, bg="white")
    txtBill_frame.place(x=230, y=70, height=380, width=430)

    # Button to the save the bill data to the database

    save_btn = Button(txtBill_frame, text='Save', cursor="hand2", font=('Comic Sans MS', 10, 'bold'), bg='Orange', fg='black', padx=10, pady=5, relief=SUNKEN, command=save).grid(row=3, column=0)

    textBill=Text(txtBill_frame,font=('arial',12,'bold'),bd=3,width=48,height=30)
    textBill.grid(row=15,column=0)
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0:
         textBill.delete(1.0, END)
         global billnumber, date, total
         x = random.randint(100, 10000)
         billnumber = 'Bill'+ str(x)
         date = time.strftime('%d/%m/%Y')
         textBill.insert(END, 'Receipt Ref:\t\t'+ billnumber +'\t\t'+ date+'\n')
         textBill.insert(END, '************************************************************************\n')
         textBill.insert(END, 'Items\t\t Quantity\t\t\t Cost \n')
         textBill.insert(END, '************************************************************************\n')
         if e_ff.get() != '0':
             textBill.insert(END, f"French Fries\t\t\t{int(e_ff.get())}\t\t{int(e_ff.get())*15}\n")
         if e_cc.get() != '0':
            textBill.insert(END, f"Crispy corn\t\t\t{int(e_cc.get())}\t\t{int(e_cc.get())*25}\n")
         if e_samosa.get() != '0':
            textBill.insert(END, f"Samosa\t\t\t{int(e_samosa.get())}\t\t{int(e_samosa.get())*15}\n")
         if e_at.get() != '0':
            textBill.insert(END, f"Aloo Tikki\t\t\t{int(e_at.get())}\t\t{int(e_at.get())*15}\n")
         if e_mt.get() != '0':
            textBill.insert(END, f"Mushrrom Tikka\t\t\t{int(e_mt.get())}\t\t{int(e_mt.get())*15}\n")
         if e_pt.get() != '0':
            textBill.insert(END, f"Paneer Tikka\t\t\t{int(e_pt.get())}\t\t{int(e_pt.get())*15}\n")
         if e_pb.get() != '0':
            textBill.insert(END, f"Paneer butter masala\t\t\t{int(e_pb.get())}\t\t{int(e_pb.get())*15}\n")
         if e_mv.get() != '0':
            textBill.insert(END, f"Mixed Vegetable\t\t\t{int(e_mv.get())}\t\t{int(e_mv.get())*15}")
         if e_df.get() != '0':
            textBill.insert(END, f"Dal Fry\t\t\t{int(e_df.get())}\t\t{int(e_df.get())*15}")
         if e_n.get() != '0':
            textBill.insert(END, f"Naan\t\t\t{int(e_n.get())}\t\t{int(e_n.get())*15}")
         if e_c.get() != '0':
           textBill.insert(END, f"Chapati\t\t\t{int(e_c.get())}\t\t{int(e_c.get())*15}")
         if e_r.get() != '0':
           textBill.insert(END, f"Rice\t\t\t{int(e_r.get())}\t\t{int(e_r.get())*15}")
         if e_l.get() != '0':
           textBill.insert(END, f"Lassi\t\t\t{int(e_l.get())}\t\t{int(e_l.get())*15}")
         if e_cd.get() != '0':
           textBill.insert(END, f"Cold Drink\t\t\t{int(e_cd.get())}\t\t{int(e_cd.get())*15}")
         if e_ic.get() != '0':
           textBill.insert(END, f"Ice cream\t\t\t{int(e_ic.get())}\t\t{int(e_ic.get())*15}")
    
         textBill.insert(END, '************************************************************************\n')
         total = ((int(e_ff.get())*15) + (int(e_cc.get())*25) + (int(e_samosa.get())*15) + (int(e_samosa.get())*15) + (int(e_at.get())*15) + (int(e_mt.get())*15) +(int(e_pt.get())*15) + (int(e_pb.get())*15) + (int(e_mv.get())*15) + (int(e_df.get())*15) + (int(e_n.get())*15) + (int(e_c.get())*15) + (int(e_r.get())*15) + (int(e_l.get())*15) + (int(e_cd.get())*15) + (int(e_ic.get())*15))
         textBill.insert(END, f"Subtotal\t\t\t {total}Rs\n\n")
         textBill.insert(END, f"Service Tax\t\t\t {50}Rs\n\n")
         textBill.insert(END, f"Total cost\t\t\t {total + 50}Rs\n\n")
         textBill.insert(END, '************************************************************************\n')
         textBill.insert(END, f'\t Thank You for your order\n')
    else:
        messagebox.showerror('Error', 'Please select something to order')

    
    root4.mainloop()



root3 = Tk()
root3.geometry('900x500')
root3.title("Menu")

# create a mainframe

main_frame = Frame(root3)
main_frame.pack(fill=BOTH, expand=1)

# Create a canvas
my_canvas = Canvas(main_frame, bg='grey')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Add another frame inside the canvas
another_frame = Frame(my_canvas, bg="grey")

# Add that frame to the window in the canvas
my_canvas.create_window((0,0), window=another_frame, anchor="nw")

#for x in range(200):
    #print("")

#adding title frame to have the name of the restuarant to be displayed
first_label = Label(another_frame, text="MB FOODS", font=('Comic Sans MS', 45, 'bold'), bg="grey", fg="Orange", padx=10, pady=0).grid(row=0, column=5, columnspan=10)

second_label = Label(another_frame, text="MENU", font=('Comic Sans MS', 20, 'bold'), bg="grey", fg="black", padx=10, pady=0).grid(row=3, column= 5)

order_btn = Button(another_frame, text='Order', font=('Comic Sans MS', 16, 'bold'), bg='Orange', fg='black', padx=0, pady=0, relief=SUNKEN, command=bill).grid(row=3, column=10)

# Variables

# checkbutton variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()

# entryfield variables

e_ff = StringVar()
e_cc = StringVar()
e_samosa = StringVar()
e_at = StringVar()
e_mt = StringVar()
e_pt = StringVar()
e_pb = StringVar()
e_mv = StringVar()
e_df = StringVar()
e_n = StringVar()
e_c = StringVar()
e_r = StringVar()
e_l = StringVar()
e_cd = StringVar()
e_ic = StringVar()

# setting all the entry variables to zero

e_ff.set('0')
e_cc.set('0')
e_samosa.set('0')
e_at.set('0')
e_mt.set('0')
e_pt.set('0')
e_pb.set('0')
e_mv.set('0')
e_df.set('0')
e_n.set('0')
e_c.set('0')
e_r.set('0')
e_l.set('0')
e_cd.set('0')
e_ic.set('0')


#Starters
third_label = Label(another_frame, text="Starters", font=('Comic Sans MS', 16), bg="grey", fg="orange", padx=0, pady=0).grid(row=5, column=0)


# French fries + cost + Quantity entry box


french_fries = Checkbutton(another_frame, text = "French Fries", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var1, command=frenchfries).grid(row=8, column=0)

french_fries_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=8, column=2, columnspan=4)

french_fries_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=8,column=10, columnspan=13)

ff_quantity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=8, column=25)

ff_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5,bg='white', textvariable=e_ff).grid(row=8, column=35)


# Crispy corn + cost + quantity


crispy_corn = Checkbutton(another_frame, text = "Crispy Corn", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var2).grid(row=10, column=0)

crispy_corn_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=10, column=2, columnspan=4)

crispy_corn_cost = Label(another_frame, text = "£25", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=10,column=10, columnspan=13)

cc_quantity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=10, column=25)

cc_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5,bg='white', textvariable=e_cc).grid(row=10, column=35)


# Samosa + cost + quantity
samosa = Checkbutton(another_frame, text = "Samosa", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var3).grid(row=12, column=0)

samosa_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=12, column=2, columnspan=4)

samosa_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=12,column=10, columnspan=13)

samosa_quantity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=12, column=25)

samosa_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_samosa).grid(row=12, column=35, columnspan=50)


# Aloo tikki + cost +quantity

aloo_tikki = Checkbutton(another_frame, text = "Aloo tikki", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var4).grid(row=14, column=0)

aloo_tikki_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=14, column=2, columnspan=4)

aloo_tikki_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=14,column=10, columnspan=13)

alootikki_quantity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=14, column=25)

alootikki_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_at).grid(row=14, column=35, columnspan=50)


# Mushroom tikka + cost + quantity
mushroom_tikka = Checkbutton(another_frame, text = "Mushroom tikka", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var5).grid(row=16, column=0)

mushroom_tikka_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=16, column=2, columnspan=4)

mushroom_tikka_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=16,column=10, columnspan=13)

mush_t_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=16, column=25)

mush_t_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_mt).grid(row=16, column=35)

#Paneer Tikka + cost +quantity

Paneer_tikka = Checkbutton(another_frame, text = "Paneer tikka", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var6).grid(row=18, column=0)

paneer_tikka_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=18, column=2, columnspan=4)

panner_tikka_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=18,column=10, columnspan=13)

panner_t_quantity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=18, column=25)

paneer_t_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_pt).grid(row=18, column=35)


#Main course 
tenth_label = Label(another_frame, text="Main Course", font=('Comic Sans MS', 20, 'bold'), bg="grey", fg="orange", padx=0, pady=15).grid(row=19, column=0)

#Paneer Butter masala + cost +quantity

paneer_bmasal = Checkbutton(another_frame, text = "Paneer Butter Masala", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var7).grid(row=20, column=0)

paneer_bmasala_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=20, column=2, columnspan=4)

panner_bmasala_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=20,column=10, columnspan=13)

p_b_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=20, column=25)

p_b_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_pb).grid(row=20, column=35)


#Mixed Vegetable + cost+quantity

m_veg = Checkbutton(another_frame, text = "Mixed Vegetable", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var8).grid(row=21, column=0)

mixedveg_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=21, column=2, columnspan=4)

mixedveg_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=21,column=10, columnspan=13)

m_veg_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=21, column=25)

m_veg_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_mv).grid(row=21, column=35)


#Dal Fry + cost +quantity

dal_fry = Checkbutton(another_frame, text = "Dal Fry", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var9).grid(row=22, column=0)

dalfry_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=22, column=2, columnspan=4)

dalfry_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=22,column=10, columnspan=13)

d_f_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=22, column=25)

d_f_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_df).grid(row=22, column=35)

#Naan + cost + quantity

naan = Checkbutton(another_frame, text = "Naan", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var10).grid(row=23, column=0)

naan_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=23, column=2, columnspan=4)

naan_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=23,column=10, columnspan=13)

naan_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=23, column=25)

naan_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_n).grid(row=23, column=35)

# Chapati + cost + quantity

chapati = Checkbutton(another_frame, text = "Chapati", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var11).grid(row=24, column=0)

chapati_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=24, column=2, columnspan=4)

chapati_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=24,column=10, columnspan=13)

chapati_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=24, column=25)

chapati_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_c).grid(row=24, column=35)

#Rice + cost + quantity

rice = Checkbutton(another_frame, text = "Rice", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var12).grid(row=25, column=0)

rice_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=25, column=2, columnspan=4)

rice_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=25,column=10, columnspan=13)

rice_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=25, column=25)

rice_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_r).grid(row=25, column=35)

#Desert and Beverages
seventeenth_label = Label(another_frame, text="Desert", font=('Comic Sans MS', 20, 'bold'), bg="grey", fg="orange", padx=0, pady=15).grid(row=26, column=0)

#Ice cream + Cost + Quantity

icecream = Checkbutton(another_frame, text = "Ice cream", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var13).grid(row=27, column=0)

iceceream_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=27, column=2, columnspan=4)

icecream_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=27,column=10, columnspan=13)

icecream_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=27, column=25)

icecream_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_ic).grid(row=27, column=35)

# Lassi +cost + quantity

lassi = Checkbutton(another_frame, text = "Lassi", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var14).grid(row=28, column=0)

lassi_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=28, column=2, columnspan=4)

lassi_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=28,column=10, columnspan=13)

lassi_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=28, column=25)

lassi_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_l).grid(row=28, column=35)

# cold drink + cost + quantity

cold_drink = Checkbutton(another_frame, text = "Cold drink", font=('Cambria', 16),bg='grey', onvalue=1, offvalue=0, variable=var15).grid(row=29, column=0)

cold_drink_spacing = Label(another_frame, text = "---------------------------------------------------------------------------------------", bg="grey", fg="black", padx= 15, pady= 5).grid(row=29, column=2, columnspan=4)

cold_drink_cost = Label(another_frame, text = "£15", font=('Cambria', 16), bg='grey', fg='black', padx=0, pady=0).grid(row=29,column=10, columnspan=13)

cd_quanity = Label(another_frame, text="Qty",font=('Cambria', 12, BOLD), bg='grey', fg='black').grid(row=29, column=25)

cd_entry = Entry(another_frame, font=('times new roman', 10), fg='grey', width=5, bg='white', textvariable=e_cd).grid(row=29, column=35)



root3.mainloop()
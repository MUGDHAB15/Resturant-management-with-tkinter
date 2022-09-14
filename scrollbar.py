






from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1300x900")

# create a mainframe

main_frame = Frame(root)
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
another_frame = Frame(my_canvas)

# Add that frame to the window in the canvas
my_canvas.create_window((0,0), window=another_frame, anchor="nw")

#adding title frame to have the name of the restuarant to be displayed

first_frame = Frame(another_frame, bg="orange", relief=SUNKEN, padx=0, pady=0)
first_frame.pack(side=TOP, fill="x")
first=Label(first_frame, text="MB FOODS", font="Helvetica 16 bold", bg="Orange", fg="black", padx=700, pady=2)
first.pack(side=TOP, fill="x")

# adding second frame for the menu

#second_frame = Frame(another_frame, bg='white', relief=SUNKEN, padx=2, pady=2)
#second_frame.pack(side = LEFT, fill=X)
second = Label(another_frame, text="Menu", font=('Comic Sans MS', 45, 'bold'), bg="grey", fg="black", padx=2, pady=2)
first.pack(side=LEFT, fill=X)




root.mainloop()
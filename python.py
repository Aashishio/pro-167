from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Drawing shapes on Canvas")
root.geometry("1500x720")

canvas = Canvas(root, width=1450, height=600, highlightbackground="grey", bg="white")
canvas.pack()

lbl__startx = Label(root, text="Start x = ")
lbl__startx.place(relx=0.05, rely=0.9, anchor=CENTER)
ent__startx = Entry(root)
ent__startx.place(relx=0.111, rely=0.9, anchor=CENTER)

lbl__starty = Label(root, text="Start y = ")
lbl__starty.place(relx=0.2, rely=0.9, anchor=CENTER)
ent__starty = Entry(root)
ent__starty.place(relx=0.261, rely=0.9, anchor=CENTER)

lbl__endx = Label(root, text="End x = ")
lbl__endx.place(relx=0.35, rely=0.9, anchor=CENTER)
ent__endx = Entry(root)
ent__endx.place(relx=0.41, rely=0.9, anchor=CENTER)

lbl__endy = Label(root, text="End y = ")
lbl__endy.place(relx=0.5, rely=0.9, anchor=CENTER)
ent__endy = Entry(root)
ent__endy.place(relx=0.56, rely=0.9, anchor=CENTER)

lbl__shape = Label(root, text="Shape : ")
lbl__shape.place(relx=0.65, rely=0.9, anchor=CENTER)
shape = ["Circle", "Rectangle"]
input__valShape = StringVar()
drop__shape = ttk.Combobox(root, values=shape, textvariable=input__valShape)
drop__shape.place(relx=0.72, rely=0.9, anchor=CENTER)

lbl__color = Label(root, text="Colour : ")
lbl__color.place(relx=0.81, rely=0.9, anchor=CENTER)
color = ["White",	"Black","Orange",	"Maroon", "Red","Yellow",	"Lime green",	"Salmon","Green",	"Sky blue",	"Crimson",	"Aqua","Grey",	"Purple",	"Mustard",	"Peach","Violet",	"Magenta",	"Coral",	"Saffron","Brown",	"Pink",	"Tan",	"Teal","Navy Blue",	"Turquoise",	"Lavender",	"Beige","Lemon yellow",	"Grape vine",	"Indigo",	"Fuchsia","Amber",	"Sea green",	"Dark green",	"Burgundy","Charcoal",	"Bronze",	"Cream", "Mauve","Olive",	"Cyan",	"Silver",	"Rust", "Ruby",	"Azure",	"Mint",	"Pearl","Ivory",	"Tangerine",	"Cherry red",	"Garnet","Emerald",	"Sapphire",	"Rosewood",	"Lilac","Arctic blue",	"Pista green",	"Coffee brown",	"Umber","Brunette",	"Mocha",	"Ash",	"Jet black"]
input__colorVal = StringVar()
drop__shape = ttk.Combobox(root, values=color, textvariable=input__colorVal)
drop__shape.place(relx=0.89, rely=0.9, anchor=CENTER)

lbl__width = Label(root, text="Width :")
lbl__width.place(relx=0.65, rely=0.95, anchor=CENTER)
ent__width = Entry(root)
ent__width.place(relx=0.71, rely=0.95, anchor=CENTER)

def create():
    startx = ent__startx.get()
    starty = ent__starty.get()
    endx = ent__endx.get()
    endy = ent__endy.get()
    width1 = ent__width.get()
    colour = input__colorVal
    shapes = input__valShape

    if input__valShape == "rectangle":
        rectangle = canvas.create_rectangle(endx, endy, startx, starty, width = width1, fill = colour)
    if input__valShape == "circle":
        rectangle = canvas.create_oval(endx, endy, startx, starty, width = width1, fill = colour)

btn__create = Button(root, text="Create", command=create)
btn__create.place(relx=0.5, rely=0.95, anchor=CENTER) 
root.mainloop()
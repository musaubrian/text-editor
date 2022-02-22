from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Simple text editor 💻")

text = Text(root)
text.grid(column=1, row=1, rowspan=3 )

def SaveAs():
    global text
    t = text.get("1.0", "end-1c")
    saveLocation = filedialog.asksaveasfilename()
    file = open(saveLocation, "w+")
    file.write(t)
    file.close()


button = Button(root, text="Save", font="arial 18", command=SaveAs)
button.grid()

# choose fonts
def FontHelvetica():
    global text
    text.config(font="Helvitica 16")

def FontCourier():
    global text
    text.config(font="Courier 16")

def FontArial():
    global text
    text.config(font="arial 16")
    


font = Menubutton(root, text="Font", font="arial 20")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

helvetica = IntVar()
courier = IntVar()
arial = IntVar()

font.menu.add_checkbutton(
    label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(
    label="Helvetica", variable=helvetica, command=FontHelvetica)
font.menu.add_checkbutton(label="Arial", variable=arial, command=FontArial)

root.mainloop()
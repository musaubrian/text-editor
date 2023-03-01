from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Editr")

text = Text(root)
text.grid(column=1, row=1, rowspan=3, columnspan=2)
text.configure(font="arial 15")


def SaveAs():
    global text
    t = text.get("1.0", "end-1c")
    saveLocation = filedialog.asksaveasfilename()
    file = open(saveLocation, "w")
    file.write(t)
    file.close()


save_button = Button(root, text="Save", font="arial 20", command=SaveAs)
save_button.grid(column=1, row=4)
quit_button = Button(root, text="Quit", font="arial 20", command=quit)
quit_button.grid(column=2, row=4)
quit_button.configure(foreground="red")


root.mainloop()

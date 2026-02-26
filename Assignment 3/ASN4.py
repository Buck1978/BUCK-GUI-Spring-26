from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class MyGUI:
    def __init__(self):
        # Main window
        self.root = Tk()
        self.root.title("Assignment 4 - tkinter GUI")

        # -----------------------------
        # Frames
        # -----------------------------
        self.img_frame = Frame(self.root)
        self.img_frame.pack(pady=10)

        self.radio_frame = Frame(self.root)
        self.radio_frame.pack(pady=10)

        # -----------------------------
        # Load Images
        # -----------------------------
        # Make sure these image files are in the same folder as ASN4.py
        self.imgChicken = ImageTk.PhotoImage(Image.open("chicken.png"))
        self.imgPie = ImageTk.PhotoImage(Image.open("pie.png"))
        self.imgPizza = ImageTk.PhotoImage(Image.open("pizza.png"))
        self.imgSalad = ImageTk.PhotoImage(Image.open("salad.png"))

        # -----------------------------
        # Label for displaying images
        # (initially empty)
        # -----------------------------
        self.lbl = Label(self.img_frame)
        self.lbl.pack()

        # -----------------------------
        # IntVar for Radiobuttons
        # -----------------------------
        self.var = IntVar()
        self.var.set(0)   # nothing selected initially

        # -----------------------------
        # Radiobuttons
        # -----------------------------
        rb_chicken = Radiobutton(self.radio_frame,
                                 text="Chicken",
                                 variable=self.var,
                                 value=1,
                                 command=self.on_radio_select)
        rb_chicken.pack(anchor="w")

        rb_pie = Radiobutton(self.radio_frame,
                             text="Pie",
                             variable=self.var,
                            	value=2,
                             command=self.on_radio_select)
        rb_pie.pack(anchor="w")

        rb_pizza = Radiobutton(self.radio_frame,
                               text="Pizza",
                               variable=self.var,
                               value=3,
                               command=self.on_radio_select)
        rb_pizza.pack(anchor="w")

        rb_salad = Radiobutton(self.radio_frame,
                               text="Salad",
                               variable=self.var,
                               value=4,
                               command=self.on_radio_select)
        rb_salad.pack(anchor="w")

        self.root.mainloop()

    # -----------------------------
    # Method called when user clicks a Radiobutton
    # -----------------------------
    def on_radio_select(self):
        choice = self.var.get()

        # Debug message (remove when finished)
        # messagebox.showinfo("Debug", f"You selected: {choice}")

        if choice == 1:
            self.lbl.config(image=self.imgChicken)
        elif choice == 2:
            self.lbl.config(image=self.imgPie)
        elif choice == 3:
            self.lbl.config(image=self.imgPizza)
        elif choice == 4:
            self.lbl.config(image=self.imgSalad)


def main():
    MyGUI()


if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class MyGUI:
    def __init__(self):

        # Main window
        
        self.root = Tk()
        self.root.title("Food Viewer")
        self.root.geometry("500x500")

        # Frames
        
        self.img_frame = Frame(self.root)
        self.img_frame.pack(pady=10)

        self.rbdBtn_frame = Frame(self.root)
        self.rbdBtn_frame.pack(pady=10)

        # Load Images (JPG per table)
        
        self.imgOne = ImageTk.PhotoImage(Image.open("chicken.jpg").resize((400, 300)))
        self.imgTwo = ImageTk.PhotoImage(Image.open("pie.jpg").resize((400, 300)))
        self.imgThree = ImageTk.PhotoImage(Image.open("pizza.jpg").resize((350, 300)))
        self.imgFour = ImageTk.PhotoImage(Image.open("steak.jpg").resize((300, 300)))

        # Label for displaying images
        
        self.lbl = Label(self.img_frame)
        self.lbl.pack()

        # IntVar for Radiobuttons
        
        self.var = IntVar()
        self.var.set(1)   # per planning table

        # Radiobuttons (left aligned)
        
        self.radio_a = Radiobutton(self.rbdBtn_frame,
                                   text="Chicken",
                                   variable=self.var,
                                   value=1,
                                   command=self.on_radio_select)
        self.radio_a.pack(side="left", padx=10)

        self.radio_b = Radiobutton(self.rbdBtn_frame,
                                   text="Pie",
                                   variable=self.var,
                                   value=2,
                                   command=self.on_radio_select)
        self.radio_b.pack(side="left", padx=10)

        self.radio_c = Radiobutton(self.rbdBtn_frame,
                                   text="Pizza",
                                   variable=self.var,
                                   value=3,
                                   command=self.on_radio_select)
        self.radio_c.pack(side="left", padx=10)

        self.radio_d = Radiobutton(self.rbdBtn_frame,
                                   text="Steak",
                                   variable=self.var,
                                   value=4,
                                   command=self.on_radio_select)
        self.radio_d.pack(side="left", padx=10)

        # Display initial image 

        self.lbl.config(image=self.imgOne)

        self.root.mainloop()

    # Method called when user clicks a Radiobutton
    
    def on_radio_select(self):
        choice = self.var.get()

        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)


def main():
    MyGUI()


if __name__ == "__main__":
    main()

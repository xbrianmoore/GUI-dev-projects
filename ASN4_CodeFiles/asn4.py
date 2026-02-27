# Brian Moore

import tkinter
from PIL import Image, ImageTk

class FoodViewerGUI:
    def __init__(self):
        # Create the main window
        self.root = tkinter.Tk()
        self.root.title("Food Viewer")
        self.root.minsize(400, 300)
        
        # Create two frames
        self.img_frame = tkinter.Frame(self.root)
        self.rbdBtn_frame = tkinter.Frame(self.root)
        
        # Load and resize images
        self.img1 = Image.open("chicken.jpg")
        self.img1 = self.img1.resize((400, 300))
        self.imgOne = ImageTk.PhotoImage(self.img1)
        
        self.img2 = Image.open("pie.jpg")
        self.img2 = self.img2.resize((400, 300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)
        
        self.img3 = Image.open("pizza.jpg")
        self.img3 = self.img3.resize((350, 300))
        self.imgThree = ImageTk.PhotoImage(self.img3)
        
        self.img4 = Image.open("steak.jpg")
        self.img4 = self.img4.resize((300, 300))
        self.imgFour = ImageTk.PhotoImage(self.img4)
        
        # Create a label in the img_frame to display images
        self.lbl = tkinter.Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()
        
        # Create IntVar to track radiobutton selection (initialized to 1 for Chicken)
        self.var = tkinter.IntVar(value=1)
        
        # Create the 4 radiobuttons in the rbdBtn_frame
        self.radio_a = tkinter.Radiobutton(self.rbdBtn_frame, 
                                           text="Chicken", 
                                           value=1, 
                                           variable=self.var,
                                           command=self.on_radio_select)
        self.radio_a.pack(side="left", padx=10)
        
        self.radio_b = tkinter.Radiobutton(self.rbdBtn_frame, 
                                           text="Pie", 
                                           value=2, 
                                           variable=self.var,
                                           command=self.on_radio_select)
        self.radio_b.pack(side="left", padx=10)
        
        self.radio_c = tkinter.Radiobutton(self.rbdBtn_frame, 
                                           text="Pizza", 
                                           value=3, 
                                           variable=self.var,
                                           command=self.on_radio_select)
        self.radio_c.pack(side="left", padx=10)
        
        self.radio_d = tkinter.Radiobutton(self.rbdBtn_frame, 
                                           text="Steak", 
                                           value=4, 
                                           variable=self.var,
                                           command=self.on_radio_select)
        self.radio_d.pack(side="left", padx=10)
        
        self.img_frame.pack()
        self.rbdBtn_frame.pack()
        
        # main loop
        tkinter.mainloop()
    
    # on_radio_select method
    def on_radio_select(self):
        # Get the current user choice
        choice = self.var.get()
        
        # Display the appropriate image based on user choice
        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)

# Create an instance of FoodViewerGUI
if __name__ == '__main__':
    food_viewer = FoodViewerGUI()

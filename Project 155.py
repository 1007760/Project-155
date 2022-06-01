from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.title("Project 155")
root.configure(background = 'red')
dictionary = {"Colors": ["CadetBlue1", "IndianRed2", "SlateGray1", "dark orchid", "cornflower blue", "VioletRed3"]}

def background() :
    background = random.randint(0,5)
    print(dictionary["Colors"][background])
    root.configure(background = dictionary["Colors"][background])

btn = Button(root, text = "Click me.", command = background)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()
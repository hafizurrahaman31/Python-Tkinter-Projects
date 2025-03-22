from tkinter import *
from PIL import Image, ImageTk
import os
def rotate_img():
    global counter
    image_label.config(image = img_array[counter % len(img_array)])
    counter += 1
    
counter = 1
root = Tk()

root.title("Image Viewer")
root.geometry("250x400")
root.configure(bg="black")

# Load the image
files = os.listdir("walpapers")

img_array = []

for file in files:
    img = Image.open(os.path.join("walpapers", file))
    resized_img = img.resize((200,200))
    img_array.append(ImageTk.PhotoImage(resized_img))

image_label = Label(root, image = img_array[0])
image_label.pack(pady=(15,10))

next_btn = Button(root, text="Next", bg="white", fg="black" , width = 24, height = 2, command = rotate_img)
next_btn.pack()




root.mainloop()

import numbers
import tkinter as tk
import glob
import os
from PIL import Image, ImageTk


# Init tk
root = tk.Tk()
root.geometry("906x687+100+100")
root.title("圖片查看器")

# Get the photos
photos = glob.glob(r"D:\User_Andongni\Desktop\python\Project\Tkinter\Read Photo\Photo\*.png")
photos = [ImageTk.PhotoImage(Image.open(photo)) for photo in photos]

# Show the first photo
current_photo_no = 0
photo_label = tk.Label(root, image=photos[current_photo_no], width=900, height=600)
photo_label.pack()

# Number Bar
number_var = tk.StringVar()
number_var.set("1 of 4")
tk.Label(root, textvariable=number_var, bd=1, relief=tk.SUNKEN, anchor=tk.CENTER).pack(fill=tk.X)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack()
prev_photo = tk.Button(root, text="上一頁")
next_photo = tk.Button(root, text="下一頁")
prev_photo.pack(side=tk.LEFT, anchor=tk.CENTER)
next_photo.pack(side=tk.RIGHT, anchor=tk.CENTER)

# Button Logic
def change_photos(next_no):
    global current_photo_no

    current_photo_no += next_no  
    
    # If No Out of index
    if current_photo_no >= len(photos): 
        current_photo_no = 0
    if current_photo_no < 0:
        current_photo_no = len(photos) - 1

    # Set the UI
    number_var.set(f"{current_photo_no + 1} of {len(photos)}")     
    photo_label.configure(image=photos[current_photo_no])

prev_photo.config(command=lambda: change_photos(-1))
next_photo.config(command=lambda: change_photos(1))

root.mainloop()
import tkinter as tk
from tkinter import messagebox
from random import random

# Init Tkinter
root = tk.Tk()
root.geometry("500x300+100+100")
root.title("辭職信")

### Frame1 ###
frame1 = tk.Frame(root)
frame1.pack()

# Text
tk.Label(frame1, text="尊敬的各位領導: ", font=24, padx=30, pady=30).pack(side=tk.LEFT, anchor=tk.N)
# Img
img = tk.PhotoImage(file=r"D:\User_Andongni\Desktop\python\Project\Tkinter\Resign\Data\Resign.png")
label_img = tk.Label(frame1, image=img, padx=30, pady=30, bd=0).pack(side=tk.LEFT, anchor=tk.N)
# Text
tk.Label(frame1, text="辭職人: 安東尼", height=25, font=24, padx=30, pady=30, anchor=tk.S).pack(side=tk.LEFT)
# Yes No Button
yes_img = tk.PhotoImage(file=r"D:\User_Andongni\Desktop\python\Project\Tkinter\Resign\Data\yes.png")
yes_btn = tk.Button(frame1, image=yes_img, bd=0)
yes_btn.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

no_img = tk.PhotoImage(file=r"D:\User_Andongni\Desktop\python\Project\Tkinter\Resign\Data\no.png")
no_btn = tk.Button(frame1, image=no_img, bd=0)
no_btn.place(relx=0.7, rely=0.8, anchor=tk.CENTER)


### Frame2 ###
frame2 = tk.Frame(root)
# Text
tk.Label(frame2, 
        text="老闆大人，臣告退了\n這一退，可能就是一輩子了\n! ! ｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡ ! !",
        font=("黑體", 18),
        justify=tk.LEFT,
        height=300,
        fg="red",
        padx=50
        ).pack()
# Button
tk.Button(frame2, text="退出", command=root.quit).place(relx=0.9, rely=0.8)

### LOGIC ###
# On Exit
def on_exit():
    messagebox.showwarning(title="提示", message="此路不通")
root.protocol("WM_DELETE_WINDOW", on_exit)

# No Button Click
def move(event):
    no_btn.place(relx=random(), rely=random(), anchor=tk.CENTER)

no_btn.bind("<Enter>", move)

# Yes Button Click
def sure():
    frame1.pack_forget()
    frame2.pack()

yes_btn.config(command=sure)


root.mainloop()
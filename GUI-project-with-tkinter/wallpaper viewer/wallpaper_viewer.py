from tkinter import *
from PIL import Image, ImageTk
import os

def next_img():
    global counter
    img_label.config(image=img_array[counter])
    counter+=1
    if counter==len(img_array):
        counter=0

def prev_img():
    global counter
    img_label.config(image=img_array[counter])
    counter-=1
    if counter==-1:
        counter=len(img_array)-1

counter=1
root=Tk()

root.title("Wallpaper Viewer")
root.geometry("500x500")
root.configure(bg='black')

wall_label = Label(root, text="Wallpaper Viewer", bg='black', fg='white', font=('Arial', 24))
wall_label.pack()


files=os.listdir('wallpaper')
print(files)

img_array=[]
for file in files:
    img=Image.open(os.path.join('wallpaper', file))
    img=img.resize((200, 200))
    img_array.append(ImageTk.PhotoImage(img))


print(len(img_array))

img_label=Label(root,image=img_array[0])
img_label.pack(pady=20)

next_btn=Button(root,text="next",bg='white',fg='black',width=25,height=2,command=next_img)
next_btn.pack()

prev_btn=Button(root,text='Previous',bg='white',fg='black',width=25,height=2,command=prev_img)
prev_btn.pack(pady=10)

root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

email="anjalikhot5268@gmail.com"
password="1234"

def handle_login():
    e=email_input.get()
    p=password_input.get()
    if e==email and p==password:
        print("Login Success")
        messagebox.showinfo("Login Status","Login Success")

    else:
        print("Login Failed")
        messagebox.showerror("Login Status","Login Failed")

root=Tk()

root.title("Login Form")
root.iconbitmap('favicon.ico')
# root.minsize(500,500)


root.geometry("350x500")

root.config(bg="#0096DC")
img=Image.open("flipkart.png")
resize_img=img.resize((70,70))
img=ImageTk.PhotoImage(resize_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))


text_label=Label(root,text="Flipkart",fg="white",bg="#0096DC")
text_label.pack()
text_label.config(font=('verdana',24))

email_label=Label(root,text="Email",fg="white",bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input=Entry(root,width=30)
email_input.pack(ipady=4,pady=(1,15))

password_label=Label(root,text="Password",fg="white",bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input=Entry(root,width=30,show="*")
password_input.pack(ipady=4,pady=(1,15))

login_btn=Button(root,text="Login",bg="white",fg="black",width=15,activebackground="#007ACC",activeforeground="white",command=handle_login)
login_btn.pack(pady=(20,10))
login_btn.config(font=('verdana',10))





root.mainloop()


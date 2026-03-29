import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen 
from PIL import ImageTk,Image

class NewsApp:
    def __init__(self):
        # fetch data
        self.data=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=22dae05a3ce542429b43a7e164e285b0").json()
        print(self.data)

        # initial GUI load
        self.load_gui()
        
        self.load_news_item(0)

    def load_gui(self):
        self.root=Tk()
        self.root.title("News Application")
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.configure(bg="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        self.clear()

        try:
    # Try getting the URL from your data; fallback to Reddit URL if it's None/Missing
            img_url = self.data["articles"][index].get("urlToImage") or "https://www.reddit.com..."
    
            with urlopen(img_url) as response:
                raw_data = response.read()
        
        except Exception as e:
    # If the URL is broken or there is a network error, use a local default image
    # This is much faster and more reliable than a second download attempt
            img = Image.open("img_cant.jpg") # Make sure this file exists in your folder
            print(f"Error loading image: {e}")
        else:
            # If the download succeeded, create the image from raw_data
            img = Image.open(io.BytesIO(raw_data))

        # Common processing for both paths
        img = img.resize((350, 250), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        label = Label(self.root, image=photo)
        label.image = photo 
        label.pack()


        self.heading=Label(self.root,text=self.data["articles"][index]["title"],bg="black",fg="white",wraplength=350,justify="center")
        self.heading.pack(pady=(10,20))
        self.heading.config(font=("verdana",15))

        self.details=Label(self.root,text=self.data["articles"][index]["description"],bg="black",fg="white",wraplength=350,justify="center")
        self.details.pack(pady=(2,20))
        self.details.config(font=("verdana",12))

        self.frame=Frame(self.root,bg="black")
        self.frame.pack(expand=True,fill=BOTH)

        if index!=0:
            self.prev=Button(self.frame,text="Prev",width=16,height=3,command=lambda:self.load_news_item((index-1)))
            self.prev.pack(side=LEFT)

        self.read=Button(self.frame,text="Read More",width=16,height=3,command=lambda:self.open_link(self.data["articles"][index]["url"]))
        self.read.pack(side=LEFT)
        if index!=len(self.data["articles"])-1:
            self.next=Button(self.frame,text="Next",width=16,height=3,command=lambda:self.load_news_item((index+1)))
            self.next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)



a=NewsApp()
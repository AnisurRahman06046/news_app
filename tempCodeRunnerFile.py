import requests
from tkinter import Tk, Label,Button, Frame, BOTH, LEFT,RIGHT
from PIL import Image,ImageTk
from urllib.request import urlopen,Request
import io 
import webbrowser
class NewsApp:
    def __init__(self):
        # fetch data
        # self.data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9ddf978a1d1144b198c4913cf8f92731").json()
        self.data = requests.get("https://newsdata.io/api/1/latest?country=bd&apikey=pub_511242bc4a4b82b34f0192f0d27534c645d43").json()
        
        # print(self.data)
        
        # initial GUI load
        self.load_gui()
        
        # load the first news item
        self.load_news_item(0)
        
    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.title("News App")
        self.root.resizable(0, 0)
        self.root.configure(background='black')
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
    def load_news_item(self, index):
        # clear the screen
        self.clear()
        

        img_url = self.data['results'][index]['image_url']
        
        # Adding User-Agent header to the request
        req = Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        raw_image_data = urlopen(req).read()
        
        image = Image.open(io.BytesIO(raw_image_data))
        resized_img = image.resize((350, 250))
        photo = ImageTk.PhotoImage(resized_img)
        
        img_label = Label(self.root, image=photo)
        img_label.image = photo  # Keep a reference to the image to prevent garbage collection
        img_label.pack()

        # heading
        heading = Label(
            self.root,
            text=self.data['results'][index]['title'],
            bg='black',
            fg='white',
            wraplength=350,
            justify='center'
        )
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))
        # self.root.mainloop()
        
        # details
        details = Label(
            self.root,
            text=self.data['results'][index]['description'],
            bg='black',
            fg='white',
            wraplength=350,
            justify='center'
        )
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))
        
        # frame for button
        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)
        
        if index!=0:
            
            prevBtn = Button(frame,text='Prev',width=10,height=1,command=lambda:self.load_news_item(index-1))
            prevBtn.pack(side=LEFT)
        

        
        if index!=len(self.data['results'])-1:
            nextBtn = Button(frame,text='Next',width=10,height=1,command=lambda:self.load_news_item(index+1))
            nextBtn.pack(side=RIGHT)
        

        
        readBtn = Button(frame,text='Read More',width=10,height=1,command=lambda:self.open_link(self.data['results'][index]['link']))
        readBtn.place(relx=0.5, rely=0.5, anchor='center')
        
        
    
    
        self.root.mainloop()
        
    def open_link(self,url):
        webbrowser.open(url)

# Create an instance of the NewsApp
obj = NewsApp()




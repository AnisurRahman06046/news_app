import requests
from tkinter import Tk, Label, Button, Frame, BOTH, LEFT, RIGHT, BOTTOM
from PIL import Image, ImageTk
from urllib.request import urlopen, Request
import io 
import webbrowser

class NewsApp:
    def __init__(self):
        # fetch data
        self.data = requests.get("https://newsdata.io/api/1/latest?country=bd&apikey=pub_511242bc4a4b82b34f0192f0d27534c645d43").json()
        
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
        
        # Create a frame for the buttons at the bottom
        self.button_frame = Frame(self.root, bg='black')
        self.button_frame.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)
        
    def clear(self):
        for widget in self.root.pack_slaves():
            if widget != self.button_frame:
                widget.destroy()
    
    def load_news_item(self, index):
        # clear the screen except the button frame
        self.clear()

        img_url = self.data['results'][index].get('image_url')

        if img_url:
            # Adding User-Agent header to the request
            req = Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            raw_image_data = urlopen(req).read()
            
            image = Image.open(io.BytesIO(raw_image_data))
            resized_img = image.resize((350, 250))
            photo = ImageTk.PhotoImage(resized_img)
            
            img_label = Label(self.root, image=photo)
            img_label.image = photo  # Keep a reference to the image to prevent garbage collection
            img_label.pack()
        else:
            # Display a placeholder if no image URL is available
            img_label = Label(self.root, text="No Image Available", bg='black', fg='white', width=350, height=10)
            img_label.pack()

        # heading
        heading = Label(
            self.root,
            text=self.data['results'][index]['title'],
            bg='black',
            fg='white',
            wraplength=330,
            justify='center',
            anchor='center',
            padx=10,
            pady=5
        )
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15, 'bold'))
        
        # details
        details = Label(
            self.root,
            text=self.data['results'][index]['description'],
            bg='black',
            fg='white',
            wraplength=330,
            justify='left',
            anchor='w',
            padx=15,
            pady=10
        )
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))
        
        # Clear the button frame before adding buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        # Show "Prev" button only if index is greater than 0
        if index > 0:
            prevBtn = Button(self.button_frame, text='Prev', width=10, height=1, command=lambda: self.load_news_item(index-1))
            prevBtn.pack(side=LEFT, padx=10)

        # Show "Next" button only if index is less than the last news item
        if index < len(self.data['results']) - 1:
            nextBtn = Button(self.button_frame, text='Next', width=10, height=1, command=lambda: self.load_news_item(index+1))
            nextBtn.pack(side=RIGHT, padx=10)

        # "Read More" button to open the full news article
        readBtn = Button(self.button_frame, text='Read More', width=10, height=1, command=lambda: self.open_link(self.data['results'][index]['link']))
        readBtn.pack(side=BOTTOM, pady=10)
        
    def open_link(self, url):
        webbrowser.open(url)

# Create an instance of the NewsApp and start the application
news = NewsApp()
news.root.mainloop()

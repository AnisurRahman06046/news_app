# import requests
# from tkinter import Tk,Label
# class NewsApp:
#     def __init__(self):
#         # fetch data
#         self.data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9ddf978a1d1144b198c4913cf8f92731").json()
#         print(self.data)
        
#         # bdData = requests.get("https://api.apitube.io/v1/news/articles")
#         # initial gui load
#         self.load_gui()
        
#         # load first news item
#         self.load_news_item(0)
        
#     def load_gui(self):
#         self.root = Tk()
#         self.root.geometry("350x600")
#         self.root.title("News App")
#         self.root.resizable(0,0)
#         self.root.configure(background='black')
        
    
#     def clear(self):
#         for i in self.root.pack_slaves():
#             i.destroy()
    
#     def load_news_item(self,index):
#         # clear the screen
#         self.clear()
#         # heading
#         heading = Label(self.root,text=self.data['articles'][index]['title'],b='black',fg='white',wraplength=350,justify='center')
#         heading.pack(pady=(10,20))
#         heading.config(font=('verdana',50))
#         self.root.mainloop()
        
# obj = NewsApp()


import requests
from tkinter import Tk, Label

class NewsApp:
    def __init__(self):
        # fetch data
        # self.data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9ddf978a1d1144b198c4913cf8f92731").json()
        self.data = requests.get("https://newsdata.io/api/1/latest?country=bd&apikey=pub_511242bc4a4b82b34f0192f0d27534c645d43").json()
        
        print(self.data)
        
        # initial GUI load
        self.load_gui()
        
        # load the first news item
        self.load_news_item(1)
        
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
        self.root.mainloop()

# Create an instance of the NewsApp
obj = NewsApp()

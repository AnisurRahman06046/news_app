import requests
from tkinter import Tk
class NewsApp:
    def __init__(self):
        # fetch data
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9ddf978a1d1144b198c4913cf8f92731").json()
        print(self.data)
        
        # bdData = requests.get("https://api.apitube.io/v1/news/articles")
        # initial gui load
        self.load_gui()
        # load first news item
        
    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.title("News App")
        self.root.mainloop()
        
        
obj = NewsApp()
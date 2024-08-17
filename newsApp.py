import requests
class NewsApp:
    def __init__(self):
        # fetch data
        data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9ddf978a1d1144b198c4913cf8f92731").json()
        print(data)
        # initial gui load
        # load first news item
        
        
obj = NewsApp()
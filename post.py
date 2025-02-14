import requests

class Post:
    def __init__(self):
        self.API_URL = "https://api.npoint.io/d5f5fefc94cb3f25fa68"
    #first is to get all the data back 
    def get_blogs(self): 
        response = requests.get(self.API_URL)
        blogs = response.json()
        return blogs
    def specific_blog(self, index_number): 
        return Post().get_blogs()[index_number-1]
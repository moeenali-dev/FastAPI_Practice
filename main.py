from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

@app.get("/")

def home():
    return("Hello World")

@app.get("/posts")
def root():
    return("Hi this is my post")

@app.post("/createposts") 
def create_posts(worldtimes : dict = Body): 
    print(worldtimes) 
    return f"Your post is successfully created: \n Title: {worldtimes['title']} Content: {worldtimes['content']}"
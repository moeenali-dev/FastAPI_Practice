from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool 
    reviews: int
    ratings: Optional[int] = None

    
@app.get("/")
def home():
    return("Hello World")

@app.get("/posts")
def root():
    return("Hi this is my post")

@app.post("/createposts") 
def create_posts(posts = Post): 
    print(posts.dict()) 
    return f"Your post is successfully created: \n Title: {posts['title']} \n Content: {posts['content']} \n Published: {posts['published']} \n Reviews: {posts['reviews']}  \n Ratings: {posts['ratings']}"
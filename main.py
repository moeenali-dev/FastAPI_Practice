from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool 
    reviews: int
    ratings: Optional[int] = None


my_posts = [{"title: ": "Hey the title of my post is Foods " , "content:" : "Pakistani food is very scrumptious" , "published: ": "Yes it is published" , "id: " : 1} , {"title: ": "Hey the title of my post is Foods " , "content:" : "Mexican food is very scrumptious" , "published: ": "Yes it is published" , "id: " : 2}]

    
@app.get("/")
def home():
    return("Hello World")

@app.get("/posts")
def root():
    return("Hi this is my post")

@app.post("/posts") 
def create_posts(posts: Post): 
    post_dict = posts.model.dump()
    post_dict = ['id'] = randrange(0,1000)
    my_posts.append(post_dict)
    return f"Your post is successfully created: \n Title:{posts.title} \n Content: {posts.content} \n Published: {posts.published} \n Reviews: {posts.reviews}"
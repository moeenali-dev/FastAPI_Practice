from fastapi import FastAPI , status , HTTPException 
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


my_posts = [{"title": "Hey the title of my post is Foods " , "content" : "Pakistani food is very scrumptious" , "published": "Yes it is published" , "id" : 1} , {"title": "Hey the title of my post is Foods " , "content" : "Mexican food is very scrumptious" , "published": "Yes it is published" , "id" : 2}]

    
@app.get("/")
def home():
    return("Hello World")

@app.get("/posts")
def root():
    return{"data: ":  my_posts}

@app.post("/posts" , status_code=status.HTTP_201_CREATED) 
def create_posts(posts: Post): 
    post_dict = posts.model_dump()
    post_dict ['id'] = randrange(0,1000)
    my_posts.append(post_dict)
    
    return {"data: " : post_dict}


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p 
    return None
    

@app.get("/posts/{id}")
def get_specific_post(id: int ):
    post = find_post(int(id) )
    if post is None:
       raise HTTPException (status_code=status.HTTP_404_NOT_FOUND , detail=f"Your post of id {id} is not found")
    return {"Posts Details: Here is your post: ": post}

def get_index(id):
    for i, p in enumerate (my_posts):
        if p["id"] == id:
            return i
    return None
        
@app.delete("/posts/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = get_index(id)
    if post is None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND , detail=f"Your post of id {id} is not found")
    my_posts.pop(post)    
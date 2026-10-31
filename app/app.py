from fastapi import FastAPI,HTTPException

app = FastAPI()

# @app.get("/welcome to our website")
# def welcome():
#     return {"message": "Welcome to our website!"}

text_posts= [
    {
        1:{"title": "A Day in the City",
        "description": "Exploring the city and capturing beautiful moments.",
        "media_type": "video",
        "category": "Lifestyle",
        }
    },
    {
       2:{ "title": "Beautiful Nature",
        "description": "Nature reminds us to appreciate life.",
        "media_type": "photo",
        "category": "Nature",
       }
       
    },
    {
       3:{"title": "Coding Workspace",
        "description": "Building something meaningful, one line at a time.",
        "media_type": "photo",
        "category": "Technology",
        } 
    }
]
@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return text_posts[:limit]
    return text_posts





# @app.get("/posts")
# def get_all_posts(limit:int=None):
#     if limit:
#         return text_posts[:limit]
    
#     return text_posts


# @app.get("/posts/{id}")
# def get_posts_by_id(id: int):
#     for post in text_posts:
#         if id in post:
#             return post[id]

#     raise HTTPException(
#         status_code=404,
#         detail="Post not found"
#     )

from fastapi import FastAPI,HTTPException
from app.schema import postcreate,postresponse
from app.db import post,create_db_and_tables,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield




app = FastAPI(lifespan=lifespan)

@app.get("/welcome to our website")
def welcome():
    return {"message": "Welcome to our website!"}

text_posts=[{
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
    return text_posts                      # this is how we can get posts using limit up to what we want to see.


@app.get("/posts/{id}")
def get_posts_by_id(id: int):
    for post in text_posts:
        if id in post:
            return post[id]

    raise HTTPException(
        status_code=404,
        detail="Post not found"           # this is how we can get data using unique id.
    )


@app.post("/posts")
def create_post(post:postcreate):
    new_post = {"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post                               # this is how we can create new posts or some data.




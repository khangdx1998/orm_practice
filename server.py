from internal.routes import item
from internal.routes import user

from fastapi import FastAPI
from internal.repository.base import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"Message": "Hello"}

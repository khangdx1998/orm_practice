import uvicorn
from fastapi import FastAPI, Depends

from internal.repository.base import Base, engine
from internal.routes import item
from internal.routes import user
from middlewares import check_authentication_header

Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(check_authentication_header)])

app.include_router(item.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"Message": "Hello"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

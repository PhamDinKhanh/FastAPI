from fastapi import FastAPI


app = FastAPI()


app.get(/)
app.include_router(author.router)


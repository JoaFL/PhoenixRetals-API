from fastapi import FastAPI

app = FastAPI()

@app.post("/notebook")
async def post_notebook():
    return
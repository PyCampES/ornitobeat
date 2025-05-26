from fastapi import FastAPI
from routers import birds

app = FastAPI(title="OrnitoBeats API")

app.include_router(birds.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a OrnitoBeats! 🎶"}
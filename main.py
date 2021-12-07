from fastapi import FastAPI
from routes.socials import socials

app = FastAPI()
app.include_router(socials)
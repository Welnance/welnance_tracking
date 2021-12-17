from fastapi import FastAPI
from routes.socials import socials
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(socials)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

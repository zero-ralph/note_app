# main.py

from fastapi import (
    APIRouter,
    FastAPI
)
from src.api.v1.note import NoteAPI
from src.api.v1.tag import TagAPI

# Create FastAPI app (Note APP)
app = FastAPI(title="Note APP")

# Set the API Route Group Prefix
NoteAPI(app)
TagAPI(app)

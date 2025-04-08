from fastapi import (
    APIRouter,
    Depends, 
    FastAPI,
    status
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.serializer import (
    TagSerializer,
    TagInputSerializer,
)
from src.service.tag import TagService


class TagAPI:

    def __init__(self, app: FastAPI):
        self.app = app
        self.router = APIRouter(prefix='/api/tags')
        self._register_routes()

    def _register_routes(self):
        self.router.add_api_route(
            '/', self.list, methods=['GET'],
        )
        self.router.add_api_route(
            '/', self.create, methods=['POST'],
            response_model=TagSerializer
        )
        self.router.add_api_route(
            '/{tag_id}', self.retrieve, methods=['GET'],
        )
        self.router.add_api_route(
            '/{tag_id}', self.update, methods=['PUT'],
            response_model=TagSerializer
        )
        self.router.add_api_route(
            '/{tag_id}', self.delete, methods=['DELETE']
        )

        self.app.include_router(self.router)

    async def list(self, db: Session = Depends(get_db), service: TagService = Depends(TagService)):
        tags = service.list(db)

        tags_with_notes = []
        for tag in tags:
            notes = [
                {
                    'id': note.id,
                    'title': note.title,
                    'description': note.description,
                }
                for note in tag.notes
            ]
            tags_with_notes.append({**tag.__dict__, "notes": notes})
        
        return tags_with_notes
    
    async def create(self, tag: TagInputSerializer, db: Session = Depends(get_db), service: TagService = Depends(TagService)):
        tag = service.create(db, tag)
        return tag
    
    
    async def retrieve(self, tag_id: int, db: Session = Depends(get_db), service: TagService = Depends(TagService)):
        tag = service.retrieve(db, tag_id)

        tag_with_notes = []
        notes = [
            {
                'id': note.id,
                'title': note.title,
                'description': note.description,
            }
            for note in tag.notes
        ]
        tag_with_notes.append({**tag.__dict__, "notes": notes})
        
        return tag_with_notes
    
    
    async def update(self, tag_id: int, tag: TagInputSerializer, db: Session = Depends(get_db), service: TagService = Depends(TagService)):
        tag = service.update(db, tag_id, tag)
        return tag
    
    
    async def delete(self, tag_id: int, db: Session = Depends(get_db), service: TagService = Depends(TagService)):
        service.delete(db, tag_id)
        return JSONResponse(status_code=status.HTTP_410_GONE, content={'detail': 'Not Found'})
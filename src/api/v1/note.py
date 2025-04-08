from fastapi import (
    APIRouter,
    Depends, 
    FastAPI,
    status
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.service.note import NoteService
from src.serializer import (
    NoteSerializer, 
    NoteInputSerializer
)


class NoteAPI:

    def __init__(self, app: FastAPI):
        self.app = app
        self.router = APIRouter(prefix='/api/notes')
        self._register_routes()

    def _register_routes(self):
        self.router.add_api_route(
            '/', self.list, methods=['GET'],
            response_model=list[NoteSerializer]
        )
        self.router.add_api_route(
            '/', self.create, methods=['POST'],
            response_model=NoteSerializer
        )
        self.router.add_api_route(
            '/{note_id}', self.retrieve, methods=['GET'],
            response_model=NoteSerializer
        )
        self.router.add_api_route(
            '/{note_id}', self.update, methods=['PUT'],
            response_model=NoteSerializer
        )
        self.router.add_api_route(
            '/{note_id}', self.delete, methods=['DELETE']
        )

        self.app.include_router(self.router)

    async def list(self, db: Session = Depends(get_db), service: NoteService = Depends(NoteService)):
        notes = service.list(db)
        return notes
    
    async def create(self, note: NoteInputSerializer, db: Session = Depends(get_db), service: NoteService = Depends(NoteService)):
        note = service.create(db, note)
        return note
    
    
    async def retrieve(self, note_id: int, db: Session = Depends(get_db), service: NoteService = Depends(NoteService)):
        note = service.retrieve(db, note_id)
        return note
    
    
    async def update(self, note_id: int, note: NoteInputSerializer, db: Session = Depends(get_db), service: NoteService = Depends(NoteService)):
        note = service.update(db, note_id, note)
        return note
    
    
    async def delete(self, note_id: int, db: Session = Depends(get_db), service: NoteService = Depends(NoteService)):
        service.delete(db, note_id)
        return JSONResponse(status_code=status.HTTP_410_GONE, content={'detail': 'Not Found'})
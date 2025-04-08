from fastapi import Depends
from sqlalchemy.orm import Session
from src.repository.note import NoteRepository
from src.serializer import NoteInputSerializer

class NoteService:
    
    def __init__(self):
        self.repository = NoteRepository()

    def list(self, db: Session):
        return self.repository.get_all_notes(db)

    def create(self, db: Session, note: NoteInputSerializer):
        return self.repository.create_note(db, note)
        
    def retrieve(self, db: Session, note_id: int):
        return self.repository.get_note_by_id(db, note_id)

    def update(self, db: Session, note_id: int, note: NoteInputSerializer):
        return self.repository.update_note(db, note_id, note)

    def delete(self, db: Session, note_id: int):
        return self.repository.delete_note(db, note_id)
        
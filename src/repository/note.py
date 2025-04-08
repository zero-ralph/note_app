# crud.py

from sqlalchemy.orm import Session
from src.models import Note, Tag, note_tag_association
from src.serializer import NoteInputSerializer
from src.repository.tag import TagRepository
# from src.serializer.tag import TagCreate


class NoteRepository:
    
    def __init__(self):
        # self.db = db
        self.model = Note
        self.tag_repository = TagRepository

    def get_all_notes(self, db: Session):
        return db.query(self.model).all()
    
    def create_note(self, db: Session, note: NoteInputSerializer):
        note_record = Note(title=note.title, description=note.description)
    
        db.add(note_record)
    
        tags = []
        for tag in note.tags:
            if isinstance(tag, int):
                tag = self.tag_repository.get_tag_by_id(self, db, tag)
                if tag:
                    tags.append(tag)

        note_record.tags = tags

        # Commit the changes to the database
        db.commit()
        db.refresh(note_record)
        return note_record
    
    def get_note_by_id(self, db: Session, note_id: int):
        return db.query(self.model).filter(self.model.id == note_id).first()
    

    def update_note(self, db: Session, note_id: int, note: NoteInputSerializer):
        note_record = db.query(Note).filter(Note.id == note_id).first()
        if note_record:
            note_record.title = note.title
            note_record.description = note.description
            
            # Update tags association
            note_record.tags.clear()  # Remove existing tags
            
            # Add new tags from the request
            if note.tags:
                for tag_id in note.tags:
                    tag = db.query(Tag).filter(Tag.id == tag_id).first()
                    note_record.tags.append(tag)
            
            db.commit()
            db.refresh(note_record)
        
        return note_record

 

    def delete_note(self, db: Session, note_id: int):
        note_record = self.get_note_by_id(db, note_id)
        if note_record:
            db.delete(note_record)
            db.commit()
        return note_record

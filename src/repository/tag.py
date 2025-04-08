
from sqlalchemy.orm import Session, selectinload
from src.models import Tag
from src.serializer  import TagInputSerializer


class TagRepository:
    
    def __init__(self):
        self.model = Tag

    def get_all_tags(self, db: Session):
        return db.query(self.model).options(selectinload(self.model.notes)).all()
    
    def create_tag(self, db: Session, tag: TagInputSerializer):
        tag = Tag(name=tag.name)
        db.add(tag)
        db.commit()
        db.refresh(tag)
        return tag

    def get_tag_by_id(self, db: Session, tag_id: int):
        return db.query(self.model).filter(self.model.id == tag_id).first()

    def update_tag(self, db: Session, tag_id: int, tag: TagInputSerializer):
        tag_record = self.get_tag_by_id(db, tag_id)
        if tag_record:
            tag_record.name = tag.name
            db.commit()
            db.refresh(tag_record)

        return tag_record

    def delete_tag(self, db: Session, tag_id: int):
        tag_record = self.get_tag_by_id(db, tag_id)
        if tag_record:
            db.delete(tag_record)
            db.commit()
        return tag_record

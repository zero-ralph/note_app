from sqlalchemy.orm import Session
from src.serializer import TagInputSerializer
from src.repository.tag import TagRepository


class TagService:

    def __init__(self):
        self.repository = TagRepository()

    def list(self, db: Session):
        return self.repository.get_all_tags(db)

    def create(self, db: Session, tag: TagInputSerializer):
        return self.repository.create_tag(db, tag)

    def retrieve(self, db: Session, tag_id: int):
        return self.repository.get_tag_by_id(db, tag_id)

    def update(self, db: Session, tag_id: int, tag: TagInputSerializer):
        return self.repository.update_tag(db, tag_id, tag)

    def delete(self, db: Session, tag_id: int):
        return self.repository.delete_tag(db, tag_id)

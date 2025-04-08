from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Table, 
    ForeignKey
)
from sqlalchemy.orm import relationship
from src.config.base import Base


# Association table for the many-to-many relationship between Note and Tag
note_tag_association = Table(
    'note_tag',
    Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

# Note Model
class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    # Relationship to tags
    tags = relationship('Tag', secondary=note_tag_association, back_populates="notes")

# Tag Model
class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Relationship to notes
    notes = relationship("Note", secondary=note_tag_association, back_populates="tags")
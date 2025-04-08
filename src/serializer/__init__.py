from typing import List, Optional
from pydantic import BaseModel



# Tag Serializers
class TagBaseSerializer(BaseModel):
    name: str

class TagInputSerializer(TagBaseSerializer):
    pass

class TagSerializer(TagBaseSerializer):
    id: int
    
    class Config:
        from_attributes = True 

# Note Serializers
class NoteBaseSerializer(BaseModel):
    title: str
    description: str

class NoteInputSerializer(NoteBaseSerializer):
    tags: Optional[List[int]] = [] 

class NoteSerializer(NoteBaseSerializer):
    id: int
    tags: List[TagSerializer]

    class Config:
        from_attributes = True


class TagSerializerResponse(TagBaseSerializer):
    id: int
    notes: List[NoteSerializer]

    class Config:
        from_attributes = True


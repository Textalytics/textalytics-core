from typing import Optional, List
from pydantic import BaseModel


class TextInput(BaseModel):
    source_text: str
    source_language: Optional[str] = "en"
    provider: Optional[str]
    model_name: Optional[str]


class Entity(BaseModel):
    entity: str
    label: str
    description: Optional[str]
    resolution_id: Optional[str]
    resolution_link: Optional[str]
    resolution_type: Optional[str]
    pos_tag: Optional[str]
    start_offset: Optional[int]
    end_offset: Optional[int]


class EntityRecognizerOutput(BaseModel):
    entities: List[Entity]

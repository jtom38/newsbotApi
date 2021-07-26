from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import uuid4

class Articles(BaseModel):
    id: Optional[str] 
    siteName: Optional[str]
    sourceName: Optional[str]
    sourceType: Optional[str]
    tags: Optional[str]
    title: Optional[str]
    url: Optional[str]
    pubDate: Optional[date]
    video: Optional[str]
    videoHeight: Optional[int]
    videoWidth: Optional[int]
    thumbnail: Optional[str]
    description: Optional[str]
    authorName: Optional[str]
    authorImage: Optional[str]

    class Config:
        orm_mode = True

class DiscordQueue(BaseModel):
    id: str
    siteName: Optional[str]
    title: Optional[str]
    link: Optional[str]
    tags: Optional[str]
    thumbnail: Optional[str]
    description: Optional[str]
    video: Optional[str]
    videoHeight: Optional[int]
    videoWidth: Optional[int]
    authorName: Optional[str]
    authorImage: Optional[str]
    sourceName: Optional[str]
    sourceType: Optional[str]

    class Config:
        orm_mode = True

class DiscordWebHooks(BaseModel):
    id: Optional[str]
    name: Optional[str]
    key: Optional[str]
    url: Optional[str]
    server: Optional[str]
    channel: Optional[str]
    enabled: bool
    fromEnv: bool
    class Config:
        orm_mode = True

class Icons(BaseModel):
    id: Optional[str]
    filename: Optional[str]
    site: Optional[str]

    class Config:
        orm_mode = True

class Logs(BaseModel):
    id: Optional[str]
    date: Optional[str]
    time: Optional[str]
    type: Optional[str]
    caller: Optional[str]
    message: Optional[str]

    class Config:
        orm_mode = True

class Settings(BaseModel):
    id: Optional[str]
    key: Optional[str]
    value: Optional[str]
    options: Optional[str]
    notes: Optional[str]

    class Config:
        orm_mode = True

class Sources(BaseModel):
    id: Optional[str]
    name: Optional[str]
    source: Optional[str]
    type: Optional[str]
    value: Optional[str]
    enabled: bool
    url: Optional[str]
    tags: Optional[str]
    fromEnv: bool

class SourceLinks(BaseModel):
    id: Optional[str]
    sourceID: Optional[str]
    sourceType: Optional[str]
    sourceName: Optional[str]
    discordName: Optional[str]
    discordID: Optional[str]
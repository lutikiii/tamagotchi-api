from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class PetUpdate(BaseModel):
    name: str | None = None
    hunger: int | None = None
    mood: int | None = None
    cleanliness: int | None = None
    # --- НОВЫЕ ПОЛЯ ---
    imageBase64: str | None = None
    lastFedTime: int | None = None
    lastPettedTime: int | None = None
    lastWashedTime: int | None = None

class PetResponse(BaseModel):
    id: int
    name: str
    hunger: int
    mood: int
    cleanliness: int
    # --- НОВЫЕ ПОЛЯ ---
    imageBase64: str | None = None
    lastFedTime: int | None = None
    lastPettedTime: int | None = None
    lastWashedTime: int | None = None
    class Config:
        from_attributes = True
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    pet = relationship("Pet", back_populates="owner", uselist=False)

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="Без имени")
    hunger = Column(Integer, default=0)
    mood = Column(Integer, default=0)
    cleanliness = Column(Integer, default=0)
    
    # --- НОВЫЕ КОЛОНКИ ---
    imageBase64 = Column(String, default="") # Для картинки
    lastFedTime = Column(Integer, default=0) # Для таймера еды
    lastPettedTime = Column(Integer, default=0) # Для таймера поглаживания
    lastWashedTime = Column(Integer, default=0) # Для таймера мытья
    # ---------------------
    
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="pet")

# --- ТАБЛИЦА ДЛЯ ЕДЫ ---
class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hungerPercent = Column(Integer)
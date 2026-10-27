from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tamagotchi API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ЗАПОЛНЕНИЕ БАЗЫ ПРИ СТАРТЕ (ПРОДУКТЫ И АДМИН) ---
db = SessionLocal()

# 1. Продукты
if db.query(models.Food).count() == 0:
    foods_data = [
        # Съедобное
        {"name": "Яблоко", "hungerPercent": 2}, {"name": "Апельсин", "hungerPercent": 3},
        {"name": "Банан", "hungerPercent": 4}, {"name": "Груша", "hungerPercent": 2},
        {"name": "Клубника", "hungerPercent": 3}, {"name": "Вишня", "hungerPercent": 2},
        {"name": "Арбуз", "hungerPercent": 5}, {"name": "Дыня", "hungerPercent": 5},
        {"name": "Морковь", "hungerPercent": 2}, {"name": "Картофель", "hungerPercent": 3},
        {"name": "Огурец", "hungerPercent": 2}, {"name": "Помидор", "hungerPercent": 2},
        {"name": "Хлеб", "hungerPercent": 5}, {"name": "Сыр", "hungerPercent": 7},
        {"name": "Колбаса", "hungerPercent": 8}, {"name": "Курица", "hungerPercent": 10},
        {"name": "Рыба", "hungerPercent": 8}, {"name": "Мясо", "hungerPercent": 12},
        {"name": "Молоко", "hungerPercent": 4}, {"name": "Кефир", "hungerPercent": 4},
        {"name": "Йогурт", "hungerPercent": 5}, {"name": "Каша", "hungerPercent": 7},
        {"name": "Суп", "hungerPercent": 8}, {"name": "Макароны", "hungerPercent": 6},
        {"name": "Пицца", "hungerPercent": 15}, {"name": "Бургер", "hungerPercent": 14},
        {"name": "Шоколад", "hungerPercent": 5}, {"name": "Печенье", "hungerPercent": 4},
        {"name": "Мороженое", "hungerPercent": 5}, {"name": "Торт", "hungerPercent": 10},
        {"name": "Мед", "hungerPercent": 6}, {"name": "Орехи", "hungerPercent": 5},
        {"name": "Яйцо", "hungerPercent": 4}, {"name": "Рис", "hungerPercent": 6},
        {"name": "Устрица", "hungerPercent": 3}, {"name": "Сок", "hungerPercent": 3},
        {"name": "Сосиска", "hungerPercent": 8}, {"name": "Бекон", "hungerPercent": 12},
        {"name": "Стейк", "hungerPercent": 18}, {"name": "Котлета", "hungerPercent": 10},
        {"name": "Пельмени", "hungerPercent": 9}, {"name": "Блины", "hungerPercent": 7},
        {"name": "Сырники", "hungerPercent": 8}, {"name": "Оладьи", "hungerPercent": 7},
        {"name": "Плов", "hungerPercent": 12}, {"name": "Гречка", "hungerPercent": 6},
        {"name": "Овсянка", "hungerPercent": 5}, {"name": "Мюсли", "hungerPercent": 4},
        {"name": "Бутерброд", "hungerPercent": 6}, {"name": "Шаурма", "hungerPercent": 14},
        {"name": "Хот-дог", "hungerPercent": 11}, {"name": "Наггетсы", "hungerPercent": 9},
        {"name": "Картошка фри", "hungerPercent": 10}, {"name": "Чипсы", "hungerPercent": 3},
        {"name": "Сухарики", "hungerPercent": 2}, {"name": "Попкорн", "hungerPercent": 3},
        {"name": "Крекеры", "hungerPercent": 3}, {"name": "Вафли", "hungerPercent": 5},
        {"name": "Пряники", "hungerPercent": 6}, {"name": "Конфета", "hungerPercent": 2},
        {"name": "Мармелад", "hungerPercent": 3}, {"name": "Зефир", "hungerPercent": 4},
        {"name": "Пастила", "hungerPercent": 4}, {"name": "Халва", "hungerPercent": 7},
        {"name": "Нут", "hungerPercent": 6}, {"name": "Фасоль", "hungerPercent": 6},
        {"name": "Горох", "hungerPercent": 5}, {"name": "Чечевица", "hungerPercent": 6},
        {"name": "Кукуруза", "hungerPercent": 4}, {"name": "Капуста", "hungerPercent": 2},
        {"name": "Брокколи", "hungerPercent": 3}, {"name": "Свекла", "hungerPercent": 3},
        {"name": "Репа", "hungerPercent": 2}, {"name": "Тыква", "hungerPercent": 5},
        {"name": "Кабачок", "hungerPercent": 3}, {"name": "Баклажан", "hungerPercent": 3},
        {"name": "Перец", "hungerPercent": 2}, {"name": "Лук", "hungerPercent": 1},
        {"name": "Чеснок", "hungerPercent": 1}, {"name": "Виноград", "hungerPercent": 4},
        {"name": "Слива", "hungerPercent": 3}, {"name": "Персик", "hungerPercent": 3},
        {"name": "Абрикос", "hungerPercent": 3}, {"name": "Гранат", "hungerPercent": 4},
        {"name": "Хурма", "hungerPercent": 4}, {"name": "Ананас", "hungerPercent": 5},
        {"name": "Манго", "hungerPercent": 5}, {"name": "Киви", "hungerPercent": 3},
        {"name": "Лимон", "hungerPercent": 1}, {"name": "Лайм", "hungerPercent": 1},
        # Несъедобное
        {"name": "Камень", "hungerPercent": -10}, {"name": "Носк", "hungerPercent": -5},
        {"name": "Батарейка", "hungerPercent": -15}, {"name": "Мыло", "hungerPercent": -8},
        {"name": "Бензин", "hungerPercent": -20}, {"name": "Стекло", "hungerPercent": -12},
        {"name": "Гвоздь", "hungerPercent": -10}, {"name": "Вилка", "hungerPercent": -8},
        {"name": "Ложка", "hungerPercent": -6}, {"name": "Провод", "hungerPercent": -10},
        {"name": "Губка", "hungerPercent": -7}, {"name": "Пластик", "hungerPercent": -9},
        {"name": "Бумага", "hungerPercent": -3}, {"name": "Картон", "hungerPercent": -4},
        {"name": "Резина", "hungerPercent": -8}, {"name": "Металл", "hungerPercent": -15},
        {"name": "Земля", "hungerPercent": -5}, {"name": "Песок", "hungerPercent": -6},
        {"name": "Кирпич", "hungerPercent": -12}, {"name": "Пуговица", "hungerPercent": -4}
    ]
    for food in foods_data:
        db.add(models.Food(**food))
    db.commit()

# 2. Админ
if not db.query(models.User).filter(models.User.username == "админ").first():
    admin_user = models.User(username="админ", password="админ123")
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    
    admin_pet = models.Pet(user_id=admin_user.id, name="Админский питомец")
    db.add(admin_pet)
    db.commit()

db.close()
# -------------------------------------------------

# 1. РЕГИСТРАЦИЯ
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким логином уже существует")
    
    new_user = models.User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    new_pet = models.Pet(user_id=new_user.id)
    db.add(new_pet)
    db.commit()
    
    return new_user

# 2. ВХОД
@app.post("/login/")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    return {"user_id": db_user.id, "message": "Успешный вход"}

# 3. ПОЛУЧЕНИЕ ПИТОМЦА
@app.get("/users/{user_id}/pet/", response_model=schemas.PetResponse)
def get_pet(user_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.user_id == user_id).first()
    if not pet:
        pet = models.Pet(user_id=user_id)
        db.add(pet)
        db.commit()
        db.refresh(pet)
    return pet

# 4. СОХРАНЕНИЕ ПРОГРЕССА
@app.post("/users/{user_id}/pet/update/")
def update_pet_stats(user_id: int, pet_update: schemas.PetUpdate, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.user_id == user_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Питомец не найден")
    
    if pet_update.hunger is not None: pet.hunger = pet_update.hunger
    if pet_update.mood is not None: pet.mood = pet_update.mood
    if pet_update.cleanliness is not None: pet.cleanliness = pet_update.cleanliness
    # --- НОВЫЕ ПОЛЯ ---
    if pet_update.imageBase64 is not None: pet.imageBase64 = pet_update.imageBase64
    if pet_update.lastFedTime is not None: pet.lastFedTime = pet_update.lastFedTime
    if pet_update.lastPettedTime is not None: pet.lastPettedTime = pet_update.lastPettedTime
    if pet_update.lastWashedTime is not None: pet.lastWashedTime = pet_update.lastWashedTime
    # -----------------
    
    db.commit()
    db.refresh(pet)
    return pet

# 5. УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
@app.delete("/users/{user_id}/")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    db.query(models.Pet).filter(models.Pet.user_id == user_id).delete()
    db.delete(user)
    db.commit()
    return {"message": "Аккаунт удален"}

# 6. ПОЛУЧЕНИЕ СПИСКА ЕДЫ
@app.get("/foods/")
def get_foods(db: Session = Depends(get_db)):
    return db.query(models.Food).order_by(models.Food.name).all()

# 7. ИЗМЕНЕНИЕ ИМЕНИ ПИТОМЦА
@app.post("/users/{user_id}/pet/rename/")
def rename_pet(user_id: int, new_name: str, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.user_id == user_id).first()
    if pet:
        pet.name = new_name
        db.commit()
        db.refresh(pet)
    return pet
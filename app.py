from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from passlib.context import CryptContext
from datetime import datetime
import uvicorn

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    email = Column(String, unique=True, index=True)
    appointments = relationship("Appointment", back_populates="user")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime)
    description = Column(String)
    user = relationship("User", back_populates="appointments")

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(Text)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Seed data
def seed_data():
    db = SessionLocal()
    if not db.query(User).first():
        user = User(username="testuser", password_hash=get_password_hash("testpass"), email="test@example.com")
        db.add(user)
        db.commit()
        db.refresh(user)
        appointment = Appointment(user_id=user.id, date=datetime.now(), description="General Checkup")
        db.add(appointment)
        db.commit()
    db.close()

seed_data()

# FastAPI app
app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        return f.read()

@app.get("/chat", response_class=HTMLResponse)
async def chat_page():
    with open("templates/chat.html") as f:
        return f.read()

@app.get("/appointments", response_class=HTMLResponse)
async def appointments_page():
    with open("templates/appointments.html") as f:
        return f.read()

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    with open("templates/login.html") as f:
        return f.read()

@app.get("/admin", response_class=HTMLResponse)
async def admin_page():
    with open("templates/admin.html") as f:
        return f.read()

# API Endpoints
@app.post("/api/chat")
async def chat_endpoint():
    return {"response": "This is a mock response from the chatbot."}

@app.get("/api/appointments")
async def get_appointments():
    db = SessionLocal()
    appointments = db.query(Appointment).all()
    db.close()
    return appointments

@app.post("/api/appointments")
async def create_appointment():
    return {"status": "Appointment created successfully."}

@app.post("/api/login")
async def login():
    return {"status": "User authenticated successfully."}

@app.get("/api/users")
async def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from core.database import Base, engine
from controllers import item

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item.router)
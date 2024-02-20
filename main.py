from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.route.health import router as health_router
from src.service.mongo_service import connect_and_init_db, close_db_connect, get_db
from src.utils.config import Config

app = FastAPI()

# DB Events
app.add_event_handler("startup", Config.app_settings_validate)
app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_db_connect)


app.include_router(
    health_router,
    prefix='/health',
    tags=["health"]
)

@app.get("/")
async def health(db: AsyncIOMotorDatabase = Depends(get_db)):
    # db.getCollectionInfos
    print(await db.test.sample_resource.find_one())
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

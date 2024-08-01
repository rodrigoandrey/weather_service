import math
from fastapi import FastAPI, HTTPException, BackgroundTasks

from settings import DATA_FILE, PROGRESS_FILE
from utils import load_data, city_ids, collect_weather_data_task

app = FastAPI()

# City IDs from Appendix A


@app.get('/')
def home_index():
    return {"status": "Hello World!"}


@app.post("/api/weather/{user_id}")
async def collect_weather_data(user_id: str, background_tasks: BackgroundTasks):
    """Route to post a new user from user_id"""
    user_id = user_id

    data_store = load_data(DATA_FILE)
    if user_id in data_store:
        raise HTTPException(status_code=400, detail="User ID already exists")

    background_tasks.add_task(collect_weather_data_task, user_id)
    return {"status": "Data collection started", "user_id": user_id}


@app.get("/api/weather/{user_id}/progress")
async def get_progress(user_id: str):
    """Route to get progress from user_id"""
    progress = load_data(PROGRESS_FILE)
    if user_id not in progress:
        raise HTTPException(status_code=404, detail="User ID not found")

    total_cities = len(city_ids)
    completed = progress[user_id]
    _progress = math.ceil((completed / total_cities) * 100)
    return {"progress": _progress}


@app.get("/api/weather/{user_id}/data")
async def get_weather_data(user_id: str):
    """Route to get user data from user_id"""
    data_store = load_data(DATA_FILE)
    if user_id not in data_store:
        raise HTTPException(status_code=404, detail="User ID not found")

    return data_store[user_id]

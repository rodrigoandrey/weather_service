import os

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from main import app

load_dotenv()

client = TestClient(app)

DATA_FILE = os.getenv("DATA_FILE", "./database/data_store.json")

os.environ["DEBUG"] = "0"


def test_post_weather():
    response = client.post("/api/weather/test_user")
    assert response.status_code == 200
    assert response.json()["status"] == "Data collection started"


def test_get_progress():
    response = client.get("/api/weather/test_user/progress")
    assert response.status_code == 200
    assert "progress" in response.json()


def test_get_weather_data():
    response = client.get("/api/weather/test_user/data")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

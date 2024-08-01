import os
from dotenv import load_dotenv

load_dotenv()

OWM_API_KEY = os.getenv("OWM_API_KEY", "your_open_weather_api_key")  # Replace with your Open Weather Map API key
OWM_API_URL = "http://api.openweathermap.org/data/2.5/weather"

DATA_FILE = "./database/data_store.json"
PROGRESS_FILE = "./database/progress.json"

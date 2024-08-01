from pydantic import BaseModel


class WeatherData(BaseModel):
    user_id: str
    request_datetime: str
    city_id: int
    celsius_temperature: float
    humidity: int

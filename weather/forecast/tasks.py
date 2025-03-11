from celery import shared_task
import requests
from .models import City, WeatherData
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Avg
import logging
from dotenv import load_dotenv

# Налаштування логування
logger = logging.getLogger(__name__)


@shared_task
def update_weather_data():
    """
    Завдання для оновлення даних про погоду для всіх міст.
    """
    logger.info("Starting weather data update task.")

    for city in City.objects.all():
        try:
            # Запит до API погоди
            response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "lat": city.latitude,
                    "lon": city.longitude,
                    "appid": os.environ.get('WEATHER_API_KEY'),
                    "units": "metric",
                },
            )
            response.raise_for_status()  # Викидає виняток, якщо статус не 200

            data = response.json()

            # Створення запису погоди
            WeatherData.objects.create(
                city=city,
                timestamp=now(),
                temperature=data["main"]["temp"],
                humidity=data["main"]["humidity"],
                pressure=data["main"]["pressure"],
                weather_description=data["weather"][0]["description"],
                wind_speed=data["wind"]["speed"],
                wind_direction=data["wind"].get("deg"),
            )
            logger.info(f"Weather data updated successfully for city: {city.name}.")

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch weather data for city: {city.name}. Error: {e}")
        except Exception as e:
            logger.exception(f"An unexpected error occurred while updating weather data for city: {city.name}.")

    logger.info("Weather data update task completed.")


@shared_task
def generate_weather_statistics():
    """
    Завдання для генерації статистики погоди за останній тиждень.
    """
    logger.info("Starting weather statistics generation task.")

    for city in City.objects.all():
        try:
            # Фільтрація даних за останній тиждень
            past_week_data = WeatherData.objects.filter(
                city=city,
                timestamp__gte=now() - timedelta(days=7)
            )
            if past_week_data.exists():
                avg_temp = past_week_data.aggregate(Avg('temperature'))['temperature__avg']
                avg_humidity = past_week_data.aggregate(Avg('humidity'))['humidity__avg']
                logger.info(
                    f"City: {city.name}, Avg Temp: {avg_temp:.2f}°C, Avg Humidity: {avg_humidity:.2f}%."
                )
            else:
                logger.warning(f"No weather data found for city: {city.name} for the past week.")
        except Exception as e:
            logger.exception(f"An error occurred while generating statistics for city: {city.name}. Error: {e}")

    logger.info("Weather statistics generation task completed.")

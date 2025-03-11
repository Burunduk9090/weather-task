from rest_framework import serializers
from forecast.models import City, WeatherData


class CitySerializer(serializers.ModelSerializer):
    """
    Серіалізатор для моделі City.
    """
    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'latitude', 'longitude']  # Явно вказані поля


class WeatherDataSerializer(serializers.ModelSerializer):
    """
    Серіалізатор для моделі WeatherData.
    """
    city = serializers.StringRelatedField()  # Повертає назву міста у читабельному вигляді

    class Meta:
        model = WeatherData
        fields = [
            'city_id', 'city', 'timestamp', 'temperature',
            'humidity', 'pressure', 'weather_description',
            'wind_speed', 'wind_direction'
        ]


from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.country}"

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='weather_data')
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    weather_description = models.CharField(max_length=255)
    wind_speed = models.FloatField()
    wind_direction = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Weather in {self.city.name} at {self.timestamp}"


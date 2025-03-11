from django.contrib import admin
from .models import City, WeatherData

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'latitude', 'longitude')
    search_fields = ('name', 'country')
    list_filter = ('country',)

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'timestamp', 'temperature', 'humidity', 'weather_description')
    search_fields = ('city__name', 'weather_description')
    list_filter = ('city', 'timestamp')
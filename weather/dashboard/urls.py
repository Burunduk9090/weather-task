from django.urls import path
from .views import weather_dashboard, city_weather

urlpatterns = [
    path('', weather_dashboard, name='dashboard-index'),
    # path('<int:city_id>/', city_weather, name='city-weather'),
]

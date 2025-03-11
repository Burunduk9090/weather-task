from django.urls import path
from .views import CityListView, WeatherDataView

urlpatterns = [
    path('cities/', CityListView.as_view(), name='cities'),
    path('cities/<int:city_id>/', WeatherDataView.as_view(), name='weather'),

]

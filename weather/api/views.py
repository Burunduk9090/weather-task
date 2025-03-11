from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from forecast.models import City, WeatherData
from .serializers import CitySerializer, WeatherDataSerializer


class CityListView(ListAPIView):
    """
    Представлення для отримання списку всіх міст.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class WeatherDataView(ListAPIView):
    """
    Представлення для отримання всіх погодних даних для конкретного міста.
    """
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')  # Отримує ID міста з URL
        try:
            city = City.objects.get(id=city_id)
        except City.DoesNotExist:
            raise NotFound(f"City with id {city_id} not found.")  # Повертає помилку, якщо місто не знайдене
        return WeatherData.objects.filter(city=city)  # Фільтрує погодні дані за містом

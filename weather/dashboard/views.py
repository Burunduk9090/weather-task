from django.shortcuts import render, get_object_or_404
from forecast.models import City, WeatherData

def weather_dashboard(request):
    """
    Рендерить фронтенд для погодного дашборду.
    """
    return render(request, 'weather.html')


def city_weather(request, city_id):
    """
    Відображає HTML-сторінку з деталями погоди для конкретного міста.
    """
    city = get_object_or_404(City, id=city_id)
    weather_data = WeatherData.objects.filter(city=city).order_by('-timestamp')
    return render(request, 'city_weather.html', {'city': city, 'weather_data': weather_data})

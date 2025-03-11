from .models import City

def add_top_cities_to_db():
    """
    Додає 5 найбільших міст України до бази даних.
    """
    cities = [
        {"name": "Kyiv", "country": "UA", "latitude": 50.4501, "longitude": 30.5234},
        {"name": "Kharkiv", "country": "UA", "latitude": 49.9935, "longitude": 36.2304},
        {"name": "Odesa", "country": "UA", "latitude": 46.4825, "longitude": 30.7233},
        {"name": "Dnipro", "country": "UA", "latitude": 48.4647, "longitude": 35.0462},
        {"name": "Lviv", "country": "UA", "latitude": 49.8397, "longitude": 24.0297},
    ]

    for city_data in cities:
        city, created = City.objects.get_or_create(
            name=city_data["name"],
            country=city_data["country"],
            latitude=city_data["latitude"],
            longitude=city_data["longitude"]
        )
        if created:
            print(f"Added new city: {city.name}")
        else:
            print(f"City {city.name} already exists.")

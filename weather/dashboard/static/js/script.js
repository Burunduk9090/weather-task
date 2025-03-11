// Елементи для роботи
const citiesContainer = document.getElementById("cities-container"); // Контейнер для списку міст
const cityDetailsContainer = document.createElement("div"); // Динамічний контейнер для деталей міста
cityDetailsContainer.id = "city-details"; // Встановлюємо ID контейнера
document.body.appendChild(cityDetailsContainer); // Додаємо цей контейнер до сторінки

// URL API
const apiUrl = "/api"; // Головний URL API (без слешу в кінці)

// Функція для отримання списку міст
async function fetchCities() {
    try {
        const response = await fetch(`${apiUrl}/cities/`); // Запит до головного API
        if (!response.ok) throw new Error("Failed to fetch cities data");

        const cities = await response.json(); // Парсимо JSON
        citiesContainer.innerHTML = ""; // Очищення контейнера

        cities.forEach(city => {
            const cityCard = document.createElement("div");
            cityCard.className = "city-card";
            cityCard.innerHTML = `
                <h3>${city.name}, ${city.country}</h3>
                <p><strong>Latitude:</strong> ${city.latitude}</p>
                <p><strong>Longitude:</strong> ${city.longitude}</p>
                <button onclick="fetchCityDetails(${city.id}, '${city.name}')">View Details</button>
            `;
            citiesContainer.appendChild(cityCard);
        });
    } catch (error) {
        console.error("Error fetching cities:", error);
        citiesContainer.innerHTML = "<p>Error loading cities. Please try again later.</p>";
    }
}

// Функція для отримання деталей міста за ID
async function fetchCityDetails(cityId, cityName) {
    try {
        const response = await fetch(`${apiUrl}/cities/${cityId}/`); // Запит до API з ID міста
        if (!response.ok) throw new Error("Failed to fetch city weather data");

        const weatherData = await response.json(); // Парсимо JSON

        // Очищення попередніх деталей
        cityDetailsContainer.innerHTML = `
            <h2>Weather Details for ${cityName}</h2>
            <button onclick="closeDetails()">Back to Cities</button>
        `;

        if (weatherData.length === 0) {
            cityDetailsContainer.innerHTML += `<p>No weather data available for this city.</p>`;
        } else {
            const weatherList = document.createElement("ul");

            weatherData.forEach(data => {
                const weatherItem = document.createElement("li");
                weatherItem.innerHTML = `
                    <p><strong>Timestamp:</strong> ${data.timestamp}</p>
                    <p><strong>Temperature:</strong> ${data.temperature}°C</p>
                    <p><strong>Humidity:</strong> ${data.humidity}%</p>
                    <p><strong>Description:</strong> ${data.weather_description}</p>
                    <p><strong>Wind Speed:</strong> ${data.wind_speed} m/s</p>
                    <p><strong>Wind Direction:</strong> ${data.wind_direction}°</p>
                `;
                weatherList.appendChild(weatherItem);
            });

            cityDetailsContainer.appendChild(weatherList);
        }

        // Показати контейнер із деталями та сховати список міст
        citiesContainer.style.display = "none";
        cityDetailsContainer.style.display = "block";
    } catch (error) {
        console.error("Error fetching city details:", error);
        cityDetailsContainer.innerHTML = "<p>Error loading weather details. Please try again later.</p>";
    }
}

// Функція для повернення до списку міст
function closeDetails() {
    cityDetailsContainer.style.display = "none"; // Сховати контейнер із деталями
    citiesContainer.style.display = "flex"; // Показати список міст
    citiesContainer.style.flexWrap = "wrap"; // Дозволити перенесення в рядки
    citiesContainer.style.justifyContent = "center"; // Вирівнювання по центру
    citiesContainer.style.alignItems = "flex-start"; // Вирівнювання по верхньому краю
}

// Завантаження міст при завантаженні сторінки
window.onload = fetchCities;

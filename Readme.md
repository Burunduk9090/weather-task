---

# 🌦️ Dashboard for Weather Data

A Django-based web application that collects, processes, and displays weather data from a public API. This project demonstrates the use of Python, Django, PostgreSQL, Celery, Redis, and frontend technologies to create a scalable and responsive dashboard.

---

## 📝 Project Description

The application fetches weather data for 5-10 major cities worldwide using the [OpenWeatherMap API](https://openweathermap.org/api) or any other free weather API. The data is stored in a PostgreSQL database and is periodically updated using Celery and Redis. The project also features:

- A responsive frontend dashboard to display real-time weather data.
- A RESTful API for accessing weather data programmatically.

This project emphasizes scalability and maintainability by incorporating modern best practices, making it ready for further development and real-world applications.

---

## ⚙️ Setup Instructions

Follow these steps to set up and run the project locally or in a Docker environment:

### Prerequisites

- Python 3.x
- Docker & Docker Compose (for containerization)
- Redis
- PostgreSQL

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/username/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Install dependencies:**

   Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**

   Make sure PostgreSQL is running. Create a new database and update the `DATABASES` settings in `settings.py`.

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Add your API Key:**

   Create an `.env` file in the project directory and add your API key for OpenWeatherMap:

   ```env
   WEATHER_API_KEY=your_api_key_here
   ```

6. **Run the application:**

   Start the development server:

   ```bash
   python manage.py runserver
   ```

7. **Set up Celery and Redis:**

   Start Redis (if it's not already running):

   ```bash
   redis-server
   ```

   Run the Celery worker:

   ```bash
   celery -A project_name worker --loglevel=info
   ```

8. **(Optional) Dockerized Setup:**

   If you want to use Docker for deployment, build and run the containers:

   ```bash
   docker-compose up --build
   ```

---

## 📋 API Documentation

### **Base URL**

```
http://<your-domain>/api/
```

---

### **Endpoints**

#### 1. `GET /api/cities/`
**Description:** Fetch a list of cities with current weather data.

- **Method:** `GET`
- **Response:** A JSON array containing basic weather information for each city.

**Example Request:**
```http
GET /api/cities/ HTTP/1.1
Host: <your-domain>
```

**Example Response:**
```json
[
    {
        "city_id": 1,
        "city": "Kyiv, UA",
        "timestamp": "2025-03-11T10:35:53.164683Z",
        "temperature": 19.57,
        "humidity": 34.0,
        "pressure": 1003.0,
        "weather_description": "overcast clouds",
        "wind_speed": 5.17,
        "wind_direction": 226.0
    }, 
    {
        "city_id": 2,
        "city": "Kharkiv, UA",
        "timestamp": "2025-03-11T12:24:23.938972Z",
        "temperature": 14.94,
        "humidity": 41.0,
        "pressure": 1009.0,
        "weather_description": "overcast clouds",
        "wind_speed": 6.04,
        "wind_direction": 205.0
    }
]
```

---

#### 2. `GET /api/cities/<city_id>/`
**Description:** Fetch current weather data for a specific city.

- **Method:** `GET`
- **Path Parameter:**
  - `city_id` – unique identifier for the city
- **Response:** A JSON object containing city details and current weather information.

**Example Request:**
```http
GET /api/cities/1/ HTTP/1.1
Host: <your-domain>
```

**Example Response:**
```json
{
    "city_id": 1,
    "city": "Kyiv, UA",
    "timestamp": "2025-03-11T10:35:53.164683Z",
    "temperature": 19.57,
    "humidity": 34.0,
    "pressure": 1003.0,
    "weather_description": "overcast clouds",
    "wind_speed": 5.17,
    "wind_direction": 226.0
}
```

---

### **Error Responses**

#### 1. **404 Not Found:**
Occurs if an invalid endpoint is accessed.

**Example Response:**
```json
{
    "error": "Invalid endpoint. Please check the URL."
}
```

---

## 💡 Explanation of Design Decisions

As this was a time-constrained task (8-hour test assignment), the focus was on creating a scalable foundation rather than adding all features. Below are some key decisions:

1. **Scalability:**
   - Implemented **Docker** for containerized deployment.
   - Used **Redis** as a message broker for Celery to schedule periodic updates to weather data.
   - Designed a well-structured PostgreSQL database to store and retrieve weather data efficiently.

2. **Maintainability:**
   - Organized Django apps, models, views, and URLs according to best practices.
   - Added logging to track errors and application activity.

3. **Extensibility:**
   - Prepared the project for future features, like user authentication and advanced data visualizations.
   - Modularized the architecture to facilitate easier updates.

---

## 🚀 Deliverables

- Source code in this repository.
- Responsive web dashboard to display weather data.
- RESTful API for programmatic access to data.
- Periodic updates of weather data using Celery and Redis.

---

## 📖 Notes

- Ensure you have adequate API request limits if you're using a free-tier weather API.
- Replace placeholders in this document (e.g., `your_api_key_here`) with actual values before sharing with others.

---

Feel free to reach out with any questions or suggestions! 🎉

---


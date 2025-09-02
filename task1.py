import requests
import matplotlib.pyplot as plt
from datetime import datetime

# 🔑 Replace with your actual API key
API_KEY = "05bf4e8ead43e56a5d9ed87d9e739f74"
CITY = "Bengaluru"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# 📡 Fetch data from OpenWeatherMap
response = requests.get(URL)
data = response.json()

# 🧹 Extract temperature and time
timestamps = []
temperatures = []

for entry in data['list']:
    temp = entry['main']['temp']
    time = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S")
    temperatures.append(temp)
    timestamps.append(time)

# 🎨 Plotting with Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='teal')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
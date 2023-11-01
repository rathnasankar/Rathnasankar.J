import requests
import json
import random
import time 
Api_key = "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"
City = "YourCity"
Country = "YourCountry"

APIurl="http://api.openweathermap.org/data/2.5/air_pollution?lat=0&lon=0&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
   
    Air_quality = data["list"][0]["main"]
    
    print(f"Air Quality in {city}, {country}:")
    print(f" - AQI (Air Quality Index): {air_quality[‘aqi’]}")
    print(f" – Particulate Matter (PM2.5): {air_quality[‘pm2_5']} µg/m³")
    print(f" – Particulate Matter (PM10): {air_quality[‘pm10’]} µg/m³")
    print(f" – Carbon Monoxide (CO): {air_quality[‘co’]} µg/m³")
    print(f" – Nitrogen Dioxide (NO2): {air_quality[‘no2’]} µg/m³")
    print(f" – Ozone (O3): {air_quality[‘o3’]} µg/m³")
    print(f" – Sulfur Dioxide (SO2): {air_quality[‘so2’]} µg/m³")
class AirQualityMonitor:
    def __init__(self, location):
        self.location = location
        self.pm25 = 0
        self.pm10 = 0

    def measure_air_quality(self):
        self.pm25 = random.uniform(0, 100)
        Self.pm10 = random.uniform(0, 150)

    def display_data(self):
        print(f"Location: {self.location}")
        print(f"PM2.5: {self.pm25} µg/m³")
        print(f"PM10: {self.pm10} µg/m³")
        print("----------------------------")

if __name__ == "__main__":
    outdoor_sensor = AirQualityMonitor("Outdoor Sensor")
    indoor_sensor = AirQualityMonitor("Indoor Sensor")

    while True:
        outdoor_sensor.measure_air_quality()
        indoor_sensor.measure_air_quality()

        outdoor_sensor.display_data()
        indoor_sensor.display_data()

        # Simulate data collection every 5 seconds
        time.sleep(5)
else:
    print("Failed to retrieve air quality data")
def air_quality(aqi):
    if 0 <= aqi <= 50:
        return "Good"
    elif 51 <= aqi <= 100:
        return "Moderate"
    elif 101 <= aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif 151 <= aqi <= 200:
        return "Unhealthy"
    else:
        return "Hazardous"

Aqi_value = 75  
Result = air_quality(aqi_value)
print(f"The air quality is {result}")

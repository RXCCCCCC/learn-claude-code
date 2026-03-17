#!/usr/bin/env python3
"""weather_server.py - MCP server for weather data"""

import json
import httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("weather-server")

@server.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city.
    
    Args:
        city: City name to get weather for
    """
    try:
        # Note: You'll need to get a real API key from weatherapi.com
        # This is a placeholder implementation
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"https://api.weatherapi.com/v1/current.json",
                params={"key": "YOUR_API_KEY_HERE", "q": city}
            )
            
            if resp.status_code == 200:
                data = resp.json()
                weather_info = {
                    "city": data["location"]["name"],
                    "country": data["location"]["country"],
                    "temperature_c": data["current"]["temp_c"],
                    "temperature_f": data["current"]["temp_f"],
                    "condition": data["current"]["condition"]["text"],
                    "wind_kph": data["current"]["wind_kph"],
                    "humidity": data["current"]["humidity"],
                    "last_updated": data["current"]["last_updated"]
                }
                return json.dumps(weather_info, indent=2)
            else:
                return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error getting weather: {str(e)}"

@server.tool()
async def get_weather_forecast(city: str, days: int = 3) -> str:
    """Get weather forecast for a city.
    
    Args:
        city: City name to get forecast for
        days: Number of days to forecast (1-10, default: 3)
    """
    try:
        if days < 1 or days > 10:
            return "Error: Days must be between 1 and 10"
        
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"https://api.weatherapi.com/v1/forecast.json",
                params={"key": "YOUR_API_KEY_HERE", "q": city, "days": days}
            )
            
            if resp.status_code == 200:
                data = resp.json()
                forecast = []
                
                for day in data["forecast"]["forecastday"]:
                    forecast_data = {
                        "date": day["date"],
                        "max_temp_c": day["day"]["maxtemp_c"],
                        "min_temp_c": day["day"]["mintemp_c"],
                        "avg_temp_c": day["day"]["avgtemp_c"],
                        "condition": day["day"]["condition"]["text"],
                        "rain_chance": day["day"]["daily_chance_of_rain"],
                        "sun_hours": day["day"]["sunhours"]
                    }
                    forecast.append(forecast_data)
                
                result = {
                    "city": data["location"]["name"],
                    "country": data["location"]["country"],
                    "forecast": forecast
                }
                return json.dumps(result, indent=2)
            else:
                return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error getting forecast: {str(e)}"

# Run server
async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
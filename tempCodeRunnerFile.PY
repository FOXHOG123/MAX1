
        #TEMPERATURE AND WEATHER AND LOCATION............
#  elif "temperature" in query:
#             # Use Google Maps Geocoding to find location based on user query:

#             location = gmaps_client.geocode(query)
#             if location:
#                 # Extract coordinates from the first result:

#                 latitude = location[0]["geometry"]["location"]["lat"]
#                 longitude = location[0]["geometry"]["location"]["lng"]

#                 # Use OpenWeatherMap API to fetch weather data:

#                 weather_data = ow_client.weather_at_coords(latitude, longitude)
#                 temperature = weather_data.main["temp"]
#                 weather_description = weather_data.weather[0]["main"]

#                 # Speak the temperature and weather description:

#                 speak(f"In {query}, the temperature is currently {temperature:.1f}°C and the weather is {weather_description}.")
#             else:
#                 speak(f"Sorry, I couldn't find any location information for your query.")

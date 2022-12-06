import customtkinter
import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "32d05524b45767a93493ae180c5cde16"

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title('Weather App')
root.geometry('500x350')

CITY = "Kiev"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

temp_kelvin = response ["main"] ["temp"]
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response ["main"] ["feels_like"]
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humidity = response ["main"] ["humidity"]
description = response ["weather"] [0] ["description"]
wind_speed = response ["wind"]["speed"]
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']) 
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']) 

data1 = (f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
data2 = (f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
data3 = (f"Humidity in {CITY}: {humidity}%")
data4 = (f"Wind speed in {CITY}: {wind_speed:.2f}m/s")
data5 = (f"General weather in {CITY}: {description}")
data6 = (f"Sun rises in {CITY} at {sunrise_time} local time")
data7 = (f"Sun sets in {CITY} at {sunset_time} local time")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text=[CITY], font = ('Roboto', 30))
label.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text=[data2], font = ('Roboto', 16))
label2.pack(pady=12, padx=10)

label3 = customtkinter.CTkLabel(master=frame, text=[data3], font = ('Roboto', 16))
label3.pack(pady=12, padx=10)

label4 = customtkinter.CTkLabel(master=frame, text=[data4], font = ('Roboto', 16))
label4.pack(pady=12, padx=10)

label5 = customtkinter.CTkLabel(master=frame, text=[data5], font = ('Roboto', 16))
label5.pack(pady=12, padx=10)

label6 = customtkinter.CTkLabel(master=frame, text=[data6], font = ('Roboto', 16))
label6.pack(pady=12, padx=10)

label7 = customtkinter.CTkLabel(master=frame, text=[data7], font = ('Roboto', 16))
label7.pack(pady=12, padx=10)

root.mainloop()
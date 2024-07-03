import streamlit as st
import requests
from datetime import datetime


def get_weather(city):
    api_key = "d374b0a46ff3fd614ed6c7e315287160"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "ro"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        timestamp = data["dt"]
        local_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return weather_description, temperature, humidity, wind_speed, pressure, local_time
    else:
        return None, None, None, None, None, None


def main():
    st.title("Prognoza Meteo")

    # Bara laterală (stânga)
    with st.sidebar:
        with st.form(key="weather_form"):
            city_name = st.text_input("Introdu orașul dorit:")
            submit_button = st.form_submit_button(label="Verifică vremea")

    # Rezultate (mijloc)
    if submit_button:
        weather_description, temperature, humidity, wind_speed, pressure, local_time = get_weather(city_name)
        if weather_description and temperature and humidity:
            st.write(f"În {city_name.capitalize()} este {weather_description} "
                     f"și temperatura este de {temperature:.1f} °C.")
            st.write(f"Umiditatea este de {humidity} %.")
            st.write(f"Viteza vântului este de {wind_speed} m/s.")
            st.write(f"Presiunea atmosferică este de {pressure} hPa.")
            st.write(f"Data și ora locală: {local_time}.")
        else:
            st.write("Nu am putut găsi informații despre vreme pentru orașul introdus.")


if __name__ == "__main__":
    main()

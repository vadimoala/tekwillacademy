import streamlit as st
import requests
import folium
from streamlit_folium import folium_static



def get_weather(city):
    api_key = "d374b0a46ff3fd614ed6c7e315287160"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        coordinates = data["coord"]
        return weather_description, temperature, coordinates
    else:
        return None, None, None


def main():
    st.title("Vremea")
    city_name = st.text_input("Introdu orasul dorit:")

    if st.button("Verifică vremea"):
        weather_description, temperature, coordinates = get_weather(city_name)
        if weather_description and temperature and coordinates:
            st.write(f"În {city_name} este {weather_description} și temperatura este de {temperature:.1f} °C.")





if __name__ == "__main__":
    main()
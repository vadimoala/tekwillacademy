import streamlit as st
import requests
from streamlit_folium import folium_static
import folium



weather_icons = {
    "cer senin": "https://img.icons8.com/color/96/000000/sun--v1.png",
    "cer acoperit de nori": "https://img.icons8.com/color/96/000000/clouds.png",
    "ploaie ușoară": "https://img.icons8.com/color/96/000000/rain--v1.png",
    "ploaie": "https://img.icons8.com/color/96/000000/heavy-rain.png",
    "furtună": "https://img.icons8.com/color/96/000000/storm.png",
    "ninsoare": "https://img.icons8.com/color/96/000000/snow.png",
    "cețos": "https://img.icons8.com/color/96/000000/fog-day.png",
    "nori împrăștiați": "https://img.icons8.com/color/96/000000/cloud-computing.png",
    "dezgheț": "https://img.icons8.com/color/96/000000/temperature.png",
    "ceață": "https://img.icons8.com/color/96/000000/fog-night.png",
    "vânt": "https://img.icons8.com/color/96/000000/wind.png",
    "gheață": "https://img.icons8.com/color/96/000000/iceberg.png",
    "nori grei": "https://img.icons8.com/color/96/000000/thick-clouds.png",
    "ploaie deasă": "https://img.icons8.com/color/96/000000/rainfall.png"
}


with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

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
        coordinates = data["coord"]
        return weather_description, temperature, humidity, coordinates
    else:
        return None, None, None, None

def main():
    st.title("Vremea")
    city_name = st.text_input("Introdu orasul dorit:")

    if st.button("Verifica"):
        weather_description, temperature, umiditatea, coordinates = get_weather(city_name)
        if weather_description and temperature and umiditatea and coordinates:
            st.write(f"În {city_name.capitalize()} este {weather_description} "
                     f"și temperatura este de {temperature:.1f} °C\n"
                     f"\nIar umiditatea este de {umiditatea} %")

            if weather_description in weather_icons:
                st.image(weather_icons[weather_description], width=50)
            else:
                None


            map = folium.Map(location=[coordinates["lat"], coordinates["lon"]], zoom_start=15)
            folium.Marker([coordinates["lat"], coordinates["lon"]], popup=f"{city_name} - {temperature:.1f} °C").add_to(
                map)


            folium_static(map)
        else:
            st.write("Nu am putut obține datele meteo pentru acest oraș.")


if __name__ == "__main__":
    main()
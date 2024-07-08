import streamlit as st
import requests
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd


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

weather_messages = {
    "cer senin": "Este o zi frumoasă și însorită! Nu uita să te hidratezi bine.",
    "cer acoperit de nori": "Cerul este acoperit de nori. Poate ar fi bine să ai o jachetă la îndemână.",
    "ploaie ușoară": "Ploaie ușoară. Nu uita să iei o umbrelă cu tine.",
    "ploaie": "Ploaie. Asigură-te că ai o umbrelă și o haină impermeabilă.",
    "furtună": "Furtună. Este recomandat să stai în interior cât mai mult posibil.",
    "ninsoare": "Ninsoare. Îmbracă-te bine și ai grijă la drumuri alunecoase.",
    "cețos": "Este ceață. Condu cu atenție și fii precaut.",
    "nori împrăștiați": "Nori împrăștiați pe cer. O zi obișnuită, dar fii pregătit pentru orice.",
    "dezgheț": "Temperaturile cresc. Poate fi alunecos pe jos.",
    "ceață": "Ceață densă. Ai grijă când conduci.",
    "vânt": "Vânt puternic. Ai grijă la obiectele ușoare din jurul tău.",
    "gheață": "Gheață. Atenție mare la drumuri și trotuare.",
    "nori grei": "Nori grei. Poate începe să plouă în curând.",
    "ploaie deasă": "Ploaie deasă. Asigură-te că ai echipament de ploaie."
}

    # Extragere informatii generale
def get_weather(city):
    api_key = "d374b0a46ff3fd614ed6c7e315287160"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "ro"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        country = data["sys"]["country"]
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        timestamp = data["dt"]
        timezone_offset = data["timezone"]

        # Calcularea orei locale
        utc_time = datetime.utcfromtimestamp(timestamp)
        local_time = utc_time + timedelta(seconds=timezone_offset)
        local_time_str = local_time.strftime('%Y-%m-%d %H:%M:%S')

        return country, weather_description, temperature, humidity, wind_speed, pressure, local_time_str, data["coord"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None, None, None, None, None, None, None

    # Extragere informatii pentru grafic
def get_forecast(city):
    api_key = "d374b0a46ff3fd614ed6c7e315287160"
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "ro"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        forecast_data = []
        for entry in data["list"]:
            timestamp = entry["dt"]
            temperature = entry["main"]["temp"]
            description = entry["weather"][0]["description"]
            utc_time = datetime.utcfromtimestamp(timestamp)
            local_time = utc_time + timedelta(seconds=data["city"]["timezone"])
            forecast_data.append((local_time, temperature, description))

        return forecast_data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

    # Mesajul de afisare rezultate
def display_weather(city, country, description, temp, humidity, wind_speed, pressure, local_time):
    if description and temp is not None:
        st.markdown(f"<h2 style='color:white;'>{city.capitalize()}, {country}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'>În {city.capitalize()} este {description} și temperatura este de "
                    f"{temp:.1f} °C.</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'>Umiditatea este de {humidity}%.</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'>Viteza vântului este de {wind_speed} m/s.</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'>Presiunea atmosferică este de {pressure} hPa.</p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'>Data și ora locală: {local_time}.</p>", unsafe_allow_html=True)
        if description in weather_icons:
            st.image(weather_icons[description], width=50)
        if description in weather_messages:
            st.markdown(f"<p style='color:white;'>Nota: {weather_messages[description]}</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:white;'>Nu am putut găsi informații despre vreme pentru orașul introdus.</p>",
                    unsafe_allow_html=True)

    # Graficul pe 5 zile
def display_forecast(forecast_data):
    if forecast_data:
        dates = [entry[0] for entry in forecast_data]
        temperatures = [entry[1] for entry in forecast_data]
        descriptions = [entry[2] for entry in forecast_data]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=temperatures, mode='lines+markers', name='Temperature'))

        st.plotly_chart(fig)

        forecast_df = pd.DataFrame({
            "Date": dates,
            "Temperature (°C)": temperatures,
            "Description": descriptions
        })

        st.dataframe(forecast_df)

        csv = forecast_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Descarcă prognoza meteo",
            data=csv,
            file_name=f'forecast_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv',
            mime='text/csv',
        )

    else:
        st.markdown(
            "<p style='color:white;'>Nu am putut găsi informații despre prognoza meteo pentru orașul introdus.</p>",
            unsafe_allow_html=True)

    # Locatia
def display_map(city, coord):
    if coord:
        map_url = f"https://maps.google.com/maps?q={coord['lat']},{coord['lon']}&z=15&output=embed"
        st.markdown(f"<iframe src='{map_url}' width='100%' height='500'></iframe>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:white;'>Nu am putut găsi coordonatele pentru orașul introdus.</p>",
                    unsafe_allow_html=True)

    # Primul antet(numele paginii)
def main():
    st.markdown("<h1 style='color:white;'>Prognoza Meteo</h1>", unsafe_allow_html=True)

    # Imagine de fundal
    background_image_url = ("https://amateurphotographer.com/wp-content/uploads/sites/7/2023/03/"
                            "dmitry-bessonov-unsplash_1024px.jpg")
    st.markdown(
        f"""
           <style>
           .stApp {{
               background-image: url({background_image_url});
               background-size: cover;
               background-position: center;
               background-repeat: no-repeat;
               background-attachment: fixed;
           }}
           </style>
           """,
        unsafe_allow_html=True
    )

    # Bara Meniu
    with st.sidebar:
        with st.form(key="weather_form"):
            city_name = st.text_input("Introduceți orașul dorit:")
            submit_button = st.form_submit_button(label="Verifică Vremea")

    if submit_button:
        country, weather_description, temperature, humidity, wind_speed, pressure, local_time, coord = get_weather(city_name)
        display_weather(city_name, country, weather_description, temperature, humidity, wind_speed, pressure, local_time)
        forecast_data = get_forecast(city_name)
        display_forecast(forecast_data)
        display_map(city_name, coord)

if __name__ == "__main__":
    main()

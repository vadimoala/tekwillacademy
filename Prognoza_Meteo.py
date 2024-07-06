import streamlit as st
import requests
from datetime import datetime, timedelta


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


def get_weather(city):
    api_key = "d374b0a46ff3fd614ed6c7e315287160"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "ro"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
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

        return weather_description, temperature, humidity, wind_speed, pressure, local_time_str
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None, None, None, None, None, None

# Rezultatele (mesaj pe mijloc)
def display_weather(city, description, temp, humidity, wind_speed, pressure, local_time):
    if description and temp is not None:
        st.write(f"În {city.capitalize()} este {description} și temperatura este de {temp:.1f} °C.")
        st.write(f"Umiditatea este de {humidity}%.")
        st.write(f"Viteza vântului este de {wind_speed} m/s.")
        st.write(f"Presiunea atmosferică este de {pressure} hPa.")
        st.write(f"Data și ora locală: {local_time}.")
        if description in weather_icons:
            st.image(weather_icons[description], width=50)
        if description in weather_messages:
            st.write(f"Mesaj: {weather_messages[description]}")
    else:
        st.write("Nu am putut găsi informații despre vreme pentru orașul introdus.")

def main():
    st.title("Prognoza Meteo")

    # Imagine de fundal
    background_image_url = "https://amateurphotographer.com/wp-content/uploads/sites/7/2023/03/dmitry-bessonov-unsplash_1024px.jpg"
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
        weather_description, temperature, humidity, wind_speed, pressure, local_time = get_weather(city_name)
        display_weather(city_name, weather_description, temperature, humidity, wind_speed, pressure, local_time)

if __name__ == "__main__":
    main()

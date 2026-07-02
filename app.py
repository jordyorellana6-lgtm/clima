import streamlit as st
import pandas as pd
from api_clima import obtener_clima_actual, obtener_pronostico
from ciudades import CIUDADES

st.set_page_config(page_title="Clima API", layout="wide")

st.title("Aplicacion del clima con Open-Meteo")

ciudad = st.sidebar.selectbox("Seleccione una ciudad", list(CIUDADES.keys()))

latitud, longitud = CIUDADES[ciudad]

clima = obtener_clima_actual(latitud, longitud)

if clima:
    actual = clima["current"]

    st.header(f"Clima actual en {ciudad}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperatura", f"{actual['temperature_2m']} °C")
    col2.metric("Humedad", f"{actual['relative_humidity_2m']} %")
    col3.metric("Viento", f"{actual['wind_speed_10m']} km/h")

    pronostico = obtener_pronostico(latitud, longitud)

    if pronostico:
        horas = pronostico["hourly"]

        df = pd.DataFrame({
            "hora": horas["time"],
            "temperatura": horas["temperature_2m"],
            "humedad": horas["relative_humidity_2m"],
            "viento": horas["wind_speed_10m"]
        })

        st.subheader("Pronostico por hora")
        st.dataframe(df, use_container_width=True)

        st.line_chart(df.set_index("hora")["temperatura"])
    else:
        st.warning("No se pudo obtener el pronostico.")
else:
    st.error("No se pudo obtener el clima actual.")

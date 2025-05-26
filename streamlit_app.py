import streamlit as st
import requests
import os

st.set_page_config(page_title="ChirpQuest Mapa", layout="centered")

st.title("Mapa Interactivo de Aves de Colombia")
st.markdown("Este mapa muestra las ubicaciones de aves registradas en Xeno-Canto.")

country = st.text_input("País", value="Colombia")

if st.button("Generar Mapa"):
    with st.spinner("Consultando y generando mapa..."):
        response = requests.get(f"http://127.0.0.1:8000/birds/map?country={country}")
        if response.status_code == 200:
            with open("mapa_aves.html", "wb") as f:
                f.write(response.content)
            st.success("✅ Mapa generado correctamente.")
            st.components.v1.html(open("mapa_aves.html", "r").read(), height=600)
        else:
            st.error("❌ No se pudo generar el mapa. Intenta de nuevo.")
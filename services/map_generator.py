import folium
import webbrowser
import os

def generate_map(bird_data, filename="mapa_aves.html"):
    try:
        m = folium.Map(location=[4.5709, -74.2973], zoom_start=6)

        for bird in bird_data:
            try:
                lat = float(bird.get("lat", ""))
                lng = float(bird.get("lng", ""))
                folium.Marker(
                    location=[lat, lng],
                    popup=f"{bird['gen']} {bird['sp']} ({bird['en']})"
                ).add_to(m)
            except (ValueError, TypeError):
                continue

        m.save(filename)

        full_path = os.path.abspath(filename)
        print(f"✅ Mapa guardado en: {full_path}")

        # Abrir en navegador local
        webbrowser.open(f"file://{full_path}")

        return full_path

    except Exception as e:
        print("❌ Error generando mapa:", e)
        return None
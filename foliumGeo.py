import folium
import json

# Load the GeoJSON file
with open('china_provinces.geojson', encoding='utf-8') as f:
    china_geojson = json.load(f)

# Initialize a Folium map centered on China
m = folium.Map(location=[35.8617, 104.1954], zoom_start=4)

# Define a function to style the features
def style_function(feature):
    return {
        'fillColor': 'blue',
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5',
        'fillOpacity': 0.5,
    }

# Define a function to handle clicks on the provinces
def highlight_function(feature):
    return {
        'fillColor': 'yellow',
        'color': 'black',
        'weight': 3,
        'dashArray': '1, 1',
        'fillOpacity': 0.7,
    }

# Create a GeoJson object with the style and highlight functions
folium.GeoJson(
    china_geojson,
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['Province:']),
).add_to(m)

# Add a layer control to switch between different layers
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save('china_province_folium.html')



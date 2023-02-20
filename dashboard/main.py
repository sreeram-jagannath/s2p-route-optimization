import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static


def get_random_cities_list():
    # Load random city data
    # to generate new random cities, run the notebook "select_cities.ipynb"
    random_cities = pd.read_csv("../data/random_cities.csv")
    random_cities_list = random_cities.filter(["city", "lat", "lng", "color"]).values.tolist()
    return random_cities_list


def get_folium_map():

    # Create map
    m = folium.Map(location=[40, -95], zoom_start=4)

    # Add choropleth to the map
    folium.Choropleth(
        geo_data='../data/us-state-boundaries.geojson',
        line_opacity=0.8,
        fill_color="yellow",
        fill_opacity=0.1,
        highlight=True
    ).add_to(m)

    # plot all the cities
    for city, lat, long, clr in random_cities_list:
        folium.CircleMarker(
            [lat, long], 
            radius=10,
            fill=True,
            fill_color=clr,
            color=False,
            fill_opacity=0.5,
            tooltip=city,
        ).add_to(m)

    return m

if __name__ == "__main__":

    random_cities_list = get_random_cities_list()

    us_map = get_folium_map()

    # Display map in Streamlit app
    folium_static(us_map)

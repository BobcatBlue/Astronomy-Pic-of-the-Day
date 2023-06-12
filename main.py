import streamlit as st
import requests


API_KEY = "FvQx9wSyr98TgVS4u9wyGcArF63330QA4z5ob7lt"
url = "https://api.nasa.gov/planetary/apod?" \
          f"api_key={API_KEY}" \

# Get a dictionary of data from the APOD web API and store it in variable, "response"
response = requests.get(url)
data = response.json()

title = data['title']
image_url = data['url']
explanation = data['explanation']

# Download the Astronomy Image of the Day
image_data = requests.get(image_url).content
image_filepath = "APODimage.jpg"
with open(image_filepath, "wb") as daily_image:
    daily_image.write(image_data)

# Display the image title as the page title
st.markdown("<h1 style='text-align: center; color: black;'>"
            f"{title}</h1>", unsafe_allow_html=True)

# Render image on the page
st.image(image_filepath)

# Display the image description under the image
st.write(explanation)

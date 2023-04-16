import json
import streamlit as st
import plotly.express as px


# 1. Read the data from sample_data.json
with open("sample_data.json", "r") as f:
    data = json.load(f)


def read_data(data):

    readings = {"times": [], "values": []}

    for entry in data:
        if entry["sensor"] == "Microphone":
            readings["times"].append(entry["seconds_elapsed"])
            readings["values"].append(entry["dBFS"])

    return readings


def generate_plot(readings):

    # create the plot with plotly
    plot = px.line(readings, x="times", y="values")
    return plot


readings = read_data(data)

# streamlit app that displays the sensor data
st.title("Simple Streamlit Sensor App")

# create the plot and display it
if st.button("display data"):
    plot = generate_plot(readings)
    st.plotly_chart(plot)

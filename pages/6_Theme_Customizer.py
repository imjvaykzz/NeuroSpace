
import streamlit as st
from utils import theme_manager

st.set_page_config(page_title="Theme Customizer")

st.title("🎨 Theme Customizer")

theme = st.selectbox("Choose a theme:", ["Light", "Dark", "Custom"])

if theme == "Custom":
    primary_color = st.color_picker("Pick a primary color", "#4A90E2")
    bg_color = st.color_picker("Pick a background color", "#ffffff")
    text_color = st.color_picker("Pick a text color", "#000000")
else:
    primary_color = "#4A90E2" if theme == "Light" else "#ffffff"
    bg_color = "#ffffff" if theme == "Light" else "#0e1117"
    text_color = "#000000" if theme == "Light" else "#ffffff"

st.success(f"Theme applied: {theme}")
theme_manager.apply_theme(primary_color, bg_color, text_color)

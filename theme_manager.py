
import streamlit as st

def apply_theme(primary_color, background_color, text_color):
    custom_style = f"""
    <style>
        :root {{
            --primary-color: {primary_color};
            --background-color: {background_color};
            --text-color: {text_color};
        }}
        body {{
            background-color: var(--background-color);
            color: var(--text-color);
        }}
        .stButton>button {{
            background-color: var(--primary-color);
            color: white;
        }}
    </style>
    """
    st.markdown(custom_style, unsafe_allow_html=True)

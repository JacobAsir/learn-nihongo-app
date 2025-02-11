import streamlit as st

# Set page configuration as the first Streamlit command
st.set_page_config(
    page_title="Japanese Learning App",
    page_icon="🇯🇵",
    layout="wide"
)

# Define the navigation pages
pg = st.navigation([
    st.Page(page="nihongo.py", url_path='Learn_to_speak_Japanese'),
    st.Page(page="learn_kana.py", url_path='Learn_Kana'),
    st.Page(page="romaji_to_kana.py", url_path='Romaji_to_Kana'),
    st.Page(page="kana_to_romaji.py", url_path='Kana_to_Romaji')
])

# Add descriptions in the sidebar
st.sidebar.title("Descriptions")
st.sidebar.write("**Nihongo**: learn to speak Japanese.")
st.sidebar.write("**Learn Kana**: This page helps you learn Kana.")
st.sidebar.write("**Romaji to Kana**: Practice Kana writing!")
st.sidebar.write("**Kana to Romaji**: Practice Kana reading!")

# Run the navigation
pg.run()
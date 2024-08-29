import streamlit as st
import pandas as pd
import seaborn as sns
from streamlit_option_menu import option_menu

# Custom CSS to move sidebar to the right
st.markdown("""
    <style>
    .css-1aumxhk {
        position: fixed;
        right: 0;
        width: 200px;
        height: 100%;
        background-color: #f0f0f0;
        border-left: 1px solid #e0e0e0;
        padding: 10px;
    }
    .css-1aumxhk .stButton {
        margin-bottom: 10px;
    }
    </style>
    <div class="css-1aumxhk">
        <h3>Main Menu</h3>
        <button class="stButton" id="home">Home</button>
        <button class="stButton" id="projects">Projects</button>
        <button class="stButton" id="contact">Contact</button>
    </div>
    """, unsafe_allow_html=True)

# Main content area
st.title("Welcome to the App")
st.write("Select an option from the menu to see more details.")

# JavaScript to handle button clicks and update content
st.markdown("""
    <script>
    document.getElementById("home").onclick = function() {
        window.location.href = "?page=home";
    };
    document.getElementById("projects").onclick = function() {
        window.location.href = "?page=projects";
    };
    document.getElementById("contact").onclick = function() {
        window.location.href = "?page=contact";
    };
    </script>
    """, unsafe_allow_html=True)

# Read the page parameter from URL
page = st.experimental_get_query_params().get("page", ["home"])[0]

if page == "home":
    st.title("Home")
    st.header('Snowflake Healthcare App')
    
    my_catalog = sns.load_dataset('iris')

    st.dataframe(my_catalog)
    q1 = st.text_input('Write your query', '')
    st.button('Run Query')
    if not q1:
        st.error('Please write a query')
    else:
        st.dataframe(my_catalog)

elif page == "projects":
    st.title("Projects")
    st.write("Here are some projects.")

elif page == "contact":
    st.title("Contact")
    st.write("Contact information here.")

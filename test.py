# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import streamlit_option_menu
# from streamlit_option_menu import option_menu


# with st.sidebar:
#   selected = option_menu(
#     menu_title = "Main Menu",
#     options = ["Home","Projects","Contact"],
#     icons = ["house","book","envelope"],
#     menu_icon = "cast",
#     default_index = 0,

#   )
#   if selected == "Home":
#     st.title(f"You Have selected {selected}")
#     st.header('Snowflake Healthcare App')
    
#     my_catalog = sns.load_dataset('iris')

#     st.dataframe(my_catalog)
#     q1 = st.text_input('Write your query','')
#     st.button('Run Query')
#     if not q1:
#       st.error('Please write a query')
#     else:
#       st.dataframe(my_catalog)
#   if selected == "Projects":
#     st.title(f"You Have selected {selected}")
#   if selected == "Contact":
#     st.title(f"You Have selected {selected}")
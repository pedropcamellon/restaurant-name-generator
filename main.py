"""
Restaurant Name Generator app.
The user selects a cusine and gets a list of restaurant names that serve that cusine.
Also could generate a random menu items for that restaurant.
"""

import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.title("Restaruant Name Generator")

st.sidebar.header("This is my sidebar")

cuisine = st.sidebar.selectbox("Pick up a cusine", ("Mexican", "American", "Chinese"))

restaurant_name = st.text_input("Enter a restaurant name")

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)

    # Display restaurant name
    if restaurant_name:
        st.header(restaurant_name)
    else:
        st.header(response["restaurant_name"])

    # Display menu items
    menu_items = []

    try:
        print(response["food_items"])
        menu_items_raw = response["food_items"]
        menu_items_list = menu_items_raw.split(",")

        menu_items = menu_items_list

        # Truncate menu items to 3
        if len(menu_items) > 3:
            menu_items = menu_items[0:3]

    except KeyError:
        pass

    if len(menu_items) != 0:
        # Display menu
        st.write("Menu:")

        for item in menu_items:
            st.write("-", item)

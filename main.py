import streamlit as st
from generator import generate_restaurant_name


def main():
    st.set_page_config(
        page_title="Restaurant Name Generator",
        page_icon="🍽️",
    )

    st.title("🏪 Restaurant Name Generator")

    # Add a sidebar with information
    with st.sidebar:
        st.header("About")
        st.write("Generate unique restaurant names based on cuisine type using AI.")

    # Main content
    cuisines = [
        "Italian",
        "Mexican",
        "Chinese",
        "Indian",
        "Japanese",
        "American",
        "French",
        "Thai",
    ]
    cuisine = st.selectbox("Select a cuisine type:", cuisines)

    if st.button("Generate Restaurant Name", type="primary"):
        with st.spinner("Generating restaurant name..."):
            # Generate restaurant name
            restaurant_name = generate_restaurant_name(cuisine)

            if restaurant_name:
                st.header(restaurant_name)

            else:
                st.error("Failed to generate restaurant name. Please try again.")


if __name__ == "__main__":
    main()

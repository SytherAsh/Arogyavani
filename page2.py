import streamlit as st
from pages import home, about, contact  # Import your pages in the desired order

PAGES = {
    "Home": home,
    "About": about,
    "Contact": contact,
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()

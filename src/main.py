import streamlit as st

from streamlit_option_menu import option_menu
from components.simple_read import SimpleReadPage
from components.crud import CRUDPage
from components.simple_viz import SimpleVizPage

page_title="Hellofresh streamlit test"
page_icon=":coconut:"
layout="centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

def select_order_id(order_obj):
    st.session_state["selected_order"] = order_obj

def clear_order_id():
    if "selected_order" in st.session_state:
        del st.session_state["selected_order"]

# ===== Form code ======

if __name__ == "__main__":

    selected = option_menu(
        menu_title=None,
        options=["simple-read", "simple-viz", "crud"],
        orientation="horizontal"
    )

    match selected:
        case "simple-read":
            SimpleReadPage().render()
        case "simple-viz":
            SimpleVizPage().render()
        case "crud":
            CRUDPage().render()
        case other:
            st.write("Option not recognized")
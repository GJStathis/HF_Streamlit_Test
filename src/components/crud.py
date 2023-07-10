import streamlit as st
from utils.session_manager import SessionManager
from database.db_conn import DBConnection

class CRUDPage:

    def __init__(self):
        self.session_state = SessionManager
        self.db = DBConnection

        dummy_session_data = self.db.read_dummy_data()
        self.session_state.set("data", dummy_session_data)
        self.session_state.set("show_create", False)


    def _select_order_id(self, order_obj):
        self.session_state.update("selected_obj", order_obj)


    def _info_container_component(self, obj):
        with st.container():
            col1, col2 = st.columns(2)
            col1.write(f"name of sale: {obj['name']}")
            col2.write(f"price: {obj['price']}")
            col1.button(label="select", on_click=self._select_order_id, kwargs={"order_obj": obj}, key=obj["order_id"])


    def _update_selected_obj_component(self):
        if self.session_state.read("selected_obj"):
            current_obj: dict = self.session_state.read("selected_obj")

            st.text_input("name", current_obj.get("name"), key="order_name")
            st.text_input("price", current_obj.get("price"), key="order_price")

            col1, col2 = st.columns(2)

            col1.button("Update",
                on_click=self._update,
                kwargs={
                    "order_id": current_obj.get("order_id"), 
                    "name": self.session_state.read("order_name"),
                    "price": self.session_state.read("order_price")
                }
            )
            col2.button("Delete", 
                on_click=self._delete, 
                kwargs={"state_key": "data", "filter_key": "order_id", "filter_value": current_obj.get("order_id")}
            )


    def _create_obj_component(self):
        with st.container():
            st.text_input("name", key="new_order_name")
            st.text_input("price", key="new_order_price")

            col1, col2 = st.columns(2)

            col1.button("Create", on_click=self._create, kwargs={
                "name": self.session_state.read("new_order_name"),
                "price": self.session_state.read("new_order_price")
            })
            col2.button("Close", on_click=self.session_state.update, kwargs={"key": "show_create", "value": False})


    def _get_selected_obj_string(self):
        if self.session_state.read("selected_obj"):
            return self.session_state.read("selected_obj")["order_id"]

        return "nothing"


    def _delete(self, state_key, filter_key, filter_value):
        self.session_state.delete_state_value(state_key, filter_key, filter_value)
        self.db.delete_dummy_data(filter_value)
        self.session_state.clear("selected_obj")

    def _create(self, name, price):
        new_order_id = self.db.create_dummy_data(name, price)
        self.session_state.update("data", {"order_id": new_order_id, "name": name, "price": price})
        self.session_state.update("show_create", False)

    def _update(self, order_id, name, price):
        self.db.update_dummy_data(order_id, name, price)

        update_obj = {"order_id": order_id, "name": name, "price": price}

        self.session_state.update("data", update_obj, state_key="data", filter_key="order_id", filter_value=order_id)
        self.session_state.clear("selected_obj")


    def render(self):

        self._update_selected_obj_component()

        "---"

        col1, col2 = st.columns(2)

        col1.button(label="clear selected", on_click=self.session_state.clear, kwargs={"key": "selected_obj"})

        print(self.session_state.read("show_create"))        

        if self.session_state.read("show_create"):
            self._create_obj_component()
        else:
            col2.button("create new obj", on_click=self.session_state.update, kwargs={"key": "show_create", "value": True})
        
        "---"

        st.write(f"currently {self._get_selected_obj_string()} is selected")

        for obj in self.session_state.read("data"):
            self._info_container_component(obj)
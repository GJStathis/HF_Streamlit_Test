import streamlit as st

class SessionManager:

    @staticmethod
    def clear(key):
        try:
            del st.session_state[key]
        except KeyError:
            print("Key not found in session doing nothing...")


    @staticmethod
    def read(key):
        try:
            return st.session_state[key]
        except KeyError:
            return None


    @staticmethod
    def set(key, value):
        if key not in st.session_state:
            st.session_state[key] = value
        else:
            print("ERROR: value is already in session state. If trying to change use the update method instead")

    
    @staticmethod
    def delete_state_value(state_key, filter_key, filter_value):
        for idx in range(len(st.session_state[state_key])):
            if st.session_state[state_key][idx][filter_key] == filter_value:
                del st.session_state[state_key][idx]
                break


    @staticmethod
    def update(key, value, state_key=None, filter_key=None, filter_value=None):
        if state_key and filter_key and filter_value:
            for idx in range(len(st.session_state[state_key])):
                if st.session_state[state_key][idx][filter_key] == filter_value:
                    st.session_state[state_key][idx] = value
                    break
        elif type(st.session_state.get(key)) == list:
            st.session_state[key].append(value)
        else:
            st.session_state.update({key: value})
    
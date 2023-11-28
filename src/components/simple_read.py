import calendar, os
import pandas as pd
import streamlit as st
from utils.session_manager import SessionManager

class SimpleReadPage:

    def __init__(self):
        self.session_state = SessionManager


    def _create_simple_read_page(self):
        months = list(calendar.month_name[1:])

        with st.form("show_subset_sales_data"):
            col1, col2 = st.columns(2)

            col1.selectbox("Year", [2019], key="sales_year")
            col2.selectbox("Month", months, key="sales_month")

            "--------"

            st.number_input("Number of rows", min_value=10, format="%i", step=10, key="sales_subset_size")

            "---"

            submit = st.form_submit_button("Show Data")

            if submit:
                # access data df and display 
                st.write(f"Showing {self.session_state.read('sales_subset_size')} rows")
                #st.write(f"Showing {self.session_state.read('sales_subset_size')} rows from file Sales_{self.session_state.read('sales_month')}_{self.session_state.read('sales_year')}.csv")

                file_name = f"Sales_{self.session_state.read('sales_month')}_{self.session_state.read('sales_year')}.csv"
                sales_df = pd.read_csv(os.path.join(os.getcwd(), f"data/sales_data/{file_name}"), nrows=self.session_state.read('sales_subset_size'))

                st.dataframe(sales_df)
        
    def render(self):
        self._create_simple_read_page()

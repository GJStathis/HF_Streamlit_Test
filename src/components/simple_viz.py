import calendar, os
import streamlit as st
import pandas as pd

from utils.session_manager import SessionManager

class SimpleVizPage:

    def __init__(self):
        self.session_state = SessionManager

    def _total_sales_and_quant_display(self, total_sales, total_quantity):
        with st.container():
            col1, col2 = st.columns(2)

            col1.metric("total value of sales", f"${total_sales}")
            col2.metric("total number of sales", total_quantity)


    def render(self):
        with st.form("show_data_viz"):
            months = list(calendar.month_name[1:])
            col1, col2 = st.columns(2)

            col1.selectbox("Sales Month", months, key="sales_viz_month")
            col2.selectbox("Sales Year", [2019], key="sales_viz_year")

            submit = st.form_submit_button("Viz")

            if submit:
                file_name = f"Sales_{self.session_state.read('sales_viz_month')}_{self.session_state.read('sales_viz_year')}.csv"
                sales_df = pd.read_csv(os.path.join(os.getcwd(), f"data/sales_data/{file_name}")).fillna(0)

                sales_df = sales_df[sales_df["Quantity Ordered"] != "Quantity Ordered"]
                sales_df = sales_df[sales_df["Product"] != 0]

                sales_df["Quantity Ordered"] = sales_df["Quantity Ordered"].astype(float)
                sales_df["Price Each"] = sales_df["Price Each"].astype(float)

                total_quantity = sales_df[["Quantity Ordered"]].sum()
                total_sales = sales_df[["Price Each"]].sum()

                self._total_sales_and_quant_display(round(total_sales.iloc[0],2), total_quantity.iloc[0])

                "---"


                st.write("Top 5 Sales")
                grouped_sales_df = sales_df[["Product", "Quantity Ordered", "Price Each"]].groupby(by="Product").sum().reset_index()
                grouped_sales_df = grouped_sales_df.rename(columns={"Product": 'Product', "Quantity Ordered": 'Quantity', "Price Each": 'Price'})
                grouped_sales_df = grouped_sales_df.sort_values(by="Quantity", ascending=False)
                st.dataframe(grouped_sales_df.head(5), hide_index=True)


                "---"

                dummy_lat_vals = [
                    [34.0522, -118.2437], # LA
                    [40.7128, -74.0060], # NYC
                    [41.8781, -87.6298], # Chicago
                    [47.6062, -122.3321], # seattle
                    [37.7749, -122.4194] # San fran
                ]

                df = pd.DataFrame(dummy_lat_vals, columns=['lat', 'lon'])

                st.map(df)



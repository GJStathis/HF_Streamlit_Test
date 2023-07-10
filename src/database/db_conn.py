import sqlite3, os

DATABASE_CONNECTION_STRING = os.path.join(os.getcwd(), "./database/hf_streamlit_test.db")

class DBConnection:

    @staticmethod
    def read_dummy_data():
        with sqlite3.connect(DATABASE_CONNECTION_STRING) as conn:
            result = conn.execute("select order_id, name, price from dummy_data")

            res_list = result.fetchall()

            return_val = []

            for tup in res_list:
                return_val.append({
                    "order_id": tup[0],
                    "name": tup[1],
                    "price": tup[2]
                })

            return return_val


    @staticmethod
    def delete_dummy_data(order_id):
        with sqlite3.connect(DATABASE_CONNECTION_STRING) as conn:
            conn.execute("DELETE FROM dummy_data WHERE order_id = ?", (order_id,))


    @staticmethod
    def create_dummy_data(name, price):
        with sqlite3.connect(DATABASE_CONNECTION_STRING) as conn:
            res = conn.execute("INSERT INTO dummy_data (name, price) VALUES (?, ?) RETURNING order_id", (name, price))
            
            val = res.fetchone()
            if val:
                return val[0]

    
    @staticmethod
    def update_dummy_data(order_id, name, price):
        with sqlite3.connect(DATABASE_CONNECTION_STRING) as conn:
            conn.execute("UPDATE dummy_data SET name=?, price=? WHERE order_id=?", (name, price, order_id))

        


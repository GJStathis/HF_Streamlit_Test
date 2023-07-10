import sqlite3

def create_tables():
    with sqlite3.connect("hf_streamlit_test.db") as conn:
        conn.execute("""
            CREATE TABLE dummy_data(
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT, 
                    price
                )
        """)


def insert_init_data():
    with sqlite3.connect("hf_streamlit_test.db") as conn:
        conn.execute("""
            INSERT INTO dummy_data (name, price) VALUES
                ('test', 20.1),
                ('test2', 20.23)
        """)


if __name__ == "__main__":
    create_tables()
    insert_init_data()
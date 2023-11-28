# from geopy.geocoders import Nominatim

# locator = Nominatim(user_agent="myGeocoder")
# location = locator.geocode("682 Chestnut St, Boston, MA, 02215")

# print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))


import pandas as pd

df = pd.read_csv("./src/data/sales_data/Sales_January_2019.csv")

col = ["Lane", "brand", "box_count", "cpt delta", "cpt_date", "scan amount"]

print(df)
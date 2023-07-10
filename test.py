from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("682 Chestnut St, Boston, MA, 02215")

print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

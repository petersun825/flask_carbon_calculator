import requests
import geocoder
from secrets import co2_key, nrel_key

co2_url='https://api.co2signal.com/v1/latest?{}{}&lon={}&lat={}'

elec_url = 'https://developer.nrel.gov/api/utility_rates/v3.json?api_key={}&lat={}&lon={}'
	
def get_emissions(user_address):
	g = geocoder.arcgis(user_address)

	lat=str(g.latlng[0])
	lng=str(g.latlng[1])
	request_url = co2_url.format('auth-token=', co2_key, lng, lat)
	print('request_url:', request_url)
	response=requests.get(request_url)
	response_json = response.json()
	return response_json

def get_electricity(user_address):
	g = geocoder.arcgis(user_address)

	lat=str(g.latlng[0])
	lng=str(g.latlng[1])
	request_url = elec_url.format(nrel_key, lng, lat)
	print(request_url)
	response = response=requests.get(request_url)
	response_json = response.json()
	return response_json


# curl 'https://api.co2signal.com/v1/latest?lon=6.8770394&lat=45.9162776'
#   -H 'auth-token: myapitoken'
import geocoder, csv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

locations=[]

# create a class for location
class gps():
	def __init__(self, address=''):
		self.address=address
	
	def get_latlng(self):
		g = geocoder.arcgis(self.address)
		lat=str(g.latlng[0])
		lng=str(g.latlng[1])
		#convert latitude & longtitude into str and encapsulate with () 
		return "{0},{1}".format(lat,lng)

def get_latlng(address):

		g = geocoder.arcgis(address)
		lat=str("{:.6f}0000".format(g.latlng[0]))
		lng=str("{:.6f}0000".format(g.latlng[1]))
		latlng_formatted = '{},{}'.format(lat,lng)
		
		return latlng_formatted	






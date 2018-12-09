import csv
from CO2_app import get_emissions, get_electricity
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



#import postgres filepath from config file
from config import boston_permits_postgres
app = Flask(__name__)

#way to tell DB how to connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = boston_permits_postgres

# 'sqlite:////tmp/test.db'#avoid warming message in console everytime something changes in DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class cars():
    def __init__(self, miles=1, mpg=1):
        self.miles = miles
        self.mpg = mpg

    def emissions(self):
        #emissions is miles divided by miles per gallon, then multiplied by 18.9 lbs per gallon of gasoline and divided by 2000 to get tons
        #source: https://www.eia.gov/tools/faqs/faq.php?id=307&t=11
        emission = float(self.miles) / float(self.mpg) * 18.9 / 2000
        return emission


class PermitsException(Exception):
	pass

#get utility information
def utility_rates(utility_data):
    residential_rate = utility_data['outputs']['residential']

#get emissions intensity and fossil fuel percentage
def carbon_intensity(emission_data):
    data = emission_data['data']
    carbon = data['carbonIntensity']
    return carbon

#get fossil percentage from API data
def fossil_percentage(emission_data):
    data = emission_data['data']
    fossil = data['fossilFuelPercentage']
    return fossil

#reduce the number of decimals
def reduce_decimals(info):
    num = str("{:.2f}".format(info))
    return num

#main page
@app.route('/', methods = ['GET','POST'])
def location():
    return render_template('location.html')

@app.route('/search_location', methods = ['GET', 'POST'])
def search_location():
    #take the user input from page and assign to variables
    address = request.form['address']
    elec_usage = request.form['elec']
    miles = request.form['miles']
    mpg = request.form['mpg']

    #get emission data and assign to variable
    emission = get_emissions(address)
    
    #fake data if api limit exceeded
    emission = {
    "_disclaimer": "This data is the exclusive property of Tomorrow and/or related parties. If you're in doubt about your rights to use this data, please contact hello@tmrow.com",
    "status": "ok",
    "countryCode": "US-NEISO",
    "data": {
    "carbonIntensity": 231.64984189500765,
    "fossilFuelPercentage": 41.658827150418496
    },
    "units": {
    "carbonIntensity": "gCO2eq/kWh"
    }
    }

    #electricity emissions
    if emission['status']=='ok':
        #round results to 2 decimal places for legibility
        carbon = round(carbon_intensity(emission), 2)
        fossil = round(fossil_percentage(emission), 2)
    else:
        return jsonify('error')
    
    #obtain electricity emissions
    

    #multiply per kWh of electricity usage by grams of carbon emission per kWh convert to tons of carbon per year
    per_year_carbon = float(carbon) * float(elec_usage) * 12 / 907185
    #reduce to 2 decimals
    per_year_carbon = round(per_year_carbon, 2)

    #instantiate average car
    normal_car = cars(miles, mpg)
    normal_car_emission = round(normal_car.emissions(), 2)
    #tesla gets 135 mpg equivalent
    tesla_emission = cars(miles, 135).emissions()
    tesla_emission = round(tesla_emission, 2)

    emission_saved = normal_car_emission - tesla_emission 
    return render_template('display.html', carbon=carbon, fossil = fossil, per_year_carbon = per_year_carbon, normal_car_emission = normal_car_emission,  emission_saved = emission_saved)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
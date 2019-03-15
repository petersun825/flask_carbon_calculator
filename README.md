# flask_carbon_calculator
converts electricity to carbon emissions calculator.  Uses python handle the calculations and some html/bootstrap on the front end to capture user data.  Convert users input location into coordinates to send to API go get carbon intensity.  Data from API is then fed back to the backend and calculation is done to figure out carbon output.  The output is displayed on the front end.  Compares your gasoline powered car with an electricity powered tesla vehicle, the tesla vehicle takes into account how "clean" or "dirty" the grid is.  

Tech Stack
Python Flask
HTML, CSS, Bootstrap

###Required:
python 3 or above, google chrome or other modern web browser.

###Installation - For OS only
#Required packages in terminal:
Install Flask , geocoder, psycopg2, wekzeug in terminal
- pip install flask
- pip install geocoder
- pip install psycopg2
- pip install werkzeug

###API Key
- Go to: https://www.co2signal.com/
- Sign up to receive the API key.
- create a file named secrets.py 
- Copy paste API key inside the file and assign it to variable 'co2_key'

Download the git library

In terminal, run:
- python location.py

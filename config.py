
import os


#create a class for secret key for use session
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

#db for users
local_user_postgres='postgresql://{username}:{pw}@{url}/{db}'.format(username='postgres',pw='pdc301',url='localhost:5432',db='testdb')

#db for permit data
boston_permits_postgres = 'postgresql://{username}:{pw}@{url}/{db}'.format(username='postgres',pw='pdc301',url='localhost:5432',db='boston_permits')

#heroku postgres
web_postgres='postgres://xkcarxgzffpknz:c61bf5c9453445a2d18957ed28a4c919230ce9f1ec4d7b1daa0e73a62d180012@ec2-54-235-193-0.compute-1.amazonaws.com:5432/db5dv2uouvh6ed'


# Coronavirus support administration panel

To get this started you can use docker-compose

`Git clone https://github.com/teedee22/coronaSupport.git`

`cd coronaSupport`

`docker-compose up`

navigate to http://localhost:8000

Alternatively, using python 3.8 inside a virtual environment:

`pip install -r requirements.txt`

`python manage.py runserver`

navigate to localhost:8000

## Airtable API Access
In order to access Airtable you must add your API key to your environment variables as AIRTABLE_API_KEY.

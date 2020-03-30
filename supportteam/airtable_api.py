#airtable_api.py
#This module is for all things Airtable API

from airtable import Airtable

BASE_ID = "apphZUrJD3wD17sah"

def getVolunteersTable(**kwargs):
	maxRecords = kwargs.get('maxRecords', 40)
	AT = Airtable(BASE_ID, 'Volunteers')
	return AT.get_all(maxRecords = maxRecords)

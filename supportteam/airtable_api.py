#airtable_api.py
#This module is for all things Airtable API
#Eventually airtable logic will be replaced with database logic

# @Author SkylerJEhly

from airtable import Airtable

BASE_ID = "appjQnAKA4I4B2ARq"

# VOLUNTEERS TABLE #
def getVolunteersTable(**kwargs):
	"""
	Retrieves all records of Volunteers table repetively and returns a single list

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view.
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by. Default order is by Staus and then Name
		formula: Airtable formula

	Returns: 
		A list of all records of Volunteers table

	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', None)
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', ['Status', 'Name'])
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'Volunteers')
	return AT.get_all(max_records = max_records, view=view, fields=fields, sort=sort, formula=formula)

def getVolunteerRecord(record_id):
	"""
	Retrieves a single record from Volunteers table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		A single record from Volunteers table

	"""


	AT = Airtable(BASE_ID, 'Volunteers')
	return AT.get(record_id)

def deleteVolunteerRecord(record_id):
	"""
	Deletes a single record from Volunteers table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		The deleted record

	"""

	AT = Airtable(BASE_ID, 'Volunteers')
	return AT.delete(record_id)

def getVolunteersIter(**kwargs):
	"""
	Returns iterator with lists in batches according to pageSize for Volunteers table

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view.
		page_size(int, optional): The number of records returned in each request. Must be less than or equal to 100. Default is 100.
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by. Default order is by Staus and then Name
		formula: Airtable formula

	Returns: 
		An iterator with lists in batches according to pageSize for Volunteers table

	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', None)
	page_size = kwargs.get('page_size', 100)
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', ['Status', 'Name'])
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'Volunteers')
	return AT.get_iter(max_records = max_records, view=view, page_size=page_size, fields=fields, sort=sort, formula=formula)


def updateVolunteerRecord(record_id, fields, **kwargs):
	"""
	Updates a record in Volunteers table by its record id. Only Fields passed are updated, the rest are left as is.

	Parameters:
		record_id(int): Airtable record id
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	AT = Airtable(BASE_ID, 'Volunteers')
	return AT.update(record_id, fields, typecast)

def updateVolunteerRecordByField(field_name, field_value, fields, **kwargs):
	"""
	Updates the first record in Volunteers table to match field name and value. Only Fields passed are updated, the rest are left as is.

	Parameters:
		field_name(str): Name of field to match (column name).
		field_value(str): Value of field to match.
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False
		view(str, optional): The name or ID of a view.
		sort(list, optional) List of fields to sort by. Default order is Status and Name

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	view = kwargs.get('view', None)
	sort = kwargs.get('sort', ['Status', 'Name'])
	AT = Airtable(BASE_ID, 'Volunteers')


# OFFERS TABLE #
def getOffersTable(**kwargs):
	"""
	Retrieves all records of Offers table repetively and returns a single list

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view.
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by. Default order is by Request number
		formula: Airtable formula

	Returns: 
		A list of all records of Offers table

	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', None)
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', ['Request number'])
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'Offers')
	return AT.get_all(max_records = max_records, view=view, fields=fields, sort=sort, formula=formula)

def getOfferRecord(record_id):
	"""
	Retrieves a single record from Offers table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		A single record from Offers table

	"""

	AT = Airtable(BASE_ID, 'Offers')
	return AT.get(record_id)

def deleteOfferRecord(record_id):
	"""
	Deletes a single record from Offers table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		The deleted record

	"""

	AT = Airtable(BASE_ID, 'Offers')
	return AT.delete(record_id)

# Returns iterator with lists in batches according to pageSize
def getOffersIter(**kwargs):
	"""
	Returns iterator with lists in batches according to pageSize for Offers table

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view.
		page_size(int, optional): The number of records returned in each request. Must be less than or equal to 100. Default is 100.
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by. Default order is by Request number
		formula: Airtable formula

	Returns: 
		An iterator with lists in batches according to pageSize for Offers table

	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', None)
	page_size = kwargs.get('page_size', 100)
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', ['Request number'])
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'Offers')
	return AT.get_iter(max_records = max_records, view=view, page_size=page_size, fields=fields, sort=sort, formula=formula)


def updateOfferRecord(record_id, fields, **kwargs):
	"""
	Updates a record in Offers table by its record id. Only Fields passed are updated, the rest are left as is.

	Parameters:
		record_id(int): Airtable record id
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	AT = Airtable(BASE_ID, 'Offers')
	return AT.update(record_id, fields, typecast)

def updateOfferRecordByField(field_name, field_value, fields, **kwargs):
	"""
	Updates the first record in Offers table to match field name and value. Only Fields passed are updated, the rest are left as is.

	Parameters:
		field_name(str): Name of field to match (column name).
		field_value(str): Value of field to match.
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False
		view(str, optional): The name or ID of a view.
		sort(list, optional) List of fields to sort by. Default order is by Request number

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	view = kwargs.get('view', None)
	sort = kwargs.get('sort', ['Request number'])
	AT = Airtable(BASE_ID, 'Offers')


# REQUESTS TABLE #
def getRequestsTable(**kwargs):
	"""
	Retrieves all records of Requests table repetively and returns a single list

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view.
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by. Default order is by Status (asc) and Request number (desc)
		formula: Airtable formula

	Returns: 
		A list of all records of Requests table

	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', None)
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', ['Status', '-Request number'])
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'Requests')
	return AT.get_all(max_records = max_records, view=view, fields=fields, sort=sort, formula=formula)

def getRequestRecord(record_id):
	"""
	Retrieves a single record from Requests table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		A single record from Requests table

	"""

	AT = Airtable(BASE_ID, 'Requests')
	return AT.get(record_id)

def deleteRequestRecord(record_id):
	"""
	Deletes a single record from Requests table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		The deleted record

	"""

	AT = Airtable(BASE_ID, 'Requests')
	return AT.delete(record_id)

# Returns iterator with lists in batches according to pageSize
def getRequestsIter(**kwargs):
	"""
	Returns iterator with lists in batches according to pageSize for Requests table

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view.
		page_size(int, optional): The number of records returned in each request. Must be less than or equal to 100. Default is 100.
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by. Default order is by Status (asc) and Request number (desc)
		formula: Airtable formula

	Returns: 
		An iterator with lists in batches according to pageSize for Requests table
		
	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', None)
	page_size = kwargs.get('page_size', 100)
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', ['Status', '-Request number'])
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'Requests')
	return AT.get_iter(max_records = max_records, view=view, page_size=page_size, fields=fields, sort=sort, formula=formula)

def updateRequestRecord(record_id, fields, **kwargs):
	"""
	Updates a record in Requests table by its record id. Only Fields passed are updated, the rest are left as is.

	Parameters:
		record_id(int): Airtable record id
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	AT = Airtable(BASE_ID, 'Requests')
	return AT.update(record_id, fields, typecast)

def updateRequestRecordByField(field_name, field_value, fields, **kwargs):
	"""
	Updates the first record in Requests table to match field name and value. Only Fields passed are updated, the rest are left as is.

	Parameters:
		field_name(str): Name of field to match (column name).
		field_value(str): Value of field to match.
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False
		view(str, optional): The name or ID of a view.
		sort(list, optional) List of fields to sort by. Default order is by Status (asc) and Request number (desc)

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	view = kwargs.get('view', None)
	sort = kwargs.get('sort', ['Status', '-Request number'])
	AT = Airtable(BASE_ID, 'Requests')


# SMS TABLE #
# Uses triage view as default
def getSMSTable(**kwargs):
	"""
	Retrieves all records of SMS all table repetively and returns a single list

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view. Default is SMS triage
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by.
		formula: Airtable formula

	Returns: 
		A list of all records of SMS all table

	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', 'SMS triage')
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', None)
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'SMS all')
	return AT.get_all(max_records = max_records, view=view, fields=fields, sort=sort, formula=formula)

def getSMSRecord(record_id):
	"""
	Retrieves a single record from SMS all table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		A single record from SMS all table

	"""

	AT = Airtable(BASE_ID, 'SMS all')
	return AT.get(record_id)

def deleteSMSRecord(record_id):
	"""
	Deletes a single record from SMS all table by its id

	Parameters:
		record_id(int): Airtable record id

	Returns:
		The deleted record

	"""

	AT = Airtable(BASE_ID, 'SMS all')
	return AT.delete(record_id)

# Returns iterator with lists in batches according to pageSize
def getSMSIter(**kwargs):
	"""
	Returns iterator with lists in batches according to pageSize for SMS all table

	Parameters:
		max_records (int, optional): The maximum total number of records that will be returned.
		view (str, optional): The name or ID of a view.
		page_size(int, optional): The number of records returned in each request. Must be less than or equal to 100. Default is 100.
		fields (str, list, optional): Name of field or fields to be retrieved. Default is all fields.
		sort (list, optional): List of fields to sort by.
		formula: Airtable formula

	Returns: 
		An iterator with lists in batches according to pageSize for SMS all table
		
	"""

	max_records = kwargs.get('max_records', 1000)
	view = kwargs.get('view', None)
	page_size = kwargs.get('page_size', 100)
	fields = kwargs.get('fields', None)
	sort = kwargs.get('sort', None)
	formula = kwargs.get('formula', None)
	AT = Airtable(BASE_ID, 'SMS all')
	return AT.get_iter(max_records = max_records, view=view, page_size=page_size, fields=fields, sort=sort, formula=formula)

def updateSMSRecord(record_id, fields, **kwargs):
	"""
	Updates a record in SMS all table by its record id. Only Fields passed are updated, the rest are left as is.

	Parameters:
		record_id(int): Airtable record id
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	AT = Airtable(BASE_ID, 'SMS all')
	return AT.update(record_id, fields, typecast)

def updateSMSRecordByField(field_name, field_value, fields, **kwargs):
	"""
	Updates the first record in SMS all table to match field name and value. Only Fields passed are updated, the rest are left as is.

	Parameters:
		field_name(str): Name of field to match (column name).
		field_value(str): Value of field to match.
		fields(dict): Fields to update. Must be dictionary with Column names as Key
		typecast(boolean, optional): Automatic data conversion from string values. Default is False
		view(str, optional): The name or ID of a view.
		sort(list, optional) List of fields to sort by. 

	Returns:
		The updated record

	"""

	typecast = kwargs.get('typecast', False)
	view = kwargs.get('view', 'SMS triage')
	sort = kwargs.get('sort', None)
	AT = Airtable(BASE_ID, 'SMS all')
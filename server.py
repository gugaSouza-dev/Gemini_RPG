import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'ESN000N1289306'
DATABASE_NAME = 'bd_rpg'

def connect_to_sql():
	connection_string = f"""
		DRIVER={{{DRIVER_NAME}}};
		SERVER={SERVER_NAME};
		DATABASE={DATABASE_NAME};
		Trusted_Connection=yes;
	"""
	connection = odbc.connect(connection_string)
	return connection

def close_cursor(cursor):
	cursor.close()
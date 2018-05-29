from CoreLibrary import CoreLibrary
import mysql.connector
import datetime
import json

class DatabaseLibrary:
    
    core = None

    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'projects',
        'raise_on_warnings': True,
        'use_pure': False,
    }
    connector = None

    def __init__(self):
        self.core = CoreLibrary()

    def openConnection(self):
        self.connector = mysql.connector.connect(**self.config)

    def closeConnection(self, cursor):
        cursor.close()
        self.connector.close()

    def execute(self, queryCommand, parameters = []):
        self.openConnection()
        cursor = self.connector.cursor()
        query = (queryCommand)
        try:
            if parameters.count != 0:
                cursor.execute(query % parameters[0])
            else:
                cursor.execute(query)
            return self.core.returnValue(self.setResult(cursor))
        except Exception as _ex:
            self.closeConnection(cursor)
            return self.core.returnValue([])

    def setResult(self, data):
            row_headers=[x[0] for x in data.description]
            rv = data.fetchall()
            json_data=[]
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            self.closeConnection(data)
            return json_data
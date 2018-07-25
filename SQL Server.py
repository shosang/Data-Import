# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:50:52 2018

@author: SH
"""

import pyodbc
import pandas as pd

# Obtain data from SQL Server Database 
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};'
    'SERVER=MyServer;'
    'DATABASE=MyDB;'
    'Trusted_Connection=yes;'
    )

sql_script = '''
    SELECT *
    FROM [MyDB].[dbo].[SampleTable]
'''

dataset = pd.read_sql(sql_script, conn)

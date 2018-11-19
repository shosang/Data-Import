# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:41:22 2018

@author: SH
"""

import os
import pyodbc

# Connection: MyDB
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};'
    'SERVER=MyServer;'
    'DATABASE=MyDB;'
    'Trusted_Connection=yes;'
    )

cursor = conn.cursor()
dirpath=os.getcwd()

# Open and run a SQL query (can be used for DML statements such as inserts) 
with open (dirpath + r'\sql.sql') as query_file:
    sql_script= query_file.read()

cursor.execute(sql_script)
conn.commit()

cursor.close()
conn.close()
del cursor
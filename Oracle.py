# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:30:35 2018

@author: SH
"""

import cx_Oracle
import pandas as pd

pw = input("Enter today's password: ")
dsn_tns = cx_Oracle.makedsn(hostname='hostname', port='1111', service_name='service_name') 
conn = cx_Oracle.connect(user=r'user_name', password=pw, dsn=dsn_tns) 
 
c = conn.cursor()
sql_script = '''
    SELECT *
    FROM table_name
'''

df_oracle = pd.read_sql(sql_script, conn)
conn.close()
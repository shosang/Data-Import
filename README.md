<b>Python</b>

1. File Dialog.py
This script allows the user to select a csv file using the file dialog box for data import

2. SQL Server.py
This script allows the user to pull data from an SQL Server database 
User is required to substitute details for Server and Database and to customize the SQL query.
Windows authentication is assumed.

3. Importing Web Data.ipynb
Sample code for using urllib, requests and BeautifulSoup libraries for importing data from the web.

4. Oracle.py
This script allows the user to pull data from an Oracle database 
User is required to substitute details for hostname, port, service name in dsn_tns.
User must supply their user name and will be prompted for password on execution.
User must customize the SQL query.

5. Logging.py
Script to produce a log file with the start and end time of each script run. 
Useful for implementation with a task scheduler.

6. SQL Run DML queries.py
Useful for running DML queries such as insert or truncate statements.
Opens and reads in the sql script saved in *.sql file. 
Executes the query in DB and commits changes. 


<b>R</b>
1. Connect to SQL Server DB from R.R
Use the command "sqllocaldb info MSSQLLocalDB" in command line to obtain the instance pipe name.
Replace server attribute with this detail.

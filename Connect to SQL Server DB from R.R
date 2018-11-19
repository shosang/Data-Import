install.packages("RODBC")
library("RODBC")

conn <- odbcDriverConnect('driver=SQL Server;
                          server=np:\\\\.\\pipe\\LOCALDB#7208EE4D\\tsql\\query;
                          database=Instacart;
                          trusted_connection=yes')

data <- sqlQuery(conn, "SELECT * FROM aisles;")

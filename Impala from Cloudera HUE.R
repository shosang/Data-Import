# Assumes Cloudera ODBC Connector is installed
# https://www.cloudera.com/downloads/connectors/impala/odbc/2-6-2.html#

library(implyr)
library(odbc)
library(tidyverse)

drv <- odbc::odbc()

impala <- src_impala(
  drv = drv,
  driver = "Cloudera ODBC Driver for Impala",
  host = "host",
  port = 21050,
  database = "default",
  uid = "username",
  pwd = "password"
)
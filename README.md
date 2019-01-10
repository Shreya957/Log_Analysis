# Log_Analysis
reporting tool in python that prints out reports (in plain text) based on the data in the database.

## Sets to include news Database
1. Use the vagrant file supplied by udacity ; this automatically sets up the news database
2. Download and unzip the schema
  - Download the data from (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  - Unzip the file and put the file newsdata.sql in vagrant directory
3. cd to vagrant directory and load the schema using below command
   psql -d news -f newsdata.sql
   Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating        tables    and populating them with data
 
## Steps to run the source code

1. clone the github (https://github.com/Shreya957/Log_Analysis) in the vagrant directory.
2. Create the view ( as described @ (view to be create / please execute the below sql view creation code) below)
3. Run the python code named Log_Analysis_DB.py using the below command
   python Log_Analysis_DB.py

## Program Design description
The python code has three funtions which are called in the main funtion one after the other.
Each funtion is resposible for retreiving the desired value for each of the three reporting question

## view to be create / please execute the below sql view creation code 
```create view "log_analysis"
as
select 
L.id as Id,
L.path as Path,
art.title as Title,
L.status as Status,
L.method as Method,
L.ip as IP,
L.time as time,
art.author as Auth_id
from
log as L LEFT JOIN articles as art
on
art.slug=substring(L.path FROM 10)order by time;```

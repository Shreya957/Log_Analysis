# Log_Analysis
reporting tool in python that prints out reports (in plain text) based on the data in the database.

# Command to run the code
python Log_Analysis_DB.py

# Program Design description
The python code has three funtions which are called in the main funtion one after the other.
Each funtion is resposible for retreiving the desired value for each of the three reporting question


# view to be create / please execute the below sql view creation code 
create view "log_analysis"
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
art.slug=substring(L.path FROM 10)order by time;

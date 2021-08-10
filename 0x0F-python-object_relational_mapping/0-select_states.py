#!/usr/bin/python3
"importing module "

import MySQLdb

"opening database connaction "
db= MySQLdb.connect("localhost:3306", "root","root","hbtn_0e_0_usa")
cursor = db.cursor()

sql = "SELECT * FROM state "
"""c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
try:
   # Execute the SQL command """
cursor.execute(sql)
for state in cursor.fetchall()
    print(state) 
  """
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

# disconnect from server"""
db.close()
"""
#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]"""

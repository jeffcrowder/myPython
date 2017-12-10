import sqlite3

db = sqlite3.connect('EXtemp.db')
print "connected"
cursor = db.cursor()
ts = "2017-12-5 07:00:00"
hn = "test"
td = 99.0

cursor.execute('''INSERT INTO temperature(timeStamp, hostname, tempData) VALUES( ?,?,?)''', (ts, hn, td))
print "added test data"
db.commit()


#cursor.execute('''DELETE FROM temperature WHERE hostname = ? ''', (hn,))
#print "delete the test data"
#db.commit()

db.close()

import pymysql

username = 'root'
password = 'root'
con = pymysql.connect(user=username, password=password)

cur = con.cursor()
cur.execute("SELECT now()")
now = cur.fetchone()
print("Database time: {}".format(now[0]))
cur = con.cursor()
cur.execute("SELECT user()")
user = cur.fetchone()
print("Database user: {}".format(user[0]))
cur = con.cursor()
cur.execute("SELECT VERSION()")
version = cur.fetchone()
print("Database version: {}".format(version[0]))
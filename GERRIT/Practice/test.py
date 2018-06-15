import pymysql

db = pymysql.connect("https://databases.000webhost.com","id1577436_olineexams","booki123","SAMPLE")

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version",data)
db.close()
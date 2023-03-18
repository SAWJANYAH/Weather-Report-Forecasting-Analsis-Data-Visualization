import mysql.connector

connection = mysql.connector.connect(
   user='root', password='India01$', host='127.0.0.1', port = 3306, database='weatherdata')

crsr = connection.cursor()

print("connect to database")
crsr.execute("select DateW from weatherdata where Max_gustspeed > 55")

result1 = crsr.fetchall()

for item in result1:
    print(item[0])
    sql = "select * from weatherdata where DateW > " + "'" + item[0] + "'" + " limit 4"
    crsr.execute(sql)
    resultrec = crsr.fetchall()
    print (resultrec) 

connection.close()
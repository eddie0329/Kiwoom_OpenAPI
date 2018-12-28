import sqlite3

#print(sqlite3.sqlite_version)

con = sqlite3.connect("c:/Users/LG/kospi.db")
#print(type(con))

cursor = con.cursor()

#create table kakao(Date, Open, High, Low, Closing, Volume)
#cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volume int)")

#insert values in kakao('16.06.03', 97000, 98600, 96900, 98000, 321405)
#cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")
#cursor.execute("INSERT INTO kakao VALUES('16.06.02', 99000, 99300, 96300, 97500, 556790)")

#commit
#con.commit()

#close
#con.close()

#select query
print(cursor.execute("SELECT * FROM kakao"))

#printing talbe
#print(cursor.fetchone())
#print(cursor.fetchone())
#print(cursor.fetchone())

#printing talbe all
print(cursor.fetchall())

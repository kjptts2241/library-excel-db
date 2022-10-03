import sys
import mariadb
import pandas as pd

# mariaDB 연결
def mariaDbConnection(u, pw, h, p, d):
    try:
        conn = mariadb.connect(user = u, password = pw, host = h, port = p, database = d)
        print("DB 연결 성공: {0}".format(h))
    except mariadb.Error as e:
        print("DB 연결 오류 : {}".format(e))
        sys.exit(1)

    return conn


def mariaDbClose(c):
    try:
        c.close()
        print("DB 닫기 성공")
    except mariadb.Error as e:
        print("DB 닫기 오류")
        sys.exit(1)


dbConn = mariaDbConnection('root', '1234', "localhost", 3306, 'library')
cur = dbConn.cursor()

data = pd.read_excel("lib.xlsx")

sql = "INSERT INTO libraryList (LibName,Address,Tel,Fax,Latitude,Longitude,Homepage,Closed,OperatingTime,LibCode) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
for i in range(len(data)):
    cur.execute(sql, tuple(data.values[i]))

dbConn.commit()

mariaDbClose(dbConn)

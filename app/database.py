import mysql.connector

def ConnectorMysql():
    try:
        mydb = mysql.connector.connect(
                host="",
                user="",
                passwd="",
                database="",
                auth_plugin='mysql_native_password'
        )
    except Exception as error:
        print(f"Error connecting to MySQL database: {error}")
        return
    
    return mydb


def get_all(from_table):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM {from_table}; "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def get_data(from_table, uid):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM {from_table} WHERE id=%s"
    mycursor.execute(sql, (uid,))
    myresult = mycursor.fetchone()
    if len(myresult) > 0: 
        for x in myresult:
            arr = {
                "_id" : x[0],
                "name" : x[1],
                "age" : int(x[2]),
                "address" : x[3]
                }
    return arr


def insert_data(from_table, uid, name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f"INSERT INTO {from_table} (uid,name,age) VALUES (%s ,%s, %s)"
    val = (uid, name, age)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def update_data(from_table, uid, name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f"UPDATE {from_table} SET  name=%s , age=%s WHERE id=%s"
    val = (name, age, uid)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def delete_data(from_table, uid):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f"DELETE  FROM {from_table} WHERE id=%s"
    mycursor.execute(sql, (uid,))
    mydb.commit()
    mycursor.close()
    mydb.close()
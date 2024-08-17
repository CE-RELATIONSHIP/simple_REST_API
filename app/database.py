from global_config import GlobalConfig
import mysql.connector
from os import getenv

def ConnectorMysql():
    try:
        mydb = mysql.connector.connect(
                host=getenv(GlobalConfig.HOST),
                user=getenv(GlobalConfig.USER),
                passwd=getenv(GlobalConfig.PASSWORD),
                database=getenv(GlobalConfig.DB_NAME),
                auth_plugin='mysql_native_password'
        )
    except Exception as error:
        print(f"Error connecting to MySQL database: {error}")
        return
    
    return mydb


def InitDB():
    try:
        if (ConnectorMysql() is None):
            raise "Database Can't connect"
        mydb = ConnectorMysql()
        cursor = mydb.cursor()
        
        with open('create_tables.sql', 'r') as file:
            create_table_query = file.read()
        
        cursor.execute(create_table_query)
        mydb.commit()
        print("Table created successfully.")
    
    except Exception as error:
        print(f"Error connecting to MySQL database: {error}")
        return
    
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()


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
        arr = {
            "_id" : myresult[0],
            "name" : myresult[1],
            "age" : int(myresult[2])
            }
    return arr


def insert_data(from_table, uid, name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    print(mycursor)
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
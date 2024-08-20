from flask import abort
from global_config import GlobalConfig
import mysql.connector
from os import getenv
from invalid_api_usage import InvalidAPIUsage

class CollectionsName():
    USER = 'USERS'

class MySqlConnector():
    def __init__(self, host, user, pwd, db_name, auth_plugin='mysql_native_password') -> None:
        try:
            self.__db = mysql.connector.connect(
                host = host,
                user = user,
                passwd = pwd,
                database = db_name,
                auth_plugin = auth_plugin
            )

            self.__cursor = self.__db.cursor()
        except Exception as error:
            print(f"Error connecting to MySQL database: {error}")
            exit(0)
    
    def get_all(self, from_table: str):
        sql = f"SELECT * FROM {from_table};"
        self.__cursor.execute(sql)
        myresult = self.__cursor.fetchall()
        return myresult
    
    def get_data(self, from_table: str, uid: str):
        sql = f"SELECT * FROM {from_table} WHERE uid=%s"
        self.__cursor.execute(sql, (uid,))
        myresult = self.__cursor.fetchone()
        if myresult and len(myresult) > 0: 
            data = {
                "uid" : myresult[0],
                "name" : myresult[1],
                "age" : int(myresult[2])
                }
        else:
            raise InvalidAPIUsage(f"Not found any entity belong to: {uid}", 404)
        return data

    def insert_data(self, from_table, uid, name, age):
        try:
            sql = f"INSERT INTO {from_table} (uid,name,age) VALUES (%s ,%s, %s)"
            val = (uid, name, age)
            self.__cursor.execute(sql, val)
            self.__db.commit()
        except Exception as error:
            raise InvalidAPIUsage(f"{error}", 400)

    def update_data(self, from_table, uid, name, age):
        self.get_data(from_table, uid)

        sql = f"UPDATE {from_table} SET  name=%s , age=%s WHERE uid=%s"
        val = (name, age, uid)
        self.__cursor.execute(sql, val)
        self.__db.commit()

    def delete_data(self, from_table, uid):
        self.get_data(from_table, uid)

        sql = f"DELETE  FROM {from_table} WHERE uid=%s"
        self.__cursor.execute(sql, (uid,))
        self.__db.commit()

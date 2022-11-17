import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(host = 'localhost',username = 'root',password = '999M@mmu999',database='restapi_db')
# if connection.is_connected():
#         cursor = connection.cursor()
#         user = (3, 'sam', 'mnbv')
#         insert_query = f"Insert into users (id,username,password) values ({user[0]},'{user[1]}','{user[2]}')"
#         print(insert_query)
#         cursor.execute(insert_query)
#         connection.commit()
#         # records = cursor.fetchall()
#         # print(records)
#         connection.close()

try :
    connection = mysql.connector.connect(host = 'localhost',username = 'root',password = '999M@mmu999',database='restapi_db')
    if connection.is_connected():
        cursor = connection.cursor()
        insert_query = 'Insert into users values (%s,%s,%s)'
        # user = ('5', 'john', 'dfgt')
        cursor.execute(insert_query, (9, 'jan', 'yhj'))
        connection.commit()
        # records = cursor.fetchall()
        # print(records)
        connection.close()
except Error as e:
    print(e)

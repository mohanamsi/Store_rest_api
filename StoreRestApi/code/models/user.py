import mysql.connector


class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_name(cls, username):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = 'select * from users where username = %s'
        # print(f"query=",query)
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row is not None:
            user = cls(*row)

        else :
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = f'select * from users where id = {_id} '
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            user = cls(*row)

        else:
            user = None

        connection.close()
        return user

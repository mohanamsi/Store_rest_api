import mysql.connector


class ItemModel:
    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):

        return {'name': self.name, 'price': self.price,'store_id':self.store_id}


    #it is a class method because its returning an object of itemmodel
    @classmethod
    def find_by_name(cls, name):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = 'select * from items where name=%s'
        # print(f"query=",query)
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        connection.close()

        if row:
            print(row)
            # return "worked"
            return cls(row[0],row[1],row[2])

    def insert(self):
        print(f"self",self.name,self.price)
        print()
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = 'insert into items values (%s,%s,%s)'
        print(f"query=",query)
        cursor.execute(query, (self.name, self.price,self.store_id))

        connection.commit()
        connection.close()

    def update(self):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = 'update items set  price =%s where name=%s'
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()



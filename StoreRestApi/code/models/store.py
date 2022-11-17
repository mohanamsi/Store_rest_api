import mysql.connector


class StoreModel:
    def __init__(self, store_name):
        # self.store_id = store_id
        self.store_name = store_name

    def json(self):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='999M@mmu999')
        cursor = connection.cursor()

        query = 'select * from items where store_id in (select store_id from stores where store_name=%s)'
        print(f"query=",query)
        cursor.execute(query, (self.store_name,))
        rows = cursor.fetchall()
        connection.close()
        store_items = []
        for row in rows:
            print(row)
            store_items.append({'name':row[0],'price':row[1],'store_id':row[2]})

        return {'name': self.store_name, 'items': store_items}


    #it is a class method because its returning an object of storemodel
    @classmethod
    def find_by_name(cls, store_name):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='999M@mmu999')
        cursor = connection.cursor()

        query = 'select * from stores where store_name = %s'
        # print(f"query=",query)
        print(store_name)
        cursor.execute(query, (store_name,))
        row = cursor.fetchone()
        connection.close()

        if row:
            print(row)
            # return "worked"
            return cls(row[1])

    def insert(self):
        print(f"self",self.store_name)
        print()
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='999M@mmu999')
        cursor = connection.cursor()

        query = 'insert into stores (store_name) values (%s)'
        print(f"query=",query)
        cursor.execute(query, (self.store_name,))

        connection.commit()
        connection.close()

    def update(self,new,cur):
        print(f"new=",new,cur)
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='999M@mmu999')
        cursor = connection.cursor()

        query = 'update stores set  store_name = %s where store_name=%s'
        cursor.execute(query, (new, cur,))
        print(query)

        connection.commit()
        connection.close()


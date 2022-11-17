from flask_restful import Resource,reqparse
from models.store import StoreModel
import mysql.connector


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('store_name', type=str, required=True, help='This field cannot be left blank.')
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "store not found."}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':"A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(store_name = name)
        # item.insert()
        try:
            print(f"store=", store)
            store.insert()
        except:
            return {'message': "An error occured creating the store."}, 500  # internal Server error

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store :
            products = store.json()
        else :
            return {'message':"No such store"}
        if products.items:

            return {'message': 'Cannot delete the store {}, as a items are present in that store '.format(name)}
        else :
            connection = mysql.connector.connect(host='localhost',
                                                 database='restapi_db',
                                                 username='root',
                                                 password='Sqlroot@123')
            cursor = connection.cursor()
            query = f'Delete from stores where store_name="{name}"'
            cursor.execute(query)

            connection.commit()
            connection.close()
            return {'message':'store deleted'}

    def put(self, name):
            data = Store.parser.parse_args()

            store = StoreModel.find_by_name(name)
            updated_store = StoreModel(data["store_name"])

            if store is None:
                    return {'message': 'Cannot delete the store {}, as a items are present in that store '.format(name)}
            else:
                try:
                    print(data["store_name"],name)
                    updated_store.update(data["store_name"],name)
                except:
                    return {"message": "An error occured updating the item."}, 500
            return updated_store.json()




class StoreList(Resource):
    def get(self):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = 'select * from stores'
        cursor.execute(query)
        stores = []
        for row in cursor.fetchall():
            stores.append({'store_id': row[0],'store_name': row[1] })

        connection.close()

        return {'stores': stores}

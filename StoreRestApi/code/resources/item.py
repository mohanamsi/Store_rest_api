import mysql.connector
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
# from ..models.item import ItemModel
# from code.models.item import ItemModel
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('name',type=str, required=True,help='This field cannot be left blank.')
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank.')
    parser.add_argument('store_id', type=int, required=True, help='Every item needs a store id')
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item :
            return item.json()
        return {'message':"Item not found."}, 404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)} , 400 #bad request

        data = Item.parser.parse_args()
        print(data)
        item = ItemModel(name,data['price'],data['store_id'])
        # item.insert()
        try:
            print(f"item=", item)
            item.insert()
        except:
            return {'message': "An error occured inserting the item."}, 500 #internal Server error

        return item.json(), 201

    def delete(self, name):

        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()
        if ItemModel.find_by_name(name) :
            query = f'delete from items where name="{name}"'
            cursor.execute(query)

            connection.commit()
        connection.close()

        return {'message':'Item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data["price"],data['store_id'])

        if item is None :
            try :
                updated_item.insert()
            except :
                return {"message":"An error occured inserting the item."}, 500
        else :
            try :
                updated_item.update()
            except :
                return {"message": "An error occured updating the item."}, 500
        return updated_item.json()


class ItemList(Resource):

    def get(self):
        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = 'select * from items'
        cursor.execute(query)
        items = []
        for row in cursor.fetchall():
            items.append({'name': row[0],'price': row[1],'store_id':row[2]})

        connection.close()

        return {'items': items}



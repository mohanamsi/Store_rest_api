from flask_restful import Resource,reqparse,request
import mysql.connector
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required = True,help='This field cannot be left blank.')
    parser.add_argument("password", type=str, required = True,help='This field cannot be left blank.')

    def post(self):
        data = UserRegister.parser.parse_args()

        #to avoid duplicates
        if UserModel.find_by_name(data["username"]) :
            return {'message' :'A user with that username already exists'}, 400

        connection = mysql.connector.connect(host='localhost',
                                             database='restapi_db',
                                             username='root',
                                             password='Sqlroot@123')
        cursor = connection.cursor()

        query = 'Insert into users (username,password) values(%s,%s)'
        cursor.execute(query,(data["username"],data["password"]))

        connection.commit()
        connection.close()

        return {'message':"User created successfully"}, 201






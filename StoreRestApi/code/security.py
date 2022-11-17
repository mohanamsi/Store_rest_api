# from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_name(username)
    if user and user.password == password:
        print(f'user=',user)
        return user


def identity(payload):
    print(f'payload=',payload)
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)




from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)

app.config['CORS_ORIGINS'] = 'http://127.0.0.1:5500'

CORS(app)
api = Api(app)

class Login(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True)
    parser.add_argument('password', required=True)
    args = parser.parse_args()

    username = args['username']
    password = args['password']


    return {
      'username': username,
      'password': password
    }

api.add_resource(Login, '/login')

if __name__ == '__main__':
  app.run(debug=True)
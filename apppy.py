from flask import Flask
from flask_restx import Api, Resource
app = Flask(__name__)
api = Api(app)


class apitest(Resource):
  def get(self):
    return "application deployed"
  
api.add_resource(apitest, '/apitest')
  
if __name__== '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)

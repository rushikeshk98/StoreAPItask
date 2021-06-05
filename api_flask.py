from flask import Flask, request
from flask_restful import Api, Resource
from task1 import store_api
app = Flask(__name__)
api = Api(app)
class store_api_output(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        # json_data = request.get_json(force=True)
        output = store_api(json_data)
        return output


api.add_resource(store_api_output, '/storeapi/output')

if __name__ == '__main__':
    app.run(debug=True)
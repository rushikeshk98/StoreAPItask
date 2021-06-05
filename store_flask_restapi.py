from flask import Flask, request
from flask_restful import Api, Resource
from store_api_main import store_api

app = Flask(__name__)
api = Api(app)


class StoreApiOutput(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        # json_data = request.get_json(force=True)
        output = store_api(json_data)
        return output


api.add_resource(StoreApiOutput, '/storeapi/output')

if __name__ == '__main__':
    app.run(debug=True)

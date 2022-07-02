from flask import Flask
from dataset import Dataset
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
datapath = "Programmer Test Questions SampleData.xlsx"
data = Dataset(datapath)

class Items(Resource):
	def get(self):
		return data.items

class ItemName(Resource):
	def get(self, name):
		return data.getItemByName(name)

class ItemID(Resource):
	def get(self, ID):
		return data.getItemByID(ID)

api.add_resource(Items, "/items")
api.add_resource(ItemName, "/item/<string:name>")
api.add_resource(ItemID, "/item/<int:ID>")

if __name__ == "__main__":
	app.run(debug=True)


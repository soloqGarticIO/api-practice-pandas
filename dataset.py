import pandas as pd

class Dataset:
	def __init__(self, path):
		self.path = path
		self.items = self.getItemsWithDisc()

	def getItems(self):
		df = pd.read_excel(self.path, sheet_name=0)
		df.rename(columns={"ItemPrice(RM)": "ItemPrice"}, inplace=True)
		dataset = df.to_dict(orient="records")
		for i in dataset:
			i["ItemPrice"] = format(i["ItemPrice"], ".2f")
		return dataset

	def getDiscounts(self):
		df = pd.read_excel(self.path, sheet_name=1)
		dataset = df.to_dict(orient="records")
		return dataset

	def getItemsWithDisc(self):
		items = self.getItems()
		discounts = self.getDiscounts()
		for i in items:
			for j in discounts:
				if i["DiscountCode"]==j["DiscountCode"]:
					i["DiscountPrice"] = format(float(i["ItemPrice"])*(1-float(j["Discount%"])),".2f")
		return items

	def getItemByName(self, name):
		for i in self.items:
			if i["ItemName"] == name:
				return i

	def getItemByID(self, ID):
		for i in self.items:
			if i["ItemID"] == ID:
				return i

# a = Dataset("Programmer Test Questions SampleData.xlsx")
# print(a.getItemByName("ItemB"))


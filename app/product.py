import json

class ProductHandler:
    def __init__(self, data_path):
        self.data_path = data_path
        self.load_data()

    def load_data(self):
        with open(self.data_path, "r") as file:
            self.data = json.load(file)

    def save_data(self):
        with open(self.data_path, "w") as file:
            json.dump(self.data, file, indent=2)

    def get_products(self):
        return self.data["Products"]

    def get_product_by_id(self, product_id: int):
        for product in self.data["Products"]:
            if product["id"] == product_id:
                return product
        return None

    def create_product(self, product_data: dict):
        product_data["id"] = len(self.data["Products"]) + 1
        self.data["Products"].append(product_data)
        self.save_data()
        return product_data

    def update_product(self, product_id: int, product_data: dict):
        product = self.get_product_by_id(product_id)
        if product:
            product.update(product_data)
            self.save_data()
            return True
        return False

    def delete_product(self, product_id: int):
        product = self.get_product_by_id(product_id)
        if product:
            self.data["Products"].remove(product)
            self.save_data()
            return True
        return False
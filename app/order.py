import json
from collections import defaultdict

class OrdersHandler:
    def __init__(self, data_path):
        self.data_path = data_path
        self.load_data()

    def load_data(self):
        with open(self.data_path, "r") as file:
            self.data = json.load(file)

    def save_data(self):
        with open(self.data_path, "w") as file:
            json.dump(self.data, file, indent=2)

    # get user by id
    def get_user(self, user_id: int):
        for user in self.data["Users"]:
            if user["id"] == user_id:
                return user
        return None

    # get user by id
    def get_product(self, product_id: int):
        for product in self.data["Products"]:
            if product["id"] == product_id:
                return product
        return None

    def get_orders(self, date, role):
        orders = self.data["Orders"]
        if date:
            orders = [order for order in orders if order["order_date"] == date]
            return orders

        if role == "invited":
            invited_users_orders = defaultdict(list)

            # Group orders by invited user ID
            for order in orders:
                if order["role"] == "invited":
                    invited_users_orders[order["invited_user_id"]].append(order)

            invited_users_info = []
            for user_id, user_orders in invited_users_orders.items():
                user = self.get_user(user_id)
                if user:
                    user_name = user["user_name"]
                    user_orders_count = len(user_orders)
                    invited_users_info.append({
                        "user_name": user_name,
                        "order_count": user_orders_count
                    })
            return invited_users_info

        return orders

    def get_order_by_id(self, order_id: int):
        order = next((order for order in self.data["Orders"] if order["id"] == order_id), None)
        if order:
            # user = self.get_user(order["user_id"])
            # product = self.get_product(order["product_id"])
            # order_info = {
            #     "id": order["id"],
            #     "order_date": order["order_date"],
            #     "role": order["role"],
            #     "quantity": order["quantity"],
            #     "user": user,
            #     "product": product
            # }
            # return order_info
            return order
        return None

    def create_order(self, order_data: dict):
        order_data["id"] = len(self.data["Orders"]) + 1
        self.data["Orders"].append(order_data)
        self.save_data()
        return order_data

    def update_order(self, order_id: int, order_data: dict):
        order = self.get_order_by_id(order_id)
        if order:
            order.update(order_data)
            self.save_data()
            return True
        return False

    def delete_order(self, order_id: int):
        order = self.get_order_by_id(order_id)
        if order:
            self.data["Orders"].remove(order)
            self.save_data()
            return True
        return False
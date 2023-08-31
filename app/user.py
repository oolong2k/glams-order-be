import json

class UserHandler:
    def __init__(self, data_path):
        self.data_path = data_path
        self.load_data()

    def load_data(self):
        with open(self.data_path, "r") as file:
            self.data = json.load(file)

    def save_data(self):
        with open(self.data_path, "w") as file:
            json.dump(self.data, file, indent=2)

    def get_users(self):
        return self.data["Users"]

    def get_user_by_id(self, user_id: int):
        for user in self.data["Users"]:
            if user["id"] == user_id:
                return user
        return None

    def create_user(self, user_data: dict):
        user_data["id"] = len(self.data["Users"]) + 1
        user_data["password"] = ""
        self.data["Users"].append(user_data)
        self.save_data()
        return user_data

    def update_user(self, user_id: int, user_data: dict):
        user = self.get_user_by_id(user_id)
        if user:
            user.update(user_data)
            self.save_data()
            return True
        return False

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.data["Users"].remove(user)
            self.save_data()
            return True
        return False

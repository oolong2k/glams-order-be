from fastapi import FastAPI, HTTPException, APIRouter, Query
from app.user import UserHandler
from app.product import ProductHandler
from app.order import OrdersHandler

app = FastAPI()

data_path = "databases/data.json"
router_prefix = APIRouter(prefix="/api/v1")

# load class model
user_handler = UserHandler(data_path)
product_handler = ProductHandler(data_path)
order_handler = OrdersHandler(data_path)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

#-- rest api user --#
@router_prefix.get("/users/")
def get_users():
    return user_handler.get_users()

@router_prefix.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_handler.get_user_by_id(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router_prefix.post("/users/")
def create_user(user_data: dict):
    user = user_handler.create_user(user_data)
    return {"message": "User created successfully"}

@router_prefix.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    user = user_handler.update_user(user_id, user_data)
    if user:
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router_prefix.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_handler.delete_user(user_id):
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

#-- rest api products --#
@router_prefix.get("/products/")
def get_products():
    return product_handler.get_products()

@router_prefix.get("/products/{product_id}")
def get_product(product_id: int):
    product = product_handler.get_product_by_id(product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@router_prefix.post("/products/")
def create_product(product_data: dict):
    product = product_handler.create_product(product_data)
    return {"message": "product created successfully"}

@router_prefix.put("/products/{product_id}")
def update_product(product_id: int, product_data: dict):
    product = product_handler.update_product(product_id, product_data)
    if product:
        return {"message": "Product updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@router_prefix.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_handler.delete_product(product_id):
        return {"message": "Product deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")

#-- rest api orders --#
@router_prefix.get("/orders/")
def get_orders(date: str | None = None, role: str | None = None):
    return order_handler.get_orders(date, role)

@router_prefix.get("/orders/{order_id}")
def get_order(order_id: int):
    order = order_handler.get_order_by_id(order_id)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="order not found")

@router_prefix.post("/orders/")
def create_order(order_data: dict):
    order = order_handler.create_order(order_data)
    return {"message": "order created successfully"}

@router_prefix.put("/orders/{order_id}")
def update_order(order_id: int, order_data: dict):
    order = order_handler.update_order(order_id, order_data)
    if order:
        return {"message": "order updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="order not found")

@router_prefix.delete("/orders/{order_id}")
def delete_order(order_id: int):
    if order_handler.delete_order(order_id):
        return {"message": "order deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="order not found")


app.include_router(router_prefix)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

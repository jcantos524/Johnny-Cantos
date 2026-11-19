def reserve_inventory(products, order):
    for item in order["items"]:
        product = next((p for p in products if p["id"] == item["product_id"]), None)
        if product is not None:
            if product["stock"] >= item["quantity"]: # Check if there is enough stock
                product["stock"] -= item["quantity"] # Reserve the stock by reducing it
            else:
                raise ValueError(f"Insufficient stock for product ID {item['product_id']}")

def restock_product(products, product_id, amount):
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("Restock amount must be a positive whole number.")
    for product in products:
        if product["id"] == product_id:
            product["stock"] += amount  # Add to the existing stock
            return product
    return None

def update_shopping_cart(cart, action):
    product_id = action.get("product_id")
    action_type = action.get("type")
    quantity = action.get("quantity", 0)
    
    if not product_id or not action_type:
        return cart  # Return unchanged cart if required fields are missing
    
    if action_type == "add":
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
            
    elif action_type == "remove":
        if product_id in cart:
            if cart[product_id] <= quantity:
                del cart[product_id]  # Remove product if quantity to remove >= current quantity
            else:
                cart[product_id] -= quantity
                
    elif action_type == "change":
        if quantity > 0:  # Only update if new quantity is positive
            cart[product_id] = quantity
        else:  # If new quantity is 0 or negative, remove the product
            if product_id in cart:
                del cart[product_id]
    return cart

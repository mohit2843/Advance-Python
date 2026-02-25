def create_product_catalog():
    return {
        "1": {"name": "Laptop", "price": 50000},
        "2": {"name": "Smartphone", "price": 20000},
        "3": {"name": "Headphones", "price": 2000},
        "4": {"name": "Smartwatch", "price": 1000},
        "5": {"name": "Tablet", "price": 15000},
        "6": {"name": "Grocery", "price":10000}
    }
    
def display_product_catalog(product_catalog):
    print("Product Catalog:")
    for product_id, product in product_catalog.items():
        print("ID:", product_id, "Name:", product['name'], "Price: $", product['price'])
        
def add_to_cart(cart, product_catalog, product_id):
    if product_id in product_catalog:
        cart.append(product_catalog[product_id])
        print("product added to cart",product_catalog[product_id]['name'])
    else:
        print("Invalid product ID.")
        
def remove_from_cart(cart, product_id):
    for item in cart:
        if item['name'] == product_catalog[product_id]['name']:
            cart.remove(item)
            print("product removed from cart",item['name'])
            return
    print("Product not found in cart.")
    
def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        for item in cart:
            print("items in cart:",len(cart),"name:",item['name'],"price:",item['price'])
                            
def checkout(cart):
    total_amount = sum(item['price'] for item in cart)
    total_items = len(cart)
    print(f"Total items: {total_items}")
    print(f"Total amount: ${total_amount}")
    if total_amount > 1000:
        discount = total_amount * 0.1             
        total_amount -= discount
        print("discount applied: $",discount)
        print("final amount after discount: $",total_amount)        
def main():
    product_catalog = create_product_catalog()
    cart = []
    
    while True:
        display_product_catalog(product_catalog)
        action = input("Enter 'add' to add to cart, 'remove' to remove from cart, 'checkout' to checkout, 'view' to view or 'exit' to exit: ")
        
        if action == 'add':
            product_id = input("Enter the product ID to add to cart: ")
            add_to_cart(cart, product_catalog, product_id)
        elif action == 'remove':
            product_id = input("Enter the product ID to remove from cart: ")
            remove_from_cart(cart, product_id)
        elif action == 'checkout':
            checkout(cart)
        elif action == 'view':
            view_cart(cart)    
        elif action == 'exit':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid action. Please try again.")
if __name__ == "__main__":
    main()
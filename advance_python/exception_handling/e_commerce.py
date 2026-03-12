class ECommerce:
    def __init__(self):
        self.inventory = {"Laptop": 5, "Mouse": 0}
        self.coupons = ["SAVE10", "WELCOME"]

    def process_order(self, item, coupon, payment_method):
        try:
            if coupon not in self.coupons:
                raise PermissionError("Invalid coupon code.")
            
            if payment_method not in ["Credit", "PayPal"]:
                raise ConnectionRefusedError("Invalid payment method.")
            
            print("Order processed successfully!")
            
        except (PermissionError, ConnectionRefusedError) as e:
            print("Order Processing Error:")

shop = ECommerce()
shop.process_order("Mouse", "SAVE10", "Credit")
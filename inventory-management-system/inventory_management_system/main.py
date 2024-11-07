class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"Username: {self.username}, Role: {self.role}"

user_db = {
    'admin': User('admin', 'admin123', 'Admin'),
    'user': User('user', 'user123', 'User')
}

def login(username, password):
    if username in user_db:
        user = user_db[username]
        if user.password == password:
            return user
    return None

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists.")
        else:
            self.products[product.product_id] = product
            print("Product added successfully.")

    def edit_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name:
                product.name = name
            if category:
                product.category = category
            if price:
                product.price = price
            if stock_quantity is not None:
                product.stock_quantity = stock_quantity
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                print(product)

    def add_user(self, username, password, role):
        if username in user_db:
            print("User already exists.")
        else:
            user_db[username] = User(username, password, role)
            print("User added successfully.")

    def remove_user(self, username):
        if username in user_db:
            del user_db[username]
            print("User removed successfully.")
        else:
            print("User not found.")

    def view_users(self):
        if not user_db:
            print("No users in the system.")
        else:
            for user in user_db.values():
                print(user)

def main():
    inventory = Inventory()
    while True:
        print("\nWelcome to the Inventory Management System")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose an option: ")
        if choice == '2':
            print("Exiting the system. Goodbye!")
            break

        elif choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login(username, password)

            if user:
                print(f"Welcome, {user.role}!")
                while True:
                    if user.role == 'Admin':
                        print("\nAdmin Menu:")
                        print("1. Add Product")
                        print("2. Edit Product")
                        print("3. Delete Product")
                        print("4. View Products")
                        print("5. Add User")
                        print("6. Remove User")
                        print("7. View Users")
                        print("8. Log Out")

                        admin_choice = input("Choose an option: ")
                        if admin_choice == '1':
                            product_id = input("Enter product ID: ")
                            name = input("Enter product name: ")
                            category = input("Enter product category: ")
                            price = float(input("Enter product price: "))
                            stock_quantity = int(input("Enter stock quantity: "))
                            new_product = Product(product_id, name, category, price, stock_quantity)
                            inventory.add_product(new_product)
                        elif admin_choice == '2':
                            product_id = input("Enter product ID to edit: ")
                            name = input("Enter new product name (or leave blank to keep unchanged): ")
                            category = input("Enter new product category (or leave blank to keep unchanged): ")
                            price_input = input("Enter new product price (or leave blank to keep unchanged): ")
                            stock_quantity_input = input("Enter new stock quantity (or leave blank to keep unchanged): ")

                            price = float(price_input) if price_input else None
                            stock_quantity = int(stock_quantity_input) if stock_quantity_input else None

                            inventory.edit_product(product_id, name or None, category or None, price, stock_quantity)
                        elif admin_choice == '3':
                            product_id = input("Enter product ID to delete: ")
                            inventory.delete_product(product_id)
                        elif admin_choice == '4':
                            print("\nCurrent Inventory:")
                            inventory.view_products()
                        elif admin_choice == '5':
                            new_username = input("Enter new username: ")
                            new_password = input("Enter new password: ")
                            new_role = input("Enter role (Admin/User): ")
                            inventory.add_user(new_username, new_password, new_role)
                        elif admin_choice == '6':
                            username_to_remove = input("Enter username to remove: ")
                            inventory.remove_user(username_to_remove)
                        elif admin_choice == '7':
                            print("\nCurrent Users:")
                            inventory.view_users()
                        elif admin_choice == '8':
                            break
                        else:
                            print("Invalid option.")

                    elif user.role == 'User':
                        print("\nUser Menu:")
                        print("1. View Products")
                        print("2. Log Out")

                        user_choice = input("Choose an option: ")
                        if user_choice == '1':
                            print("\nCurrent Inventory:")
                            inventory.view_products()
                        elif user_choice == '2':
                            break
                        else:
                            print("Invalid option.")
            else:
                print("Invalid username or password.")
        else:
            print("Invalid option. Please choose either 1 or 2.")

if __name__ == "__main__":
    main()

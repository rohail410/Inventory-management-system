Inventory Management System
The Inventory Management System is a console-based application built with Python for managing products, users, and inventory for a small business. The system has two main user roles: Admin and User, each with different levels of access and permissions.

Features
User Authentication: Two roles available – Admin and User.
Product Management:
Admins can add, edit, delete, and view products.
Users can only view products.
User Management:
Admins can add and remove users and view all registered users.
Inventory Viewing: Both Admins and Users can view the current inventory status.
How It Works
Login:

Users are required to log in with a username and password.
Based on the credentials provided, the user is assigned either Admin or User permissions.
Admin Role:

Upon successful login, Admins can access the following options:
Add Product: Allows adding new products to the inventory with details such as ID, name, category, price, and stock quantity.
Edit Product: Enables editing of existing product information.
Delete Product: Allows deletion of products from the inventory.
View Products: Displays a list of all products in the inventory.
Add User: Admins can add new users with specified roles.
Remove User: Admins can remove users by specifying the username.
View Users: Shows a list of all users with their roles.
Log Out: Exits the admin menu and logs out.
User Role:

Upon login, Users can access the following options:
View Products: Displays a list of all products in the inventory.
Log Out: Exits the user menu and logs out.
Default Login Credentials
Admin

Username: admin
Password: admin123
User

Username: user
Password: user123
Example Usage
Admin Example
Admin logs in with username admin and password admin123.
Accesses the Admin menu, where they can add a new product, edit existing products, or manage users.
User Example
User logs in with username user and password user123.
Can only view products in the inventory and then log out.

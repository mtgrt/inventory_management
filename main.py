from database import SessionLocal, engine
import models
from models.product import Product
from models.supplier import Supplier
import activity_log
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cli.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def main_menu():
    while True:
        print("\nInventory Management System")
        print("1. Manage Products")
        print("2. Manage Suppliers")
        print("3. View Activity Logs")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_products()
        elif choice == '2':
            manage_suppliers()
        elif choice == '3':
            view_activity_logs()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_products():
    while True:
        print("\nManage Products")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View All Products")
        print("4. Find Product by ID")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            view_all_products()
        elif choice == '4':
            find_product_by_id()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_suppliers():
    while True:
        print("\nManage Suppliers")
        print("1. Add Supplier")
        print("2. Delete Supplier")
        print("3. View All Suppliers")
        print("4. Find Supplier by ID")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_supplier()
        elif choice == '2':
            delete_supplier()
        elif choice == '3':
            view_all_suppliers()
        elif choice == '4':
            find_supplier_by_id()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def view_activity_logs():
    print("\nActivity Logs")
    activity_log.view_logs()

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    location = input("Enter product location: ")
    batch_number = input("Enter batch number: ")
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
    supplier_id = int(input("Enter supplier ID: "))
    
    db = next(get_db())
    new_product = Product(
        name=name,
        quantity=quantity,
        location=location,
        batch_number=batch_number,
        expiry_date=expiry_date,
        supplier_id=supplier_id
    )
    db.add(new_product)
    db.commit()
    activity_log.log_activity(f"Added product {name}")
    print(f"Product {name} added successfully.")

def delete_product():
    product_id = int(input("Enter product ID to delete: "))
    
    db = next(get_db())
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        activity_log.log_activity(f"Deleted product {product.name}")
        print(f"Product {product.name} deleted successfully.")
    else:
        print(f"No product found with ID {product_id}.")

def view_all_products():
    db = next(get_db())
    products = db.query(Product).all()
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, Location: {product.location}, Batch: {product.batch_number}, Expiry: {product.expiry_date}, Supplier ID: {product.supplier_id}")

def find_product_by_id():
    product_id = int(input("Enter product ID: "))
    
    db = next(get_db())
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, Location: {product.location}, Batch: {product.batch_number}, Expiry: {product.expiry_date}, Supplier ID: {product.supplier_id}")
    else:
        print(f"No product found with ID {product_id}.")

def add_supplier():
    name = input("Enter supplier name: ")
    email = input("Enter supplier email: ")
    phone = input("Enter supplier phone: ")

    db = next(get_db())
    new_supplier = Supplier(name=name, email=email, phone=phone)
    db.add(new_supplier)
    db.commit()
    activity_log.log_activity(f"Added supplier {name}")
    print(f"Supplier {name} added successfully.")

def delete_supplier():
    supplier_id = int(input("Enter supplier ID to delete: "))
    
    db = next(get_db())
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if supplier:
        db.delete(supplier)
        db.commit()
        activity_log.log_activity(f"Deleted supplier {supplier.name}")
        print(f"Supplier {supplier.name} deleted successfully.")
    else:
        print(f"No supplier found with ID {supplier_id}.")

def view_all_suppliers():
    db = next(get_db())
    suppliers = db.query(Supplier).all()
    for supplier in suppliers:
        print(f"ID: {supplier.id}, Name: {supplier.name}, Email: {supplier.email}, Phone: {supplier.phone}")

def find_supplier_by_id():
    supplier_id = int(input("Enter supplier ID: "))
    
    db = next(get_db())
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if supplier:
        print(f"ID: {supplier.id}, Name: {supplier.name}, Email: {supplier.email}, Phone: {supplier.phone}")
    else:
        print(f"No supplier found with ID {supplier_id}.")

if __name__ == "__main__":
    main_menu()

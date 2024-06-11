# Inventory Management System

This is a Python command-line application for managing inventory, handling orders, managing suppliers, tracking batches and expiry dates, and keeping a record of all inventory-related activities.

## Features

- **ORM Requirements**:
  - The application uses SQLAlchemy as the ORM framework.
  - Data model includes two main classes: `Product` and `Supplier`.
  - One-to-many relationship exists between `Product` and `Supplier`.

- **CLI Requirements**:
  - User-friendly command-line interface allows easy interaction.
  - Menus guide users through various options for managing inventory, orders, suppliers, and batches.

- **Additional Features**:
  - **Keep Track of Inventory**: Users can view item quantities and locations, and update inventory levels as needed.
  - **Handle Orders**: Users can process customer orders, manage order statuses, and generate shipping information.
  - **Manage Suppliers**: Users can add, edit, and remove supplier information, as well as place orders with suppliers.
  - **Track Batches and Expiry Dates**: Users can track batch numbers and expiry dates for perishable items, with alerts for impending expiry.
  - **Keep a Record**: All inventory-related activities are logged for accountability.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/inventory-management.git
   cd inventory-management

2. Install dependencies using Pipenv:
        pipenv install

3. Run the application:

    bash
       pipenv run python main.py

4. Usage

    Upon running the application, you'll be presented with a main menu where you can choose various options.
    Follow the prompts to perform actions such as adding products, processing orders, managing suppliers, and tracking batches.
    Error messages will be displayed for invalid inputs or actions.

5. Project Structure

inventory_management/
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── supplier.py
│   └── activity_log.py
│
├── cli/
│   ├── __init__.py
│   └── main.py
│
├── database.py
├── Pipfile
├── Pipfile.lock
└── README.md

6. Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Code Snippets

Here are some sample code snippets to demonstrate how you can implement certain features:

    ORM Models:

python

# models/product.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    location = Column(String)

    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship("Supplier", back_populates="products")

python

# models/supplier.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    phone = Column(String)

    products = relationship("Product", back_populates="supplier")

    CLI Interface:

python

# cli/main.py
def main():
    # Implement your CLI interface here
    pass

if __name__ == "__main__":
    main()

    Database Setup:

python

# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./inventory.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

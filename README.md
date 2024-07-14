# Warehouse Management App Backend

## Overview

This repository contains the backend source code for a Warehouse Management App designed for small businesses. Co-owned by [Your Name] and [Your Girlfriend's Name], this app aims to streamline inventory tracking, order processing, and warehouse operations, making it easier for small business owners to manage their stock efficiently.

## Features

- **Inventory Management**: Track stock levels, manage product details, and set reorder points.
- **Order Processing**: Process incoming orders, generate picking lists, and manage shipping.
- **Supplier Management**: Keep track of suppliers, purchase orders, and incoming shipments.
- **Reporting**: Generate reports on inventory levels, sales, and order fulfillment.
- **User Management**: Secure login and role-based access control for different user levels.

## Technologies Used

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Deployment**: Docker, Kubernetes

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Alfreed0/SoftyWarehouseBack.git
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Configure the environment variables:
   ```bash
   nano .env
4. Create the database tables:
   ```bash
   alembic upgrade head
5. Run the FastAPI server:
   ```bash
    uvicorn main:app --reload
  
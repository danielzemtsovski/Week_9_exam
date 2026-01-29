from typing import List, Dict, Any

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    # SELECT `customerName`,`creditLimit` FROM `customers` WHERE `creditLimit` < 10000 OR `creditLimit` > 100000
    pass

def get_orders_with_null_comments():
    # SELECT `orderNumber`,`comments` FROM `orders` 
    # WHERE `comments` IS NULL
    # ORDER BY `orderDate`
    """Return orders that have null comments."""
    pass

def get_first_5_customers():
    """Return the first 5 customers."""
   # SELECT `customerName`,`contactLastName`,`contactFirstName` FROM `customers` ORDER BY `contactLastName` LIMIT 5
    pass

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    #SELECT SUM(`amount`), AVG(`amount`), MIN(`amount`) ,MAX(`amount`) FROM `payments`
    pass

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    # SELECT employees.`lastName`, employees.`firstName`, offices.phone
    # FROM `employees`
    # INNER JOIN offices ON employees.officeCode=offices.officeCode
    pass

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    # SELECT customers.`customerName`, orders.shippedDate FROM `customers` LEFT JOIN orders ON customers.customerNumber=orders.customerNumber
    pass

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    # SELECT customers.customerName, COUNT(orders.orderNumber)
    # FROM `customers` 
    # INNER JOIN orders ON customers.customerNumber= orders.customerNumber
    # GROUP BY orders.customerNumber, customers.customerName
    # ORDER BY customers.customerName
    pass

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    # SELECT customers.customerName, employees.firstName, SUM(payments.amount) 
    # FROM customers
    # INNER JOIN employees ON customers.salesRepEmployeeNumber =employees.employeeNumber
    # INNER JOIN payments ON customers.customerNumber=payments.customerNumber
    # WHERE employees.firstName LIKE '%ly%' OR employees.firstName LIKE '%mu%'
    # GROUP BY customers.customerName, employees.firstName
    # ORDER BY SUM(payments.amount) DESC
    pass

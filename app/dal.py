from typing import List, Dict, Any
from db import get_db_connection

def get_customers_by_credit_limit_range():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT customerName, creditLimit FROM customers 
                      WHERE creditLimit < 10000 OR creditLimit > 100000""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results


def get_orders_with_null_comments():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT `orderNumber`,`comments` FROM `orders` 
                      WHERE `comments` IS NULL
                      ORDER BY `orderDate`""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results

def get_first_5_customers():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT `customerName`,`contactLastName`,`contactFirstName` 
                      FROM `customers` 
                      ORDER BY `contactLastName` LIMIT 5""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results

def get_payments_total_and_average():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT SUM(`amount`), AVG(`amount`), MIN(`amount`) ,MAX(`amount`) 
                   FROM `payments`""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results

def get_employees_with_office_phone():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT employees.`lastName`, employees.`firstName`, offices.phone
                      FROM `employees`
                      INNER JOIN offices ON employees.officeCode=offices.officeCode""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results

def get_customers_with_shipping_dates():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT customers.`customerName`, orders.shippedDate FROM `customers` LEFT JOIN orders ON customers.customerNumber=orders.customerNumber""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results

def get_customer_quantity_per_order():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT customers.customerName, COUNT(orders.orderNumber)
                      FROM `customers` 
                      INNER JOIN orders ON customers.customerNumber= orders.customerNumber
                      GROUP BY orders.customerNumber, customers.customerName
                      ORDER BY customers.customerName""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  
    cursor.execute("""SELECT customers.customerName, employees.firstName, SUM(payments.amount) 
                      FROM customers
                      INNER JOIN employees ON customers.salesRepEmployeeNumber =employees.employeeNumber
                      INNER JOIN payments ON customers.customerNumber=payments.customerNumber
                      WHERE employees.firstName LIKE '%ly%' OR employees.firstName LIKE '%mu%'
                      GROUP BY customers.customerName, employees.firstName
                      ORDER BY SUM(payments.amount) DESC""")
    results = cursor.fetchall()   
    cursor.close()
    connection.close()  
    return results
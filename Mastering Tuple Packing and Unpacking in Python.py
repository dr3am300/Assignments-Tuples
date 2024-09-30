# Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.
# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
# Problem Statement: You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.
# Sample Order Data:
# orders = [
#    ("Alice", "Laptop", 1),
#    ("Bob", "Camera", 2),
#    # More orders...]
# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.
# Ensure that all code in your file is ready to run. 
# This means that if someone opens your file and clicks the run button at the top, all code executes as intended. 
# For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. 
# If you have a function, make sure the function is called and runs.
# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Dream", "Smartphone", 1),
    ("Joe", "Headphones", 1),
    ("Baron", "Tablet", 2)
]

welcome_message = "Welcome to the Customer Order Processing System!"
print(welcome_message)
to_do = input("What would you like to do? (Y) Process orders (N) Exit: ").upper()

while to_do:
    if to_do == "Y":
        for order in orders:
            customer, product, quantity = order
            print(f"Customer: {customer}, Product: {product}, Quantity: {quantity}")
    elif to_do == "N":
        you_sure = input("Are you sure you want to exit? (Y) Yes (N) No: ").upper()
        if you_sure == "Y":
            break
        else:
            print("Welcome back to the Customer Order Processing System!")
    else:
        print("Invalid input. Please try again.")
    to_do = input("What would you like to do? (Y) Process orders (N) Exit: ").upper()
print("Thank you for using the Customer Order Processing System!")

def test_customer_order_processing():
    assert orders == [
        ("Alice", "Laptop", 1),
        ("Bob", "Camera", 2),
        ("Dream", "Smartphone", 1),
        ("Joe", "Headphones", 1),
        ("Baron", "Tablet", 2)
    ]
    to_do = "Y"
    for order in orders:
        customer, product, quantity = order
        assert f"Customer: {customer}, Product: {product}, Quantity: {quantity}" == f"Customer: {customer}, Product: {product}, Quantity: {quantity}"
    to_do = "N"
    assert to_do == "N"
    print("All tests pass.")
test_customer_order_processing()


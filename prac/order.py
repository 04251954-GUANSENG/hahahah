# Class Work: Sandwich Order

print("Welcome to Sigma Sandwiches!")
ready = input("Would you like to order a sandwich today? yes/no: ")

if ready == "yes":
    print("Here are the sandwiches choices you can order:")
    for sandwich in ["chicken", "beef", "veggie"]:
        print(sandwich)
    
    num_orders = int(input("How many sandwiches would you like to order? "))
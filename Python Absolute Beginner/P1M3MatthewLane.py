#P1M3MatthewLane

maximum_order = 150.0
minimum_order = 1.0

def cheese_program(order_amount):

    if order_amount.isdigit() == False:
        print('Enter cheese order weight (numeric value): ')

    elif float(order_amount) > maximum_order:
        print(order_amount, " is more than currently available stock")

    elif float(order_amount) < minimum_order:
        print(order_amount, " is less than currently available stock")

    elif (float(order_amount) <= maximum_order) and (float(order_amount) >= minimum_order):
        print(order_amount, "units of cheese costs","$",int(order_amount) * 10)

    else:
        print("Enter numeric value")


weight = input("Enter cheese order units (numeric value): ")
function = cheese_program(weight)


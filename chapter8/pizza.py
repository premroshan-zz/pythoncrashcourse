def make_pizza(size,*toppings):
    """Print the list of pizza toppings"""
    print(f"Make a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

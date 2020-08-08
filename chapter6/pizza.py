pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese']
}

#summarize the order
print(f"You ordered a {pizza['crust']}-crusted pizza with the following toppings")

for topping in pizza['toppings']:
    print(topping)
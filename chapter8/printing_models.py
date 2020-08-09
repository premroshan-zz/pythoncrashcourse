#Start with some designs that need to be printed
unprinted_designs = ['phone case','robot','container']
completed_designs = []

def print_models(unprinted_designs,completed_designs):
    #pop items from unprinted designs and then move to completed designs
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_designs.append(current_design)

def show_completed_models(completed_designs):
    #display all completed models
    print("The following models have been printed:")
    for design in completed_designs:
        print(design)

print_models(unprinted_designs[:],completed_designs)
show_completed_models(completed_designs)

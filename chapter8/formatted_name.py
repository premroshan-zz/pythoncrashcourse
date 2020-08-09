def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

fname = input("Enter first name: ")
lname = input("Enter last name: ")
musician = get_formatted_name(fname,lname)
print(musician)
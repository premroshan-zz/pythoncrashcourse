def build_person(fname,lname,age=None):
    """Returns a built person object"""
    person = {
        'first_name': fname,
        'last_name' : lname
        }
    
    if age:
        person['age'] = age
    
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
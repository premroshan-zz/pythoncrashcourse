users = {
    'premnair' : {
        'firstname' : 'Prem Roshan',
        'lastname' : 'Nair',
        'location' : 'Home'
    },
    'sagunair' : {
        'firstname' : 'Prem Sagar',
        'lastname' : 'Nair',
        'location' : 'Home'
    },
    'adinair' : {
        'firstname' : 'Aditya',
        'lastname' : 'Nair',
        'location' : 'Home'
    }
}

for user, details in users.items():
    print(f"Details for {user} are")
    print(f"First name: {details['firstname']}")
    print(f"Last name: {details['lastname']}")
    print(f"Location: {details['location']}")
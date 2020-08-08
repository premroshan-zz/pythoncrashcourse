favourite_languages = {
    'Prem' : 'python',
    'Sagar' : 'Kutta',
    'Sarath' : 'Rust',
    'Adi' : 'C'
}

language = favourite_languages['Prem'].title()
print(f"Prem's favourite language is {language}")

for name, language in favourite_languages.items():
    print(f"Favourite language of {name} is {language}")

for name in favourite_languages.keys():
    print(f"{name.title()}")

for name in sorted(favourite_languages.keys()):
    print(f"Sorted name {name}")

for language in favourite_languages.values():
    print(f"Languages are {language}")
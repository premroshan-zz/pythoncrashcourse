#have language as a list

favourite_languages = {
    'Prem' : ['Python', 'Java', 'Swift', 'Rust'],
    'Adi' : ['C', 'C++', 'Go', 'Rust'],
    'Sagu' : ['Java', 'Python', 'Javascript']
}

for name, languages in favourite_languages.items():
    print(f"{name.title()}'s favourite languages are:")
    for language in languages:
        print(language)

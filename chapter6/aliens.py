alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'blue', 'points':10}
alien_2 = {'color':'read', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(f"Alien statistics are {alien['color'], alien['points']}")
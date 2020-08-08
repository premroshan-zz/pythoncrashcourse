alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['color'] = 'blue'
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points")

alien_0['x-position'] = 0
alien_0['y-position'] = 25

print(alien_0)

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 6
print(alien_1)

print(f"Alien 1 with color {alien_0['color']} is talking to alient 2 with color {alien_1['color']}")


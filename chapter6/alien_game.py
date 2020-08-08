# alien game

alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium' }
print(f"Original position: {alien_0['x-position']}, {alien_0['y-position']}")

#move the alien to right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New position is {alien_0['x-position']},{alien_0['y-position']}")


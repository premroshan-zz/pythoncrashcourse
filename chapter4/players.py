#using slice

players = ["prem", "adi", "howzy", "lippi"]
print(players[2:])
print(players[-3:])

print("Here are the first three players on the list")
for player in players[:3]:
    print(player.title())


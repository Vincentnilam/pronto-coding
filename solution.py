import json

# load board and rolls from command line*
f = open('board.json')
data = json.load(f)

roll_1 = open('rolls_1.json')
roll_data = json.load(roll_1)

print("BOARD: ")


players = ['Peter', 'Billy', 'Charlotte', 'Sweedal'] 

propertiesOwned = {'Peter': [], 'Billy': [], 'Charlotte': [], 'Sweedal': []}

# owned money is 16 at start.
moneyOwned = {'Peter': 16, 'Billy': 16, 'Charlotte' :16, 'Sweedal': 16}

place = []
for i in data:
    print(i)
    place.append(i['name'])

for i in range(len(place)):
    print(place[i])

f.close()

print()


roll_1.close()
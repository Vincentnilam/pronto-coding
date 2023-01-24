import json
import sys

# Command line arguments


# load board and rolls from command line*
f = open(sys.argv[1])
data = json.load(f)

roll = open(sys.argv[2])
roll_data = json.load(roll)

print("BOARD: ")

players = ['Peter', 'Billy', 'Charlotte', 'Sweedal'] 

# dictionary to accumulate properties owned by each players
properties_owned = {'Peter': [], 'Billy': [], 'Charlotte': [], 'Sweedal': []}

# owned money is 16 at start.
money_owned = {'Peter': 16, 'Billy': 16, 'Charlotte' :16, 'Sweedal': 16}

# initialise players' position
players_position = {'Peter': 0, 'Billy': 0, 'Charlotte':0, 'Sweedal': 0}

place = []
for i in data:
    print(i)
    place.append(i['name'])

for i in range(len(place)):
    print(place[i])

player_index = 0
roll_index = 0

winner = None

while(winner is None):
    player = players[player_index]
    position = players_position[player]

    # since everyone starts on GO, we just need to check go after the first roll
    data_length = len(data)
    
    position = (position + roll_data[roll_index])%data_length 

    # print(player, ' ',position)
    if(data[position]['type']) == 'go':
        money_owned[player] += 1
    elif(data[position]['type'] == 'property'):
        # check if the property is not owned by any players
        if(data[position]['name'] not in properties_owned[player]):
            # check if it's buyable; if it is, buy(put in properties_owned); else; bankrupt
            if(money_owned[player] >= data[position]['price']):
                properties_owned[player].append(data[position]['name'])
                money_owned[player] -= data[position]['price']

    #print(properties_owned[player])

f.close()

print()


roll.close()
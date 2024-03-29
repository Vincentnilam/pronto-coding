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


player_index = 0
roll_index = 0

winner = None

while(winner is None):
    boolean = False
    player = players[player_index]
    position = players_position[player]
    total_same_colour_current_pos = 0
    # since everyone starts on GO, we just need to check go after the first roll
    data_length = len(data)

    position = (position + roll_data[roll_index])%data_length 
    players_position[player] = position
    # print(player, ' ',position)
    if(data[position]['type']) == 'go':
        money_owned[player] += 1
    elif(data[position]['type'] == 'property'):
        # check if the property is not owned by any players
        for p in players: 
            if(data[position]['name'] in properties_owned[p]):
                boolean = True
                break
        if(boolean == False):
            # check if it's buyable; if it is, buy(put in properties_owned); else; bankrupt
            if(money_owned[player] >= data[position]['price']):
                properties_owned[player].append(data[position]['name'])
                money_owned[player] -= data[position]['price']
                print(player,'buys ', data[position]['name'])
            # bankrupt?
            else:
                # end game print winner.
                print('Winner is ',max(money_owned, key=money_owned.get))
                break
        else:
            owner = ''
            for p in players:
                if(data[position]['name'] in properties_owned[p]):
                    owner = p
                    break
            
            rent_price = data[position]['price']

            if owner != player:
                for each in data:
                    # in the process of counting the same colours, we omit the go.
                    if(each['type'] == 'go'):
                            continue
                    if(each['colour'] == data[position]['colour']):
                        total_same_colour_current_pos +=1
                
                same_colour_owned = 0
                owned_JSON = []
                for each_string in properties_owned[owner]:
                    for j in data:
                        if(j['name'] == each_string):
                            owned_JSON.append(j)
                for each in owned_JSON:    
                    if(each['colour'] == data[position]['colour']):
                        same_colour_owned+=1

                if(total_same_colour_current_pos == same_colour_owned):
                    rent_price *= 2    
                # minus rent
                money_owned[player] -= rent_price
                money_owned[owner] += rent_price
                # print(player , 'pays rent to' ,owner, money_owned[player])
                # print(owner ,'got' ,money_owned[owner])
        if(money_owned[player] <= 0):
            print('Winner is ',max(money_owned, key=money_owned.get))
            break            
    #print(properties_owned[player])
    # next rolls.
    roll_index += 1
    player_index = (player_index + 1) % 4  # number of players
    boolean = False
f.close()

print()
print('Money owned : ',money_owned)
print('Properties owned : ',properties_owned)
print('Players positions: ',players_position)


roll.close()
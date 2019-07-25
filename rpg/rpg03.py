#!/usr/bin/python3
'''My RPG Game in my NAPYA Class'''

def showInstructions():
    print('''
    RPG Game
    Your task is to escape the house with the key and the potion.
    --------
    Commands:
        go [direction]
        get [item]
    ''')


def fight(health):
        while health != 0 :
            print('A monster has appeared!')
            print('Do you want to fight? (y/n)')
            decision = input() 
            if decision == 'y':
                print('You attack the monster!')
            else:
                print('The monster attacks you!')
                health = health - 25
                print('Your health is now ' + str(health) + ', You feel weary!')
            if health <= 0:
                print('You died!')
                break
        
def showStatus(): # display the player's status
    print('=================')
    print('You are in the ', currentRoom)
    # show inventory
    print('Inventory : ', str(inventory))
    # show item if one is in the room
    if 'item' in rooms[currentRoom]:
        print('You see a ', rooms[currentRoom]['item'])
    print('=================')
    print("Health: " + str(health))

# init a empty list
inventory = []

# create our world and its rooms
rooms = {
        'Hall' : {
            'south' : 'Kitchen',
            'east' : 'Dining Room',
            'item' : 'key'
            },
        'Kitchen' : {
            'north' : 'Hall',
            'item' : 'monster'
            },
        'Dining Room' : {
            'west' : 'Hall',
            'south' : 'Garden',
            'north' : 'Pantry',
            'item' : 'potion'
            },
        'Garden' : {
            'north' : 'Dining Room'
            },
        'Pantry' : {
            'south' : 'Dining Room',
            'item' : 'cookie'
            }
        }

# player start location
currentRoom = 'Hall'

# show instructions to the player
showInstructions()


# create an infinite loop
while True:
    health = 100
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>') # so long as the move does not
        # have a value. Ask the user for input

    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")

    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]] # add item to inv
            print(move[1] + ' received!') # msg saying you received the item
            del rooms[currentRoom]['item'] # deletes that item from the dictionary
        else:
            print('YOU CANNOT GET ', move[1], '!')

# if you enter the monster kitchen with a cookie
    if 'cookie' in inventory and 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('The monster steals your cookie and runs away!')
        inventory.remove('cookie')
        del rooms[currentRoom]['item']

    # gonna get eaten by a monster in the kitchen!
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has appeared!')
        fight(health)

        #print('A monster has got you! GAME OVER!')
        break # escape the loop

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("You escaped the house with the ultra rare key and the magic potion... YOU WIN!")
        break

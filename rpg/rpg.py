#!/usr/bin/python3

''' My RPG Game '''

def showInstructions():
    print('''
    RPG Game
    --------
    Commands:
        go [direction]
        get [item]
    ''')

def showStatus(): # display the player's status
    print('===============')
    print('You are in the', currentRoom)
    # show inventory
    print('Inventory: ', str(inventory))
    if 'item' in rooms[currentRoom]:
        print("You see a ' rooms[curentRoom]['item']")
    print('===============')

#init an empty list
inventory = []

rooms = {
        'Hall' : {
            'south' : 'Kitchen',
            'item' : 'key'
            },
        'Kitchen' : {
            'north' : 'Hall'
            }
        }
# player 
currentRoom = 'Hall'

# showInstructions()
showInstructions()

# create an infinite loop
while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>') # ask user for input
    move = move.lower().split()
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            # if YES that direction exists, then assign your
            # new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")
            if move[0] == 'get':
                    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                        del rooms[currentRoom]['item']




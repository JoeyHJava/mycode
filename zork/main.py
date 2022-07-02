#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live
from room import rooms

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print(f"You see a {rooms[currentRoom]['item']}")
  print("---------------------------")

def describeRoom():
  print( rooms[currentRoom]['description'])
  # print("---------------------------") 

def directionsYouCanTravel():
   a = ["north", "south", "east", "west"]
   print("you can travel ")
   for dir in a:
    if dir in  rooms[currentRoom]:
      print("You can travel " + dir.upper(),sep=' ', end='! ')
   


#an inventory, which is initially empty
inventory = []
#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
  showStatus()
  describeRoom()  
  directionsYouCanTravel()
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      print("in rooms.... ",  rooms[currentRoom])
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      print("...THIS GETS DESCRIPTION...",  rooms[currentRoom]['item'][move[1]]['desc'])
      #display a helpful message
      print(move[1] + ' got!')
      # print("REMOVE>.......", rooms[currentRoom])
      # print("REMOVE>.......", rooms[currentRoom]['item'])
      # print("REMOVE>.......", rooms[currentRoom]['item'].pop(move[1]))
      # print("REMOVE>.......", rooms[currentRoom]['item'])
      rooms[currentRoom]['item'].pop(move[1])
      #delete the item from the room
      if len(rooms[currentRoom]['item']) == 0:
        del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
        if move[1] not in rooms[currentRoom]['item']:
         print('Can\'t get ' + move[1] + '!')
      #tell them they can't get it
    #  move[1] not in rooms[currentRoom]['item']:
        # print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
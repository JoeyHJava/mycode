#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live
from room import rooms
import random
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
  
  # shows multiple items
  count = 0
  
  if "item" in rooms[currentRoom]:
    for key,value in rooms[currentRoom]['item'].items():
      count +=1
      print(f'{count}.{key}')
  print("---------------------------")

# describes the room
def describeRoom():
  print( rooms[currentRoom]['description'])
  # print("---------------------------") 

# describes every direction you can go
def directionsYouCanTravel():
   a = ["north", "south", "east", "west"]
   for dir in a:
    if dir in  rooms[currentRoom]:
      print("You can move " + dir.lower(),sep=' ', end='! ')

# teleport from Garage to anyroom using prompt. 
def teleport(cur_rm):
    if cur_rm == 'Garage':
        teleport = True
        if teleport == True:
            doTeleport = input("Would you like to teleport to a different room? ")
        doTeleport.lower()
        yes_no = ["y", "n"]
        if doTeleport in yes_no:
            if doTeleport == 'y':
                goToTelePortRoom()
            elif doTeleport == 'n':
                cur_rm == 'Garage'
                teleport = False
                showStatus()
                describeRoom()
                directionsYouCanTravel()
                # return
 
# heavy lifting of teleporting functionality
count = 0
def goToTelePortRoom():
    global currentRoom
    global count
    room = input('which room would you like to teleport to? ')
    if room in rooms.keys():
        currentRoom = room 
        showStatus()
        describeRoom()
        directionsYouCanTravel() 
        count = 0
    else:
        count +=1
        goToTelePortRoom()

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
  teleport(currentRoom)

  move = ''
  while move == '':
    move = input('>')
         
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
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
      #display a helpful message
      print(f'{move[1]}! {rooms[currentRoom]["item"][move[1]]} is a {move[1]}! {rooms[currentRoom]["item"][move[1]]["desc"]}')
      rooms[currentRoom]['item'].pop(move[1])
      #delete the item from the room
      if len(rooms[currentRoom]['item']) == 0:
        del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
        if move[1] not in rooms[currentRoom]['item']:
         print('Can\'t get ' + move[1] + '!')
      #tell them they can't get it
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'laptop' not in inventory:
    print('A monster has got you... GAME OVER!')
    break

    # survive encounter with the monster and teleport to random room
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'laptop' in inventory:
    anyRoomButThisRoom = []
    whichRoom = ""
    for item in rooms.keys():
        if currentRoom != item:
            anyRoomButThisRoom.append(item)
 
    whichRoom = random.choice(anyRoomButThisRoom)
    print(f"""You encountered a monster, under normal circumstances you would be dead, 
              however, you have a laptop in your inventory which prevented the monster from getting you! 
              You will be transported to the {whichRoom} """)
    currentRoom = whichRoom
    

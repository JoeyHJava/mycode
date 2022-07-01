
# This ended up being harder than I though
# Buggy code. Trying to fix
# I think I might be causing a recursive calls somewhere

import random
  
player_number = 0
count = 1
play = True



def test():
    try:
        num = int(input("-----Enter number "))
    except: 
        print("Please enter number between 1 - 10 ")
        test()
       
    else:
        player_number = num
        return player_number 


try:
    num = int(input("Enter number........ "))
except: 
    print("try again")
    test()
else:
    player_number = num

while play:

    monster_number = random.randint(1, 2)
    # 5 is hardcoded here for testing purpose
    if player_number == 5:
        print("You won....Get outta here....")
        break

    if count == 3:
        print("No more turns left")
        break

    if player_number != 5:
        print("You did not hit the monster.")

        test()
    elif play_again.upper() == "N":
        print("Good bye")
        play = False
    else:
        print("Inproper input!!")
        play_again = input("Would you like to play again? (Y/N) ")

    count += 1





































# while play:
#     monster_number = random.randint(1, 2)
#     player_number = 0
#     print("2-MOSTER Num", monster_number)
#     print("2--PLAYER Num", player_number)    

#     if player_number == monster_number:
#         print(monster_number, player_number, 'You WON')
#     else:
#         if count == 0:
#             num = input("Choos.....e a number between 1 - 10. ") 
#             player_number = int(num)
#         elif count < 4 and count != 0:
#             print(count)
#             answer = input("You did not hit the monster. Would you like to play again(y/n)?")
#             # if (answer != "T") or (answer !="F"):
#             print('answer', answer.lower())
#             # interact_with_player()
#             # play = True if( answer == t) else False
#             # print("play", play)
#             # break
#         elif count == 4:
#             print("Last change...")
#             # interact_with_player()
#             print("Good bye")
#             play == False
#             # player_number = int(num)
            
#     count = count + 1


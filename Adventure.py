print('''
*******************************************************************************
       _.--,_......----..__
       \  .'          '    ```--...__      \
        \;           '            .  '.   ||
        :           '            '     \ .''.
      .';          :            '       .|  |.--..___
     /   \         |           :        :|  /.------.\
    /    .'._      :           |        ||  ||      |\\
   /.-. /|-| `-.               :        ;|  ||______|_\`.______
  //  // |-|    \   '           '      / |  ||='      | |      `.
 //  //\\|-|     `-._'           '   .'  |  ||        | |        \
/.-.//  \\-|_________```------------` ___'. ||        | '_.--.   <)
'._.'  /  .-----.   .-----.   .''''''''.    |'--..____| /  _  \   |
       |_/.'   '.\_/.'   '.\_[ [ [  ] ] ]___|_________.'.'   '.\  ]
         :  .-.  : :  .-.  :  '........'    (_________):  .-.  :`-'
         :  '-'  : :  '-'  :                           :  '-'  :
          '._ _.'   '._ _.'                             '._ _.'LGB
*******************************************************************************
''')
print("Welcome to Follow the Truck.")
print("Your mission is to follow the truck to the destination to talk to the driver.")

direction = input("We have lost the truck! Did you see it go 'left' or 'right'? \n").lower()
if direction == "right":
    print("You got lost. Game over.")

elif direction == "left":
    action = input("Great! You caught up to the truck. Now, there\'s a yellow light."
                   "Do you want to \'drive\' through it or \'stop\'? \n").lower()

    if action == "drive":
        print("You got hit by a bus. Game over.")

    elif action == "stop":
        face_hair = input("Great! You didn't get hit by a bus. You drove on green and see the truck at the destination." 
                           " Did the driver have a beard, mustache, or shaved? \n").lower()
        if face_hair == "mustache":
            print("Game over. You did not talk to the driver.")

        if face_hair == "shaved":
                print("Game over. You did not talk to the driver.")

        if face_hair == "beard":
            print("You win! He paid you the money he owed you. Congratulations!")

else:
    print("You're input is incorrect. Game over.")
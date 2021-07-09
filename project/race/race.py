import random
from typing import Type

print("\n ----------------")
print("      賽馬      ")
print("作者: andongni0723")
print("----------------")

while True:
    money = 1000
    player = 6
    player_LI = ["Herry", "zoe", "andongni", "peter","ann", "den"]
    
    print("\n ----功能---- \n 1.SETTING \n 2.PLAY \n 3.QUIT \n ------------")
    mainMenu = input("Menu (number)? ")
   
    if(mainMenu == "1"):
        print("\n ----設定---- \n 1.money \n 2.player \n ------------")
        settingMenu = input("Menu (number)? ")
        
        if(settingMenu == "1"):
            
            # set the money
            setMoney = int(input("set the money (number) ? "))
            
            if(type(setMoney) != int or setMoney <= 0):
                print("\n ----ERROR---- \n settingERROR : the money setting has some problem , so setting canel \n please use interger and setting not less than 0 \n -------------")
            else:
                money = setMoney
                print("\n set success")
                
        elif(settingMenu == "2"):
            
            # set the player
            setPlayer = int(input("set the player (1~6)"))
            
            if(setPlayer > 6 or setPlayer <= 0):
                print("\n ----ERROR---- \n settingERROR : the player setting has some problem , so setting canel \n -------------" )
            else:
                player = setPlayer
                print("\n set success")
                
    elif(mainMenu == "2"):
        pass
    else:
        break
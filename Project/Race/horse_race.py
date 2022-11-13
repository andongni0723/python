import random
import time
import os

MinBetMoney = 100
inputDone = False
startMoney = 1000
startPlayer = 6
currentMoney = 1000
betMoney = 0
betPlayer = 1

# Class
class Horse:
    def __init__(self, index, name, minSpeed, maxSpeed):
        self.index = index
        self.name = name
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

# Funcation
def GameText(_textTittle,_type = "None", _Min = 0, _Max = 1):  
    if(_textTittle == "mainMenu"):
        return "======沈奕瑋======\n"\
               "1. Setting\n"\
               "2. Play\n"\
               "3. Quit\n"\
               "=================="

    elif(_textTittle == "line"):
        return "====================="

    elif(_textTittle == "mainMenu_input"):
        return f"Input menu index ({_type}, {_Min}~{_Max}): "
    
    elif(_textTittle == "settingMenu"):
        return "======Setting=======\n"\
               "1. Money\n"\
               "2. Player\n"\
               "====================="
    
    elif(_textTittle == "settingMenu_input"):
        return f"Input menu index ({_type}, {_Min}~{_Max}): "

    elif(_textTittle == "moneyMenu"):
        return ""

    elif(_textTittle == "moneyMenu_input"):
        return f"Input money of Game Start ({_type}, {_Min}~{_Max}): "
    
    elif(_textTittle == "playerMenu"):
        return ""

    elif(_textTittle == "playerMenu_input"):
        return f"Input pleyer of Game Start ({_type}, {_Min}~{_Max}): "
    
    elif(_textTittle == "settingDone"):
        return f"------Game Setting------\n"\
               f"Coin  : {startMoney}\n"\
               f"Player: {startPlayer}\n"\
                "------------------------\n"
    
    elif(_textTittle == "betsMenu"):
        return "======Bets======="
    
    elif(_textTittle == "betsPlayer"):
        return ""

    elif(_textTittle == "betsMoney"):
        return ""

    elif(_textTittle == "betsPlayer_input"):
        return f"Which player do you want to bet on ({_type}, {_Min}~{_Max}): "
    
    elif(_textTittle == "betsMoney_input"):
        return f"How much do you want to bet ({_type}, {_Min}~{_Max}): "
    
    elif(_textTittle == "gameStart"):
        return "============\n"\
               " GAME START \n"\
               "============\n"
    else:
        return "!!!GameTextError!!!"

def GameError(_errorType, _inputRule = "" ,_errorMsg = "Please confirm the input rule"):
    _errorText = f"\t==={_errorType}: {_errorMsg} ({_inputRule})===\n"
    return _errorText

def GemeMenuInput(_menuName: str, _type: str, _Min: int, _Max: int):
    inputDone = False
    print(GameText(_menuName))

    while not(inputDone):
        try:
            respond = int(input(GameText(f"{_menuName}_input",_type, _Min, _Max)))           
        except :
            print(GameError("Input Error", f"{_type}, {_Min}~{_Max}"))
        else:        
            if(not(_Min <= respond <= _Max)):
                print(GameError("Index Out of Range", f"{_type}, {_Min}~{_Max}"))
                continue
            inputDone = True

    inputDone = False
    time.sleep(0.5)
    os.system("cls")
    print()
    return respond

n = 10
a = "============================\n"\
    "Rank | No. |  Name  | Speed \n"\
    "----------------------------"
def Race():
    for i in range(11):
        os.system("cls")
        print(a)
        print(f"{i}st. | 1.  | 1      | {20-i} m/s \n"\
            "----------------------------")
        print(f"{i+1}st. | 2.  | 2      | {15-i} m/s \n"\
        "----------------------------\n")
        print(f'[{"█"*i}{" "*(n-i)}] {i*100/n}%')
        time.sleep(.5)



### MAIN ###
while True:
    try:
        ## Menu Input ##
        respond_Menu = GemeMenuInput("mainMenu", "Interger", 1, 3)   

        # Menu Index    
        if(respond_Menu == 1): ## Setting ##       
            respond_setting = GemeMenuInput("settingMenu", "Interger", 1, 2)

            # Setting Index
            if(respond_setting == 1):  ## Money       
                startMoney = GemeMenuInput("moneyMenu", "Interger", 100, 100000)
                print(GameText("settingDone")) # Output coin after setting

            elif(respond_setting == 2):## Player
                
                startPlayer = GemeMenuInput("playerMenu", "Interger", 2, 6)
                print(GameText("settingDone")) # Output horse after setting

        elif(respond_Menu == 2): ## Game Start ##
            print(GameText("gameStart"))
            currentMoney = startMoney

            ## Bets ## 
            print(GameText("betsMenu"))   
            betPlayer = GemeMenuInput("betsPlayer", "Interger", 1, startPlayer)
            betMoney = GemeMenuInput("betsMoney", "Interger", MinBetMoney, currentMoney)
            print(GameText("line"))

            ## Race ##  
            Race() #TODO:Race
        elif(respond_Menu == 3): ## Quit ##
            break
    except:
        print(GameError("Game Play Error", "None", "Don't click key during non-entering time"))
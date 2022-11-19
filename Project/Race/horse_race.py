import random as r
import time
import os

# Class
class Player:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.minSpeed = 5
        self.maxSpeed = 15
        self.speed = 0 
        
    def randomSpeed(self):
       self.speed = r.randint(self.minSpeed, self.maxSpeed)



MinBetMoney = 100
inputDone = False
startMoney = 1000
startPlayer = 6
currentMoney = 1000
betMoney = 0
betPlayer = 1    
PlayerList = [[Player(1, "A"), 0], [Player(2, "B"), 0], [Player(3, "C"), 0], [Player(4, "D"), 0], [Player(5, "E"), 0], [Player(6, "F"), 0]] # [player data, run distance]

# Funcation
def INIT():
    inputDone = False
    currentMoney = 1000
    betMoney = 0
    betPlayer = 1    
    PlayerList = [[Player(1, "A"), 0], [Player(2, "B"), 0], [Player(3, "C"), 0], [Player(4, "D"), 0], [Player(5, "E"), 0], [Player(6, "F"), 0]] # [player data, run distance]

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
    elif(_textTittle == "rankListTop"):
        return "==================================================\n"\
               "Rank\t| No.\t|  Name\t| Speed (m/s)\t| Distance\n"\
               "--------------------------------------------------"
    else:
        return "!!!GameTextError!!!"

def GameError(_errorType, _inputRule = "" ,_errorMsg = "Please confirm the input rule"):
    _errorText = f"\t==={_errorType}: {_errorMsg} ({_inputRule})===\n"
    return _errorText

def GemeMenuInput(_menuName: str, _type: str, _Min: int, _Max: int):
    inputDone = False
    print(GameText(_menuName))

    # Check respond is standards compliant
    while not(inputDone):
        try:
            respond = int(input(GameText(f"{_menuName}_input",_type, _Min, _Max)))    

        except :
            print(GameError("Input Error", f"{_type}, {_Min}~{_Max}"))

        else:
            # Input Index Out of Range       
            if(not(_Min <= respond <= _Max)): 
                print(GameError("Index Out of Range", f"{_type}, {_Min}~{_Max}"))
                continue
            inputDone = True

    
    inputDone = False
    time.sleep(0.5)
    os.system("cls") # Clear the CMD
    print()
    return respond

n = 10

def Race():
    # INIT
    isDone = False
    PlayerList = [[Player(1, "A"), 0], [Player(2, "B"), 0], [Player(3, "C"), 0], [Player(4, "D"), 0], [Player(5, "E"), 0], [Player(6, "F"), 0]] # [player data, run distance]
    RankList = []

    while not(isDone): 
        # Random players speed, and Calc players distance
        for i in range(startPlayer):
            PlayerList[i][0].randomSpeed()
            PlayerList[i][1] += PlayerList[i][0].speed
            RankList = sorted(PlayerList, key=lambda x: x[1], reverse=True)
            print(i)
        
        # Output race rank
        PrintRank(RankList)
        time.sleep(0.5)

        # the highest length is longer than 100, Race END
        if(RankList[0][1] >= 100):
            isDone = True

            # Print Rank
            st1, nd2 = f"{RankList[0][0].index}. {RankList[0][0].name}", f"{RankList[1][0].index}. {RankList[1][0].name}"
            rd3 =  f"{RankList[2][0].index}. {RankList[2][0].name}" if(startPlayer > 2) else ""  # if only 2 players, the race hasn't 3rd 

            print(f"         {st1}        \n"\
                  f"        ======        \n"\
                  f"  {nd2} |  1  |  {rd3}\n"\
                  f"=======       ======= \n"\
                  f"|   2           3   | \n"\
                  f"--------------------- \n")

def PrintRank(_RankList):
    os.system("cls")
    print(GameText("rankListTop"))
    
    for i in range(startPlayer):
        print(f"{i+1}st.\t| {_RankList[i][0].index}\t| {_RankList[i][0].name}\t| {_RankList[i][0].speed} m/s \t| {_RankList[i][1]} m\n"\
               "--------------------------------------------------")

    print(f'[{"█"* (_RankList[0][1] // 2)}{" "* (50- (_RankList[0][1] // 2))}] {_RankList[0][1]}m')




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
            Race() 

            # TODO: After race
        elif(respond_Menu == 3): ## Quit ##
            break

    except Exception as error:
        print(error)
        print(GameError("Game Play Error", "None", "Don't click key during non-entering time"))
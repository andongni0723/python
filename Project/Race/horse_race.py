import random

inputDone = False
startMoney = 1000

# Class
class Horse:
    def __init__(self, index, name, minSpeed, maxSpeed):
        self.index = index
        self.name = name
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

# Funcation
def GameText(_textTittle,_type, _Min, _Max):
    if(_textTittle == "mainMenu"):
        return "======沈奕瑋======\n"\
               "1. Play\n"\
               "2. Setting\n"\
               "=================="

    elif(_textTittle == "mainMenu_input"):
        return f"Input menu index ({_type}, {_Min}~{_Max}): "
    
    elif(_textTittle == "settingMenu"):
        return "======Setting=======\n"\
               "1. Money\n"\
               "2. Horse\n"\
               "====================="
    
    elif(_textTittle == "settingMenu_input"):
        return f"Input menu index ({_type}, {_Min}~{_Max}): "

    elif(_textTittle == "moneyMenu"):
        return ""

    elif(_textTittle == "moneyMenu_input"):
        return f"Input money of Game Start({_type}, {_Min}~{_Max}): "
    
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
    print()
    return respond



### MAIN ###
while True:
    ## Menu Input ##
    respond_Menu = GemeMenuInput("mainMenu", "Interger", 1, 2)   

    # Menu Index    
    if(respond_Menu == 2): 
        ## Setting ##
        respond_setting = GemeMenuInput("settingMenu", "Interger", 1, 2)

        # Setting Index
        if(respond_setting == 1):
            ## Money
            startMoney = GemeMenuInput("moneyMenu", "Interger", 100, 100000)

            #TODO: show money
        
    break
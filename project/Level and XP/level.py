print("""\n
#*///////////////////////////  Andongni0723  /////////////////////////////*#
#                         Level_and_Xp Tool v1.0                           #
#   python 3.10.2                                                          #
#   data: 2022/2/9                                                         #
#   github repo: https://github.com/andongni0723/python.git                #
#*////////////////////////////////////////////////////////////////////////*#""")
BASIC_LEVEL_UP_XP = 10 # Level max xp = Level num * 10

def Error(errorText):
    print("\n\t/////////////////ERROR///////////////// \n\t{}\n\t///////////////////////////////////////" .format(errorText))

while True:
    #### Input Mode ####
    try:      
        mode = int(input("""
        ----------------------Mode--------------------
        1. Input Xp           => Level and Xp Bar
        2. Input Level and % => Xp
        3. Quit
        ----------------------------------------------
        Input Mode: """))
    except:
        Error("Please input mode(Interger) Ex. 1, 2...")
        continue

    #### Main ####
    match(mode):
        case 1: # Load

            # Input Value
            try:
                input_xp = int(input("\n\t------------Input------------\n\tXp(Input a int > 0): "))

                if(input_xp < 0):
                    Error("Please input xp(Interger > 0) Ex. 100, 200...")
                    continue
            except:
                Error("Please input xp(Interger > 0) Ex. 100, 200...")
                continue

            # Xp => Lv. and bar
            cal_xp = 0
            level_max_xp = 10 # Lv.1 max xp
            now_Lv = 1
            isOn = True

            while isOn:
                if(input_xp-cal_xp < level_max_xp):
                    isOn = False
                    break

                cal_xp += level_max_xp
                now_Lv += 1
                level_max_xp = now_Lv * BASIC_LEVEL_UP_XP

            # Output Value
            xp_percentage_float = (input_xp-cal_xp) / level_max_xp * 100
            xp_percentage_To_20_int = int(xp_percentage_float)// 5

            xpBar_full_char = "■" * xp_percentage_To_20_int
            xpBar_null_char = " " * (20 - xp_percentage_To_20_int)

            print("\n\t--------------Output--------------")
            print("\tLv.{} |{}{}| {:.2f}% {}/{}" .format(now_Lv, xpBar_full_char,xpBar_null_char, xp_percentage_float, input_xp-cal_xp, level_max_xp))
            print("\t----------------------------------\n")

            ready = input("\tEnter any key to continue... ")

        case 2: # Save

            # Input Value
            try:
                input_level = int(input("\n\t------------Input------------\n\tLevel(Input a int >= 1): "))

                if(input_level <= 0):
                    Error("Please input a Interger (and >= 1) Ex. 1, 2...")
                    continue
            except:
                Error("Please input a Interger (and >= 1) Ex. 1, 2...")
                continue

            input_max_xp = input_level * BASIC_LEVEL_UP_XP

            try:
                input_level_xp = eval(input("\n\tLevel xp(Input a int and < {}): " .format(input_max_xp)))

                if(input_level_xp < 0 or input_level_xp > input_max_xp):
                    Error("Please input Int (and < {})" .format(input_max_xp))
                    continue
            except:
                Error("Please input Int (and < {})" .format(input_max_xp))
                continue

            # Lv. and bar => Xp
            now_xp = 0
            for i in range(1,input_level):
                now_xp += i * 10

            now_xp += input_level_xp

            print("\n\t--------------Output--------------")
            print("\txp | {}" .format(now_xp))
            print("\t----------------------------------\n")

            ready = input("\tEnter any key to continue... ")

        case 3:
            break
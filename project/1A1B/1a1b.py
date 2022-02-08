# file  : 1A2B
#
# github: https://github.com/andongni0723
# date  : 2021/8/23
  
import random 
import os

# 創建 正確答案
answerList = random.sample(range(10), 4)
#print(answerList)

# MAIN
answerTime = 1
iscorrect = False
a = 0
b = 0

while True:
    answerInput = input("猜答案 (4個數字 0~9): ")
    
    # 去除 重複數字
    set_answerInput = set(answerInput)
    # 檢查 字數
    if(len(set_answerInput) != 4):
        print("--------------\n重新輸入\n--------------\n")
        continue
    
    answerInputList = list(map(int, list(answerInput)))  # 把 str變成list，再變成 int串列
    
    # 判斷 幾A 幾B
    for k in range(0,4) :
        for l in range(0,4):
            if(answerInputList[k] == answerList[l] and k == l):
                a += 1
            elif(answerInputList[k] == answerList[l]):
                b += 1
    
    # 結果            
    print("\n--------------\n第 ",answerTime," 次結果\n")
    print(a,"A", b, "B\n--------------\n\n")
   
    # 是否 結束
    if(answerTime == 8 or a == 4):
        break
    else:
        a = 0  
        b = 0
        answerTime += 1

# 是否 獲勝
answer = "".join('%s' %id for id in answerList)  # 把 正確答案 變 字串 (list to string)

if(answerInputList == answerList): 
    print("******** WIN ********\n\n 你贏了，答案是 {}\n\n**********************\n".format(answer))
else:
    print("******** LOSE ********\n\n 你輸了，答案是 {}\n\n**********************\n".format(answer))
    
os.system("pause")
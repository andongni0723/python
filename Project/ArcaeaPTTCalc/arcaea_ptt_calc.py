difficulty = eval(input("Input difficulty: "))
score = eval(input("Input score: "))
ptt = 0

if score >= 10_000_000:
    ptt = difficulty + 2
elif 9_800_000 <= score < 10_000_000:
    ptt = difficulty + 1 + (score - 9_800_000) / 200_000
else:
    ptt = difficulty + (score - 9_500_000) / 300_000

print("After calculation, the potential is {:.2f}".format(ptt))

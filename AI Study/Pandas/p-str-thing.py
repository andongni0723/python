import numpy as np
import pandas as pd

tit = pd.read_csv("titanic.csv")

# print(tit["Name"].str.lower()[:3])
# print(tit["Name"].str.upper()[:3])
# print(tit["Name"].str.len()[:3])
# print(tit["Name"].str.strip().str.lower().str.replace(" ", "_"))
#
# tit['lastName'] = tit['Name'].str.split(',').str[0]
# print(tit.head())


# axis = 0, |||
# axis = 1, ---

def msg(x):
    sex = "He" if x["Sex"] == "male" else "She"
    sur = "survived" if x["Survived"] else "Died"
    result = "{} is {}".format(sex, sur)
    return result


tit["Message"] = tit.apply(msg, 1)
print(tit.head())

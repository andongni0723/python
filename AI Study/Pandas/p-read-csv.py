import numpy as np
import pandas as pd

tit = pd.read_csv("titanic.csv")

print(tit)
print()
# print(tit.shape)

# print(tit.head())
# print(tit.tail(3))
# print(tit.sample(3))
# print(tit.describe()) # 數據分布
# print(tit.info())
# print(tit.dtypes)
# print(tit['Sex'].unique())

# print(tit[['Sex', "PassengerId"]].groupby(["Sex"]).count())
#         PassengerId
# Sex
# female            3
# male              2

survive_by_class = tit[['Pclass', "Survived", "PassengerId"]].groupby(['Pclass', 'Survived']).count()
survive_by_class = survive_by_class.rename(columns={'PassengerId': 'count'})
# print(survive_by_class)
#                  count
# Pclass Survived
# 1      1             2
# 3      0             2
#        1             1

'''
Logic calc
~ not
& and
| or
'''


#
# fil = (tit['Age'] > 30)
# print(tit.loc[fil, :])

def pt_25(x):
    return x.quantile(0.25)


def pt_75(x):
    return x.quantile(0.75)


age_age = tit[['Pclass', "Survived", "Age"]].groupby(['Pclass', 'Survived']).agg(
    ['min', 'max', 'median', len, 'std', pt_25, pt_75]
)
# print(age_age)

age_med: pd.Series = age_age.loc[:, ('Age', "median")]
# age_med: pd.DataFrame = age_med.to_frame()
print(age_med)
print(age_med.name)
print(age_med.values)
print(age_med.index)


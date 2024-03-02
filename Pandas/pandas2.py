import pandas as pd
import numpy as np
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.


data=pd.DataFrame(np.random.rand(10,8), columns=list("abcdefgh"))
pd.options.display.max_rows = 1
print(data)
print(data.to_string()) # to_string() to [rint all data

sequence = np.arange(1, 11, 2)
sequence = np.arange(1, 11)

a = [[1, 7, 2], [6,78,4]]

myvar = pd.Series(a)

print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
myvar2 = pd.DataFrame(calories, index=[0, 1, 2])
print(myvar)
print(myvar2)
print(myvar2.loc[0, "day2"])

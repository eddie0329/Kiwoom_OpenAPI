import sqlite3
import pandas as pd
from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4], 'col1': [10, 20, 30, 40], 'col2':[100, 200, 300, 400]}
df = DataFrame(raw_data)

print(df)

con = sqlite3.connect("c:/Users/LG/kospi.db")


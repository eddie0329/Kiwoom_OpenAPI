import pandas as pd
from pandas import Series, DataFrame
import sqlite3

con = sqlite3.connect("c:/Users/LG/kospi.db")

df = pd.read_sql("SELECT * FROM kakao", con, index_col=None)

print(df)
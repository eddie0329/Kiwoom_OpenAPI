import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)
#gs = web.DataReader("078930.KS", "yahoo", start, end)
gs = web.DataReader("078930.KS", "yahoo")

#printing the gs.info()
#print(gs.info())

#result = [<matplotlib.lines.Line2D object at 0x09551990>]
#print(plt.plot(gs['Adj Close']))

#ploting the plots
#print(plt.show())

#Turning the x-axis into data(year)
print(gs.index)
print(plt.plot(gs.index, gs['Adj Close']))
print(plt.show())


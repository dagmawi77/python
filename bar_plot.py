import matplotlib.pyplot as py
import numpy as num

x = num.array(["A","B","C","D"])
y = num.array([10,30,25,45])

py.bar(x,y)
py.show()

x = ["APPLES", "BANANAS"]
y = [400, 350]
py.bar(x, y)
py.show()

x = num.array(["A","B","C","D"])
y = num.array([10,30,25,45])

py.barh(x,y,color="red")
py.show()

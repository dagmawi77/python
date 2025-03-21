import matplotlib.pyplot as pt
import numpy as py

x = py.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = py.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

pt.scatter(x,y)

pt.show()

#day one, the age and speed of 13 cars:
x = py.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = py.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
pt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = py.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = py.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
pt.scatter(x, y)

pt.show()

x = py.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = py.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
pt.scatter(x, y, color = 'hotpink')

x = py.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = py.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
pt.scatter(x, y, color = '#88c999')

pt.show()


x = py.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = py.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = py.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

pt.scatter(x, y, c=colors)


x = py.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = py.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = py.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

pt.scatter(x, y, c=colors, cmap='viridis')

pt.colorbar()



pt.show()

x = py.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = py.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = py.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

pt.scatter(x, y, s=sizes)

pt.show()


x = py.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = py.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = py.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

pt.scatter(x, y, s=sizes, alpha=0.5)

pt.show()

x = py.random.randint(100, size=(100))
y = py.random.randint(100, size=(100))
colors = py.random.randint(100, size=(100))
sizes = 10 * py.random.randint(100, size=(100))

pt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

pt.colorbar()

pt.show()
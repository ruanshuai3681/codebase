import matplotlib.pyplot as plt
import numpy
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# to fit a polynomial of degree 3 to the data points (x, y) using NumPy's polyfit()
mymodel = numpy.poly1d(numpy.polyfit(x, y, 4)) #create a one-dimensional polynomial object using poly1d()
#The coefficients variable will hold an array of coefficients, with the first element being the coefficient of the highest degree term
myline = numpy.linspace(1, 22, 100)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)


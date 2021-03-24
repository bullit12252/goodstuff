from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt










def reading_the_file(sourcefile):

    f = open(sourcefile, 'r')
    thewholetext = f.readlines()
    x = []
    y = []
    for i in thewholetext:
        x.append(float(i[:i.find('\t')].replace(",",".")))
        y.append(float(i[i.find('\t'):i.find('\n')+1].replace(",",".")))
    return x, y

def calculating_integral(x, y):
    minimum = min(y)
    new_y = []
    new_x = []
    integral = 0
    for i in range(len(x)):
        if x[i] >= 300 and x[i] <= 500:
            new_x.append(x[i])
            new_y.append(y[i]-minimum)
    for i in range(len(new_x)-1):
        integral += (new_x[i+1] - new_x[i])* new_y[i]
    return(integral)



sourcefile = 'source.txt'
xax, yax = reading_the_file(sourcefile)
minimum = min(yax)
new_yax = []
for i in yax:
    new_yax.append(i - minimum)
print(new_yax)
cs = CubicSpline(xax, new_yax)
print(cs.integrate(300,500))
print(calculating_integral(xax, cs(xax)))

plt.plot(xax, cs(xax))
plt.show()


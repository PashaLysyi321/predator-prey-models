import math
import matplotlib.pyplot as plt

a = 1.72
b = 2.11
c = 1.31
d = 0.77
x = 2.99
y = 1.96
t1 = 13
t2 = 43
e = 0.001

h = e**(1/4)
h1 = h / 2

print('\nsystem is:\n\ndx/dt ={}x-{}xy'.format(a,b))
print('dx/dt =-{}y+{}xy\ny(t0)=y(0),x(t0)=x(0)\n'.format(c,d))


def f1(x,y):
    return -c*y+d*x*y
  
  
def f2(x,y):
    return a*x-b*x*y


yh = []
xh = []
check = True


def Runge_Kytta(h):
        k1 = h*f1(x,y)
        q1 = h*f2(x,y)
        k2 = h*f1(x+q1/2, y+k1/2)
        q2 = h*f2(x+q1/2, y+k1/2)
        k3 = h*f1(x+q2/2, y+k2/2)
        q3 = h*f2(x+q2/2, y+k2/2)
        k4 = h*f1(x+q3, y+k3)
        q4 = h*f2(x+q3, y+k3)
        m = y + (k1+2*k2+2*k3+k4)/6
        m1 = x + (q1+2*q2+2*q3+q4)/6
        yh.append(m)
        xh.append(m1)
 
 
while check:
    Runge_Kytta(h)
    Runge_Kytta(h/2)
    R1 = abs(xh[0] - xh[1])/(2**4 - 1)
    R2 = abs(yh[0] - yh[1])/(2**4 - 1)
    R = max(R1,R2)
    if R<e:
        check = False
        print('R is {} < 0.001'.format(R))
        print('h is {}'.format(h))
    else:
        print('R is {} > 0.001'.format(R))
        h = h/2 
        yh = []
        xh = []


t = [t1]
yres = [y]
xres = [x]

while t1 < t2:
    t.append(t1+h)
    t1 = t1+h
    k1 = h*f1(x,y)
    q1 = h*f2(x,y)
    k2 = h*f1(x+q1/2, y+k1/2)
    q2 = h*f2(x+q1/2, y+k1/2)
    k3 = h*f1(x+q2/2, y+k2/2)
    q3 = h*f2(x+q2/2, y+k2/2)
    k4 = h*f1(x+q3, y+k3)
    q4 = h*f2(x+q3, y+k3)
    m = y + (k1+2*k2+2*k3+k4)/6
    m1 = x + (q1+2*q2+2*q3+q4)/6
    yres.append(m)
    xres.append(m1)
    y = m
    x = m1
    

plt.scatter(t,xres, s = 2, c = 'lime', label = 'prey')
plt.scatter(t,yres, s = 2, c = 'darkcyan', label = ' predators')
plt.style.use('ggplot')
plt.xticks([13,16,19,22,25,28,31,34,37,40,43])
plt.xlim([13,43])
plt.xlabel('t')
plt.title('X/ Y vs t')
plt.legend(loc = 'upper left')
plt.show()

plt.scatter(xres,yres, s = 2, c = 'darkcyan')
plt.style.use('ggplot')
plt.title('X vs Y')
plt.annotate('Critical point', xy = (1.801,0.815))
plt.scatter(1.701,0.815, c = 'red')
plt.show()

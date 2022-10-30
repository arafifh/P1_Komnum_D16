# SOURCE
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://www.codesansar.com/numerical-methods/bisection-method-python-program.htm

import matplotlib.pyplot as plot
import numpy


x0 = float(input('input x0: '))
x1 = float(input('input x1: '))
err = float(input('input error (semakin kecil semakin akurat): '))

def f(x):
    return x**3 - x**2 + 2*x + 1

def bisection(x0, x1, err):
    totIterasi = 1
    condition = True

    while condition:
        xt = (x0 + x1) / 2
        print("Iterasi-%d, xt = %0.6f dan f(xt) = %0.6f" %(totIterasi, xt, f(xt)))

        if f(x1)*f(xt) > 0 :
            x1 = xt
        else:
            x0 = xt

        totIterasi += 1
        condition = abs(f(xt)) > err

    return xt


if f(x0) * f(x1) > 0.0:
    print("Pengoperasian f(x) keluar dari constraint")
else:
    akar = bisection(x0, x1, err)
    print("\nHasil akar : %0.8f" %akar)

x = numpy.arange(x0, x1, err)
y = f(x)

def buildGraph():
    plot.plot(x, y, color = "#C94023", label="grafik fungsi", zorder=0)
    plot.axvline(x=akar, ymin=0, ymax=1, color="cyan", zorder=1)
    plot.scatter(akar, f(akar), color="blue", linewidths=0.5, label="akar", zorder=2)
    plot.xlabel("x-axis")
    plot.ylabel("y-axis")
    plot.title("Grafik Fungsi Metode Bolzano")
    plot.legend()
    plot.grid()
    plot.show()

buildGraph()
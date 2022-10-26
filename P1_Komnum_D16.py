# SOURCE
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://www.codesansar.com/numerical-methods/bisection-method-python-program.htm

import matplotlib.pyplot as plot
import numpy

def f(x):
    return x**3 - 3 * x + 1

def bisection(x0, x1, e):
    count = 1
    condition = True

    while condition:
        x2 = (x0 + x1) / 2
        print("Iteration-%d, x2 = %0.6f and f(x2) = %0.6f" %(count, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        count += 1
        condition = abs(f(x2)) > e

    return x2

x0 = 1
x1 = 2
e = 0.1

if f(x0) * f(x1) > 0.0:
    print("Given values do not bracket the root.")
    print("Try Again with different guess values.")
else:
    root = bisection(x0, x1, e)
    print("\nRequired Root is : %0.8f" %root)

x = numpy.arange(x0, x1, e)
y = f(x)

def buildGraph():
    plot.plot(x, y, color = "#ff007f", label="function graph", zorder=0)
    plot.axvline(x=root, ymin=0, ymax=1, color="pink", zorder=1)
    plot.scatter(root, f(root), color="red", linewidths=0.5, label="root", zorder=2)
    plot.xlabel("x-axis")
    plot.ylabel("y-axis")
    plot.title("bolzano method")
    plot.legend()
    plot.show()

buildGraph()
from math import*
import sys


sp = sys.argv
if len(sp) == 1:
    sp = [-1, 1]
else:
    sp = list((int(sp[1]), int(sp[2])))
x = (sp[1] + sp[0]) / 2
delta = abs((sp[1] - sp[0]))


def f(x):
    hk = -1 * (x**2)
    return asin((2 * x) / (1 + x**2)) - e**hk


print("Введите e (эпсилон) в виде обыкновенной дроби")
a, b = map(int, input().split())
eps = abs(a/b)


while delta >= 2*eps:
    k = f(x)
    if f(x) > 0:
        sp[1] = x
    elif f(x) < 0:
        sp[0] = x
    else:
        print(x)
        break
    x = (sp[1] + sp[0]) / 2
    delta = abs((sp[1] - sp[0]))
else:
    print((sp[1] + sp[0]) / 2)



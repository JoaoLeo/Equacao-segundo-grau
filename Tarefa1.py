from math import sqrt

def delta(a=0,b=0,c=0):
    res_Delta = (b*b) - (4*a*c)
    return res_Delta

a = float(input("A= "))
b = float(input("B= "))
c = float(input("C= "))

if delta(a,b,c,) < 0 :
    print("Não possui raizes reais")

else:
    if delta(a,b,c,) == 0:
        raiz = sqrt(delta(a,b,c))
        res1 = (-b + raiz) / (2*a)
        print(f"Ambas as raizes são {res1}")

    elif delta(a,b,c) > 0:
        raiz = sqrt(delta(a,b,c))
        res1 = (-b + raiz) / (2*a)
        res2 = (-b - raiz) / (2*a)
        print(f"As raizes são {int(res1)} e {int(res2)}")

def multiplication(n):
    for g in range(1, 11):
        k = g*n
        print(g, "*", n, "=", k)


def multiplication2(m, inf, sup):
    for i in range(inf, sup+1):
        print(m, "*", i, "=", i*m)


def triangle(n):
    for i in range(1, n+1):
        print(" "*(n-i),"* "*i)


def maximum(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c


def diviseurs(n):
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)

    return l


def cube(n):
    return n*n*n


def surface_triangle(h, b):
    return (h*b)/2


def somme_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + i

    return s


s = somme_n(5)
print(s)
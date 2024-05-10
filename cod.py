import numpy as np

def f_a(x):
    return x*np.sin(x)

def f_b(x):
    return x*np.log(x)

def f_c(x):
    return 1/x

def f_d(x):
    return (x**2)*np.log(x+1)

def f_e(x):
    return np.exp(-x**2)

def trapezio_simples(a, b, f):
    return (b-a)*(f(a)+f(b))/2

def trapezio_composta(a, b, n, f):
    h = (b-a)/n
    resultado = 0.5*(f(a)+f(b))
    for i in range(1, n):
        resultado += f(a+i*h)
    return resultado*h

def simpson_um_terco(a, b, f):
    h = (b-a)/2
    return h/3*(f(a)+4*f((a+b)/2)+f(b))

limite = [(0.5, 1), (1.2, 1.5), (3, 3.6), (1.2, 1.4), (1.2, 1.6)]
funcao = [f_a, f_b, f_c, f_d, f_e]
n_pts = 100

for i in range(5):
    a, b = limite[i]
    f = funcao[i]

    print(f"Para a integral {chr(97+i)}:")
    print(f"Trapézio Simples: {trapezio_simples(a, b, f)}")
    print (f"Trapézio Composta: {trapezio_composta(a, b, n_pts, f)}")
    print(f"Simpson 1/3: {simpson_um_terco(a, b, f)}\n")
import sympy as sy

sy.init_printing()
x, y = sy.var('x, y')


# declaração de função
f = sy.Lambda(x, (x**2))
g = sy.Lambda(x, (x**3 - 3*x + 2) * sy.exp(-x/4) - 1)

# resultado derivada
result1 = sy.diff(f(x), x)
sy.print_rcode(result1)

# Para avaliar a derivada em um ponto, por exemplo, para calcular  f′(1) , digitamos:
result2 = sy.diff(g(x), x).subs(x, 1)
sy.print_rcode(result2)

## Reta Tangente
fl = sy.Lambda(x, sy.diff(f(x), x))

x0 = -1/2
r = sy.Lambda(x, fl(x0)*(x-x0) + f(x0))
r

# sy.plot(f(x), (x,-2,2))

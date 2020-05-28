import sympy as sy

sy.init_printing()

x, y = sy.var('x y')

## declaração de função
f = sy.Lambda(x, (x**3 - 3*x + 2) * sy.exp(x/4) - 1)

## limite da função com f(x), com o x tendendo a 1
ponto = 1
limit = sy.limit(f(x), x, ponto)

## print limit
sy.print_rcode(limit)

## limites laterais
z = sy.var('z')
g = sy.Lambda(z, (abs(z))/z)

limiteDireita = sy.limit(g(z), z, 0, '+')
esquerda = sy.limit(g(z), z, 0, '-')

sy.print_rcode(limiteDireita)
sy.print_rcode(esquerda)

## limites ao infinito
## limit(f(x), x, oo)
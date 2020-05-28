import sympy as sy

##from sympy.printing import print_rcode
##from sympy.functions import sin, cos, Abs, sqrt
##from sympy import Lambda
## from sympy.abc import x

sy.init_printing()

## criando variavel simbolica
x = sy.var('x')

## definindo uma função
f = sy.Lambda(x, 2 - sy.sqrt(x**2 - 1))

## f de 1
sy.print_rcode(f(1))

## imprimindo o grafico da função f
sy.plot(f(x))



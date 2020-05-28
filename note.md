## link para o material do professor.
https://phkonzen.github.io/notas/


## install 
```bash
python -m pip install -U pip    
python -m pip install -U matplotlib
```

## vs code

https://stackoverflow.com/questions/43574995/visual-studio-code-pylint-unable-to-import-protorpc



















// anotações aula 

g
limit(g(x),g,1)

#digite sua resposta aqui!
g = Lambda(x, 2 - sqrt(x**2 - 1))
g
limit(g(x),x,-1)


#digite sua resposta aqui!
limit(1/x, x, 0) ## limite pela direita

#limite pela esquerda
limit(1/x, x, 0, '-')


limit(f(x), x, oo)

limit((1 + 1/x)**x ,x, oo)

limit((1 + 1/x)**x ,x, oo)
limit((1 + 1/2*x** x), x, -oo)
limit(sin(x), x, oo)



## derivadas

from sympy import *
init_printing()
var('x,y')

f = Lambda(x, (x**3 - 3*x + 2)*exp(-x/4) - 1)
f

diff(f(x), x)

## Para avaliar a derivada em um ponto, por exemplo, para calcular  𝑓′(1) , digitamos:
diff(f(x),x).subs(x,1)

## derivada igual a zero = ponto critico

## Também, podemos definir a função derivada de  𝑓  com o seguinte código:
fl = Lambda(x, diff(f(x),x))
fl


## Sendo  𝑔(𝑥)=𝑥2+12  calcule  𝑔′(1) .

diff(x**2 + 1/2, x).subs(x,1)

## Reta Tangente

x0 = -1/2
r = Lambda(x, fl(x0)*(x-x0) + f(x0))
r


%matplotlib inline
p = plot(f(x), (x,-2,2), line_color='blue', show=False)
q = plot(r(x), (x,-1.5,1), line_color='red', show=False)
p.extend(q)
p.show()



## Encontre a reta tangente ao gráfico de  𝑦=1𝑥  em  𝑥=1 . Faça os esboços dos gráficos da função e da reta tangente em um mesmo gráfico.
#digite a resolução aqui.
g = Lambda(x, 1/x)
gl = Lambda(x, diff(y(x),x)) ## função da derivada de g
x0 = 1

r = Lambda(x, yl(x0)*(x-x0) + y(x0))
%matplotlib inline
p = plot(y(x),xlim=[-5,5],ylim=[-5,5], line_color='green', show=False)
q = plot(r(x),xlim=[-5,5],ylim=[-5,5], line_color='red', show=False)

p.extend(q)
p.show()


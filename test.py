from sympy import Symbol,Function,dsolve,diff,sqrt,pi
x = Symbol("x")
k = Symbol("k")
f = Function("f")
#print(f(x).diff(x,x)+f(x))
#print(dsolve(f(x).diff(x,x)+f(x),f(x)))
print(dsolve(f(x).diff(x)-2*sqrt(pi)*k*sqrt(f(x)),f(x)))


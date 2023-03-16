from sympy import *
x,y,z=symbols('x,y,z')
u=x*y/z
v=y*z/x
w=z*x/y

dux=diff(u,x)
duy=diff(u,y)
duz=diff(u,z)
dvx=diff(v,x)
dvy=diff(v,y)
dvz=diff(v,z)
dwx=diff(w,x)
dwy=diff(w,y)
dwz=diff(w,z)

J=Matrix([[dux,duy,duz],[dvx,dvy,dvz],[dwx,dwy,dwz]])
print("The Jacobian matrix is\n")
print(J)

Jac=det(J).doit()
print('\n\nJ = ',Jac)

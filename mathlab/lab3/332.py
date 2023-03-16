from sympy import *
x,y,z=symbols('x,y,z')

u=x+3*y**2-z**3
v=4*x**2*y*z
w=2*z*z**2-x*y

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
print(Jac)

J1=J.subs([(x,1),(y,-1),(z,0)])
print('\n\n J at (1,-1,0):\n')

Jac1=det(J1).doit()
print(Jac1)

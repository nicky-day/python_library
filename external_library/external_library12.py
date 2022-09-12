import sympy

x, y = sympy.symbols("x y")
f1 = sympy.Eq(x + y, 10)
f2 = sympy.Eq(x - y, 4)
sympy.solve([f1, f2])

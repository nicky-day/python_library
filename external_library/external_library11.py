import sympy

x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
sympy.solve(f)

from fractions import Fraction
from math import remainder
import sympy

x = sympy.symbols("x")
# x, y = sympy.symbols("x y")

f = sympy.Eq(x * Fraction("2/5"), 1760)
result = sympy.solve(f)
result

remains = result[0] - 1760
remains

print("남은 돈은 {}원입니다.".format(remains))

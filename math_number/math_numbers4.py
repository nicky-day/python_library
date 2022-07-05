from fractions import Fraction

a = Fraction(1, 5)
print(a)
a = Fraction("1/5")
print(a)
print(a.numerator)
print(a.denominator)

result = Fraction(1, 5) + Fraction(2, 5)
print(result)
print(float(result))

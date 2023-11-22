import math

a = 0.94 * 10**(-3)
x = 0.093

result1 = math.acos(x ** 2)
result2 = a * (x / (a * a * a)) ** (1 / 2)
result3 = ((math.sin(math.pi / 2)) ** 3) / math.log10(2 * x)
result = result1 - result2 + result3
print(result)

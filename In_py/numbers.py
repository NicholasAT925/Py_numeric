a = 12
b = 3
c = 15.0
d = 4.0

print("a + b =",a + b, "Addition")
print("a - b =",a - b, "subtraction")
print("a * b =",a * b, "multiplication")
print("a / b =",a / b, "division")
print("a // b =",a // b, "Floor division")
print("a % b =",a % b, "modulus")
print("\n\n")
print("c + d =", c + d, "addition")
print("c - d =", d - c, "subtraction")
print("c * d =", c * d, "multiplication")
print("c / d =", c / d, "division")
print("c // d =", c // d, "floor division")
print("c % d =", c % d, "modulus" )
print("\n")

for i in range(1, a//b): # Small practice with range()
    print(i)

print("\n")
# for i in range(1, c//d): # this is wrong as float cannot be interpreted as int
#     print(i)

# Small challenge a bun cost 2.40 each you have 15 only how much bun can you buy

bun = 2.40
cash = 15
ans = cash // bun
print(ans)
x2 = 10
def add(x1):
   global x2
   x2 = 20 # グローバル変数 x2 を 20 に
   result = x1 + x2
   print(result)

print(x2)
add(5)
print(x2)

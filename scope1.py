x2 = 10 # 関数の外側で変数x2を作成(グローバル変数)
def add(x1):
   x2 = 20 # 関数内で変数を作成(ローカル変数)
   result = x1 + x2
   print(result)

print(x2)
add(5)
print(x2)

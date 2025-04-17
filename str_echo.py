def str_echo(s):
    '''文字列sを2回繰り返した
       文字列を生成する'''
    s = s + s
    return s

a = 'abc'
b = str_echo(a)

print(b) # これはきっと 'abcabc'
print(a) # こっちは?

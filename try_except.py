astr = "fourtytwo"
try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)

astr = "42"
try:
    istr = int(astr)
except:
    istr = -1

print("Second", istr)

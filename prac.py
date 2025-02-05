a = range(10)
print(list(a[0:10:2]))

s = "abcd"
a= "abcd"
print(id(a))
print(id(s))
if id(s) == id(a):
    print('same')
else:
    print('NA')
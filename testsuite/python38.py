#: Okay
def f(a, /, b):
    pass
#: Okay
if x := 1:
    print(x)
if m and (token := m.group(1)):
    pass
stuff = [[y := f(x), x / y] for x in range(5)]
#: E225:1:5
if x:= 1:
    pass
#: E225:1:18
if False or (x :=1):
    pass

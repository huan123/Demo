from collections import namedtuple
TPoint =    namedtuple('TPoint1',['x','y'])
p = TPoint(x = 10, y = 10)

print(p.x)
print(p[0])
print(p.y)
print(p)
print(type(p))
for i in p:
    print(i)
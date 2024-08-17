#check type
var = {"kop", "pune", "mum"}
print(type(var))
print(var)

myset = set(["a", "b", "c"])
print(myset)

print("add element")
myset.add("d")
print(myset)

var1 = {"pratik", "nitin", "shailesh"}
print(var1)
var2 = {"pratik","shri","kunal","prem"}
print(var2)

print("union")
print(var1.union(var2))

print("intersection")
print(var1.intersection(var2))

print("pop")
var1.pop()
print(var1)

x = set([1,2,3,4,5,6,7])
print(x)
y = set([2,5,6])
print(y)

print("chek if superset")
print(y.issuperset(x))

print("check if subset")
print(y.issubset(x))

print("remove 3 from",x)
x.remove(3)
print(x)
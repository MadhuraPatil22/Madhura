list1=[1,2,"DYPCET","kolhapur",12.7]
print(list1)
print(type(list1))

for i in list1:
    print(i)
    
#concatenate
li1=["kolhapur","nashik","mumbai","punba"]
li2=["karvir","nanded","punjab"]
print(li1+li2)

#slicing
print(li1[0])
print(li1[1])
print(li1[2])
print(li1[3])

print(li1[-1])
print(li1[-2])
print(li1[-3])
print(li1[-4])

#append
l=["game",23,69,'weather',0.90]
print(l)
l.append("main")
print(l)

list6=[12,14,16,18,20]
la = list6 * 2
print(la)

#insert
num=["mango","banana","chikku","guava"]
num.insert(3,'MAHARASHTRA')
print(num)


nob=[12,13,14,15,16,17]

nob.insert(4,2)
print(nob)

#sum
print("sum of all elements",sum(nob))


# length
n1=[1,2,22,23,12,11,23,34,90,45,67,78,69]
print(len(n1))

#index
print(n1.index(22))
print(n1.index(23))
print(n1.index(90))
print(n1.index(69))


listp=[23,34,2,45,10,45,78]
print(listp)

#count
print("count of 45 = ",listp.count(45))

#delete
del listp[0]
print(listp)

del listp[2]
print(listp)

#remove
plist=["varun","nukul","ram","ayush","pruhvi","karan","suresh","niraj"]
plist.remove("suresh")
print(plist)


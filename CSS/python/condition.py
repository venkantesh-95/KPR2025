a=20
b=60
c=70
if a>b and a>c:
    print("a is Greater")
elif b>a and b>c:
    print("b is Greater")
else:
    print("c is Greater")
    for i in range(1,6,2):
        print(i)
def add(a,b):
    return(a+b);
print(add(50,60)) 


list=[1,2,3,4,5];
for i in list:
    print(i)

    tuple=(6,7,8,9);
for i in tuple:
    print(i)
print(type(tuple))

dictionary={"name":"venkatesh","password":"123456977"}
print(dictionary["name"])
print(type(dictionary))
for key in dictionary:
    print(dictionary[key])
print("This line will be printed")
x = 1 
if x==1:
    print("x is 1")
myint = 7
print(myint)
myfloat = 7.0 
print(myfloat)
myfloat = int(myint)
print(myint)
mystring = 'hello'
print(mystring)
a,b = 3,4 
print(a,b)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3) 
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist: 
    print(x)

mylist2 = [1,2,3]
print(mylist[2])

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
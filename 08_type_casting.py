#two types of type casting
#implicit  compiler change data type
#explicit  user change data type

#implicit type casting

x=10
y=10.2
z="hello"
print(type(x))
print(type(y))
print(type(z))
x=x+y
print(type(x))   #implicit type casting

#explicit type casting
age=input("how old are you?")
print(type(age))
age=int(age)
print(type(age))
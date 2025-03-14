#hello world
print("hello world")

print("My first program")
price = 100
qty = 5
total = price*qty
print("Total: ", total)

item = "item_one" + \
"item_tw" + \
"item_three"
print(item)

days = ['monday', 'tuesday', 'wendesday',
        'thursday', 'friday']

paragraph = """this is 
a paragraph"""
print(paragraph)

'''
this is a multiline 
comment
'''
month = "may"
age = "18"
print(id(month))

counter = 100
miles = 1000.0
name = "Zara Ali"
print(counter)
print(miles)
print(name)
print(type(counter))
print(type(miles))
print(type(name))

x= str(10)
print("x =", x)

wiek = 20
Wiek = 30
print("wiek:", wiek)
print("Wiek", Wiek)

a=b=c=10
print (a,b,c)
a,b,c = 10,20,30
print(a,b,c)

width = 10
height = 20
area = width*height
perimeter = 2*(width+height)
print ("Area = ", area)
print("Perimeter = ", perimeter)

def sum(x,y):
    sum = x + y
    return sum
print(sum(5,10))

x = 5
y = 10
def sum():
    sum = x + y
    return sum
print(sum())

age = 25
print ("Age:", age)
if age >= 18:
    print ("eligible to vote")
else:
    print ("not eligible to vote")

amount = 2500
print("Amount =", amount)
if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
    discount = amount * 10 / 100
elif amount > 1000:
    discount = amount * 5 / 100

else:
    discount = 0

print("Payable amount = ", amount - discount)

zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
    if char not in 'aeiou':
        print(char, end = '')

numbers = (34,54,67,21,78)
total = 0
for num in numbers:
    total+=num #total=total+num
print ("total =", total)

numbers2 = [34,45,45]
for i in numbers2:
    if i % 2 == 0:
        print(i)

for j in range(5):
    print(j, end ='')
print('\n')
for k in range(10,20):
    print(k, end='')
print('\n')
for n in range (1,10,2):
    print(n, end = ' ')
print('\n')
numbers3 = {10:"Ten", 20:"Twenty", 30:"Thirty"}
for x in numbers3: #x in numbers.items
    #print(x)
    print(x, ":", numbers3[x])

count = 0
while count < 5:
    count+=1
    print ("iteracja nr. {}".format(count))

#var = 1
#while var == 1:
    #num = int(input("wpisz liczbe: "))
    #print ("Wpisales: ", num)

count2 = 0
while count < 5:
    count+=1
    print("iteracja nr: ", count2)

def greetings():
    print("hello")
    return 
greetings()

def testfunction(arg):
    print("id inside the function:", id(arg))

var2 ="hello"
print("id before passing:", id(var2))
testfunction(var2)

def greetings2(name):
    print( "hello {}".format(name))
    return

greetings2("Name")

def pos(x,y, /, z):
    print(x+y+z)

pos(33,22,z=11)

def add(x,y):
    z=x+y
    return z

a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a,b, result))

sum = lambda arg1, arg2: arg1 + arg2
print("wartosci sumy: ", sum(10,20))

var3 = "hello world!"
var4 = "Python Programming"

print("var3[0]: ", var3[0])
print("var4[1:5]: ", var4[1:5])

var5 = "Welcome"
print(type(var5))
print(len(var5))

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1,2,3,4,5,6,7]
print("list1[0]:", list1[0])
print("list2[1:5]:", list2[1:5])
list1[2] = 2001
print(list1)
del list1[2]
print(list1)
list1.append("obj")
print(list1)
list1.copy()
print(list1)
#list1.clear()
list1.remove("obj")
print(list1)
list1.reverse()
print(list1)

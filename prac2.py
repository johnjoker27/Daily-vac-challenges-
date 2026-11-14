#Data structure is a way of organizing and sorting data so it can be accessed and modified efficiently

#Algorithms are finite,step by step instructions to solve a prooblem

def find_largest(a, b, c):
    largest  = a 

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    return largest

print(find_largest(10, 20, 30))

a = int(input("Enter a number:"))
b = int(input("Enter another number: "))

sum = a + b
print("Sum: ",sum)
Difference = a +b
print("Difference: ",Difference)
Product = a * b
print("Product: ", Product)
Quotient = a / b 
print("Qoutient: ", Quotient)

number = 5

for i in range(1,11):
    print(number, "x", i, "=",number * i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


for i in range(1,6):
    print( i, check_number(i))


a = int(input("Enter a number : "))

if a > 0:
     print( "Positive" )
elif a == 0:
     print( "Zero" )
else:
    print( "Negative" )


for i in range(1, 21):
    print(i)

def square(num):
    a = int(input("Enter a number"))
    return a*a

num = [10, 20, 30, 40 ,50]
print(num[0])
print(num[-1])
num.append(60)
num.pop(2)
print(num)

numbers = [12, 45, 7, 89, 23]
large = numbers[0]

for i in numbers:
    if i > large:
        large = i
print(large)

human = {
    "name" : "Named",
    "age" : 18,
    "course" : "Comp eng"
}

print(human["name"])
human["age"] = 20
human["grade"] = "A"

print(human)

for i in numbers:
    for j in numbers:
        print(i, j)

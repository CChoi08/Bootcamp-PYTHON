#data types

#primitive = boolean, numbers, strings

#variable declaration
#integer int
num1 = 42
#float decimal
num2 = 2.3
#boolean true/false
boolean = True
#string 
string = 'Hello World'



#composite data types

#lists
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

#dictionaries
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

#tuples immutable content
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
#expected output: string | tuples?

print(pizza_toppings[1])
#expected output: Sausage

pizza_toppings.append('Mushrooms')
#expected output: ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives', 'Mushrooms']

print(person['name'])
#expected output: John

person['name'] = 'George'
#expected output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

person['eye_color'] = 'blue'
#expected output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': blue}

print(fruit[2])
#epected output: banana



#conditionals

#if
if num1 > 45:
    print("It's greater")
#else
else:
    print("It's lower")

#if
if len(string) < 5:
    print("It's a short word!")
#else if
elif len(string) > 15:
    print("It's a long word!")
#else
else:
    print("Just right!")

#for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1




#pop method

# pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

pizza_toppings.pop()
#expected output: ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese']

pizza_toppings.pop(1)
#expected output: ['Pepperoni','Jalepenos', ' Cheese']

#person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': blue}
print(person)
#expected output: George, Salt Lake, 37, False

person.pop('eye_color')
#expected output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

print(person)
#expected output: George, Salt Lake, 37, False



# pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#expected output: After 1st if statement, After 1st if statement, After 1st if statement



def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
#expected output: Hello, Hello, Hello, Hello, Hello, Hello, Hello, Hello, Hello, Hello


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#expected output:  Hello, Hello, Hello, Hello


def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
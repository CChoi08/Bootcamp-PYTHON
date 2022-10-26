# #1 basic print all integers from 0 to 150
for i in range(0,151):
    print(i)

# #2 multiples of 5 
for i in range(5,1005,5):
    print(i)

#3 Counting, the Dojo Way
#print integers 1 to 100. IF divisible by 5 print "Coding" IF divisible by 10 print "Dojo"
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0 :
        print("Coding")
    else:
        print(i)

#4 Whoa. That Sucker's Huge - add odd integers from 0 to 500,000. print final sum
sum = 0
for i in range(1, 500001):
    if i % 2 == 1:
        sum += i
print(sum)

#5 Countdown by Fours - print positive numbers starting at 2018 decremating by 4
count = 2018
while count > 0:
    print(count)
    count -= 4

#6 Flexible Counter
lowNum = 1
highNum = 8
mult = 3

for i in range(1, highNum + 1):
    if i % 3 == 0:
        print(i)
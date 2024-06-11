# IF 
a = 10
b = 10
if a == b:
    print('yes')
else:
    print('no')

a = 10
b = 20
c = 30
if (a + b) / c == 1 and c - b - a == 0:
    print('yes')
else:
    print('no')


a = 10
b = 11
c = 10
if a == b:
    print('first condition is true')
elif a == c:
    print('second condition is true')
else:
    print('nothing is true. existence is pain.')    


my_number = 918652728452151
if my_number % 17 == 0 and len(str(my_number)) > 12:
    print("super17")
elif my_number % 13 == 0 and len(str(my_number)) > 10:
    print("awesome13")
else:
    print("meh, this is just a random number")



# LOOPS

dog = ['Freddie', 9, True, 1.1, 2001, ['bone', 'little ball']]

for i in dog:
    print(i)


numbers = [1, 5, 12, 91, 102]

for i in numbers:
    print(i * i)

my_list = "Hello World!"

for i in my_list:
    print(i)

my_s_list = range(0,5)
for i in my_s_list:
    print(i)    


my_string = "python"
x = 0

for i in my_string:
    x = x + 1
    print(my_string[0:x])


for i in my_string:
    x = x - 1
    print(my_string[0:x])
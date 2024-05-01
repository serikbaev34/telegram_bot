name = "Alihan" 
print(name) 
age = input("Сколько тебе лет") 
#number, string, logical, object 
age = int(age) 

if age > 18 and age < 45: 
    print("Вы совершенолетний ", name) 
elif age < 18: 
    print("Вы ребенок") 
else: 
    print("Вы пенсионер")


print("Я посчитаю до 10") 
#[0,  2,  4,  6,  8, ] = range(5) 
# напечатай только чётные числа 
for i in range(5): 
    print(i) 

#while
while age < 18:
    print("Доступ запрещен") 
    age += 1


from random import randint 


def max_number(a, b): 
    # верни большее число 
    return 0 

from turtle import * 
t = Turtle()
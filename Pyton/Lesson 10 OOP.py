# Задача 1
# Создай пустой класс Робот.
# Создай два объекта этого класса: робот_1 и робот_2.
# Выведи на экран тип переменных робот_1 и робот_2.

class Robot:
    pass
robot_1= Robot()
robot_2 = Robot()
print(type(robot_1))
print(type(robot_2))


# Задача 2
# Добавь в класс Робот общий атрибут вид = "Андроид".
# Выведи этот атрибут: через обращение к классу через объект робот_1

class Robot:
    vid = "Андроид"
print(robot_1.vid)
print(Robot.vid)


# Задача 3
# Создай класс Студент.
# Добавь конструктор (__init__) , который принимает параметры имя и курс и сохраняет их как атрибуты объекта.
# Создай один объект класса Студент с любым именем и номером курса.
# Выведи имя и курс этого студента.
# Выполни её.

class Student:
    def __init__(self, name, curse):
        self.name = name
        self.curse = curse

student = Student("Алексей", 2)
print(student.name)
print(student.curse)


# Задача 4
# Создай класс Книга.
# Добавь конструктор, который принимает название и автор.
# Добавь метод описание(), который выводит фразу:
# "Книга {название}, автор {автор}"
# Создай объект и вызови этот метод.

class Book:
    def __init__(self,name,autor):
        self.name = name
        self.autor = autor
    def display_info(self):
        print(f"Книга {self.name}, автор {self.autor}")
my_book = Book("Avatar","Oleg")
my_book.display_info()


# Задача 5
# Создай класс Счетчик.
# У него должен быть общий атрибут общее_количество = 0, который считает, сколько всего создано объектов этого класса.
# В конструкторе (__init__) увеличивай этот общий атрибут на 1 при создании каждого нового объекта.
# Создай три объекта Счетчик.
# Выведи значение общее_количество через обращение к классу.

class Count:
    count = 0
    def __init__(self):
        Count.count += 1
count_1 = Count()
count_2 = Count()
count_3 = Count()


# Задача 6
# Создай класс Товар.
# В конструкторе сохраняй название и цена.
# Добавь метод цена_со_скидкой(), который принимает размер скидки в процентах и возвращает цену со скидкой.
# Создай один объект, вызови метод с любой скидкой и выведи результат.

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def discount_price(self,discount):
        return self.price - (self.price * discount / 100)

product_1 = Product(name="Apple",price=10000)
print(product_1.discount_price(discount=50))


# Задача 7
# Создай класс Пользователь.
# В конструкторе сохраняй имя и возраст.
# Добавь метод поздороваться(), который принимает объект другого пользователя и выводит:
# "{имя1} приветствует {имя2}"
# Создай двух пользователей.
# Вызови метод у первого пользователя, передав ему второго.

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def welcome(self,other_user):
        print(f"{self.name}, которому {self.age} лет, приветствует {other_user.name}, которому {other_user.age} лет")

man_1 = User(name="Oleg",age=27)
other_user = User(name="Igor",age=29)
print(man_1.welcome(other_user))


# Задача 8
# Создай класс БанкСчет.
# В конструкторе сохраняй владелец и баланс (по умолчанию 0).
# Добавь методы:
# пополнить(сумма) — увеличивает баланс
# снять(сумма) — уменьшает баланс (если сумма не превышает баланс)
# Создай один объект.
# Пополни счёт на 500, сними 200, выведи итоговый баланс.

class BankCount:
    def __init__(self,user,balance=0):
        self.user = user
        self.balance = balance

    def top_up(self,up):
        self.balance += up
        print(self.balance)
    def down_up(self,down):
        if down < self.balance:
            self.balance -= down
        elif down > self.balance:
            print("Ошибка, на балансе не достаточно средств")
up_1 = BankCount(user="Alex")
up_1.top_up(500)
up_1.down_up(200)


# Задача 9
# Создай класс Смартфон.
# В конструкторе сохраняй модель и цена.
# Добавь общий атрибут количество_продано = 0.
# Добавь метод продать(), который:
# Увеличивает общий счётчик проданных на 1
# Выводит сообщение: "Смартфон {модель} продан"
# Создай два объекта.
# Вызови метод продать() для каждого.
# Выведи общее количество проданных смартфонов.

class Phone:
    count = 0
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def seals(self):
        Phone.count += 1
        print(f"Смартфон {self.model} продан")

bay_1 = Phone(model="Iphone",price=1000)
bay_2 = Phone(model="Samsung",price=2000)
bay_1.seals()
bay_2.seals()
print(Phone.count)


# Задача 10
# Создай класс Собака.
# В конструкторе сохраняй кличка и возраст.
# Добавь метод лай(), который выводит:
# "{кличка} говорит Гав!"
# Создай список из трёх объектов класса Собака с разными кличками и возрастами.
# Пройди по списку циклом и вызови метод лай() для каждой собаки.

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print(f"{self.name} говорит Гав!")

nickname = [
    Dog("Spaik",1),
    Dog("Rodster",5),
    Dog("Polka",3)]
for n in nickname:
    n.say()
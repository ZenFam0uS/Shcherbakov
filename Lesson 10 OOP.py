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
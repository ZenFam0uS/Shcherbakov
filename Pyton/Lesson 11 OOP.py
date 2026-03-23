# Задача №1 сам

# Создай родительский класс Device (Устройство).
# У него должен быть метод turn_on, который при вызове печатает на экран строку: "Устройство включено".
# Затем создай дочерний класс Smartphone (Смартфон), который наследует этот метод от Device.
# Создай экземпляр класса Smartphone и вызови у него метод turn_on.

class Device:

    def turn_on(self):
        print("Устройство включено")

class Smartphone(Device):
    pass

my_phone = Smartphone()
my_phone.turn_on()


# Задача №2 сам

# Создай родительский класс Animal (Животное).
# В методе __init__ он должен принимать имя животного и сохранять его в атрибут self.name.
# У него должен быть метод speak, который печатает фразу: "Животное издает звук".
# Теперь создай дочерний класс Cat (Кошка).
# Он должен переопределить метод speak родителя.
# В новом методе speak класса Cat должна печататься фраза: "Мяу!".
# Создай экземпляр класса Cat с именем "Барсик" и вызови у него метод speak.

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Животное издает звук")
class Cat(Animal):
    def speak(self):
        print("Мяу")
my_cat = Cat("Барсик")
my_cat.speak()


# Задача №3 помог дипсик

# Создай родительский класс Transport (Транспорт).
# В __init__ он принимает параметр brand (марка) и сохраняет его в атрибут.
# Создай дочерний класс Car (Машина).
# В __init__ класса Car должны приниматься два параметра: brand и model (модель).
# Тебе нужно сохранить оба этих атрибута.
# Важное условие: сохранение атрибута brand должно происходить путем вызова метода __init__ родительского класса (используй super()).
# Создай экземпляр класса Car с маркой "Toyota" и моделью "Camry". Выведи на экран оба атрибута (brand и model) этого экземпляра.

class Transport:
    def __init__(self, brand):
        self.brand = brand

class Car(Transport):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

my_car = Car("Toyota", "Camry")

print(my_car.brand)
print(my_car.model)


# Задача №4 сам

# Создай два родительских класса:
# Класс Flyer (Летающий):
# Содержит метод move, который печатает: "Я лечу".
# Класс Swimmer (Плавающий):
# Содержит метод move, который печатает: "Я плыву".
# Теперь создай дочерний класс Duck (Утка), который наследует от обоих классов (Flyer и Swimmer).
# Создай экземпляр класса Duck и вызови у него метод move.
# Вопрос: Что ты увидишь на экране и почему?

class Flyer():
    def move(self):
        print("Я лечу")
class Swimmer():
    def move(self):
        print("Я плыву")
class Duck(Flyer, Swimmer):
    pass
duck_1 = Duck()
duck_1.move()


# Задача №5

# Создай класс Employee (Сотрудник).
# В __init__ принимает два параметра: name (имя) и salary (зарплата) и сохраняет их.
# Содержит метод get_info, который возвращает строку вида: "Сотрудник: имя, зарплата: значение".
# Создай класс Manager (Менеджер), который наследует от Employee.
# В __init__ принимает три параметра: name, salary и department (отдел).
# Нужно вызвать конструктор родителя для сохранения name и salary, а department сохранить самостоятельно.
# Переопредели метод get_info так, чтобы он возвращал строку: "Менеджер: имя, зарплата: значение, отдел: название".
# Важно: используй super().get_info() для получения базовой строки от родителя, а затем дополни её.
# Создай экземпляр класса Manager с именем "Анна", зарплатой 120000 и отделом "Продажи". Выведи результат вызова метода get_info на экран.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_info(self):
        print(f"Сотрудник:{self.name}, зарплата:{self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary) # тут подсказал дипсик
        self.department = department # тут подсказал дипсик
    def get_info(self):
        print(f"Менеджер:{self.name}, зарплата:{self.salary}, отдел:{self.department}")
user = Manager(name = "Анна",salary = 12000, department = "Продажи")
user.get_info()


# Задача №6

# Создай класс Vehicle (Транспортное средство).
# В __init__ сохрани атрибут speed (скорость).
# Создай метод move, который печатает: "Транспорт движется".
# Создай класс Bicycle (Велосипед), который наследует от Vehicle.
# Переопредели метод move так, чтобы он печатал: "Велосипед едет по дорожке".
# Дополнительно: внутри нового метода move также вызови метод move родительского класса (чтобы сначала выполнилось действие родителя, а потом — свое).
# Создай экземпляр Bicycle со скоростью 20 и вызови его метод move.

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print("Транспорт движется")

class Bicycle(Vehicle):
    def move(self):
        Vehicle.move(self)
        print("Велосипед едет по дорожке")

my_bike = Bicycle(speed=20)
my_bike.move()



"""
Примеры принципов SOLID в Python
"""

import math
from abc import ABC, abstractmethod

# ===========================
# S — Single Responsibility Principle (Принцип единственной ответственности)
# ===========================


class Report:
    """Класс только для хранения данных и генерации отчёта"""

    def __init__(self, data):
        self.data = data

    def generate(self):
        return f'Report: {self.data}'


class ReportPrinter:
    """Класс только для печати отчёта"""

    @staticmethod
    def print(report):
        print(report.generate())


report = Report('Sales Q4')
ReportPrinter.print(report)

# ===========================
# O — Open/Closed Principle (Принцип открытости/закрытости)
# ===========================


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Мы не изменяем базовый класс, а добавляем новые фигуры через наследование и полиморфизм


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(f'Area: {shape.area()}')

# ===========================
# L — Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
# ===========================


class Bird(ABC):
    pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class Duck(FlyingBird):
    def fly(self):
        print('Duck flying')


# class Ostrich(Bird):
#     def fly(self):
#         raise NotImplementedError("Ostrich can't fly")  # Нарушение LSP


class Ostrich(Bird):
    """Не летает - не нарушает LSP, так как не наследуется от FlyingBird"""

    def run(self):
        print('Ostrich running')


birds = [Duck(), Ostrich()]
for bird in birds:
    if isinstance(bird, FlyingBird):
        bird.fly()
    else:
        bird.run()

# ===========================
# I — Interface Segregation Principle (Принцип разделения интерфейсов)
# ===========================


class Printer(ABC):
    @abstractmethod
    def print(self, doc):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class MultiFunctionDevice(Printer, Scanner):
    def print(self, doc):
        print(f'Printing {doc}')

    def scan(self):
        print('Scanning document')


# Так клиенты реализуют только то, что им нужно
device = MultiFunctionDevice()
device.print('MyDoc')
device.scan()

# ===========================
# D — Dependency Inversion Principle (Принцип инверсии зависимостей)
# ===========================


class PaymentGateway(ABC):
    """Абстракция для платёжных систем"""

    @abstractmethod
    def pay(self, amount):
        pass


# Низкоуровжевая реализация 1
class StripeGateway(PaymentGateway):
    def pay(self, amount):
        print(f'Paying {amount} via Stripe')


# Низкоуровжевая реализация 2
class PayPalGateway(PaymentGateway):
    def pay(self, amount):
        print(f'Paying {amount} via PayPal')


# class PaymentProcessor:
#     def __init__(self):
#         self.gateway = StripeGateway()  # жёсткая зависимость - нарушение DIP
#     def pay(self, amount):
#         self.gateway.pay(amount)


class PaymentProcessor:
    """Высокоуровневый модуль зависит только от абстракции PaymentGateway"""

    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.pay(amount)


# Теперь можно легко менять реализацию
processor1 = PaymentProcessor(StripeGateway())
processor1.pay(100)

processor2 = PaymentProcessor(PayPalGateway())
processor2.pay(200)

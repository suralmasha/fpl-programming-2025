class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Person: {self.name}'


if __name__ == '__main__':
    p = Person('Alice')

    print(p)  # Person: Alice

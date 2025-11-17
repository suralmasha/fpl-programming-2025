from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

if __name__ == '__main__':
    my_color = Color.RED
    print(my_color)        # Color.RED
    print(my_color.name)   # 'RED'
    print(my_color.value)  # 1

    # Сравнение
    if my_color == Color.RED:
        print("Это красный!")



import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Число Фибоначчи")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    choice = input("пиши номер: ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("первое число: "))
        num2 = float(input("второе число: "))
        if choice == '1':
            print(num1 + num2)
        elif choice == '2':
            print(num1 - num2)
        elif choice == '3':
            print(num1 * num2)
        elif choice == '4':
            if num2 == 0:
                print("Error")
            else:
                print(num1 / num2)
        elif choice == '5':
            print(num1 ** num2)

    elif choice in ['6', '7', '8', '9', '10']:
        num = int(input("Введите число: "))
        if choice == '6':
            print(f"факториал{num}: {factorial(num)}")
        elif choice == '7':
            print(f"фибоначчи {num}-го элемента: {fibonacci(num)}")
        elif choice == '8':
            print(f"синус {num}: {math.sin(num)}")
        elif choice == '9':
            print(f"косинус {num}: {math.cos(num)}")
        elif choice == '10':
            print(f"тангенс {num}: {math.tan(num)}")

    else:
        print("ERROR")
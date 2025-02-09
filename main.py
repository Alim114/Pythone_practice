def calculator() :
    operation = input("Выберите операцию (+,-,*,/) : ")
    try :
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError :
        print("Введено не число")
    else :
        if operation == '+' :
            result = num1 + num2
        elif operation == '-' :
            result = num1 - num2
        elif operation == '*' :
            result = num1 * num2
        elif operation == '/' :
            if num2 == 0 :
                result = "Ошибка:Деление на ноль"
            else :
                result = num1 / num2
        else :
            result = "Неверная операция"

        print(f"Результат: {result}")


if __name__ == "__main__" :
    calculator()

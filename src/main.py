import sys

def check_int_numbers(number1: float, number2: float) -> bool:  # Проверяем целые ли числа
    return number1.is_integer() and number2.is_integer()


def process_tokens(tokens: list) -> float:
    stack = []
    operators = {
        "+": lambda n1, n2: n1 + n2,
        "-": lambda n1, n2: n1 - n2,
        "*": lambda n1, n2: n1 * n2,
        "/": lambda n1, n2: n1 // n2,
        "//": lambda n1, n2: n1 // n2,
        "%": lambda n1, n2: n1 % n2,
        "**": lambda n1, n2: n1 ** n2,
    }

    for token in tokens:  # Обрабатываем каждый токен
        if token in operators:  # Если это оператор
            try:
                if len(stack) < 2:
                    print("Ошибка: Не хватает чисел для операции")
                    return None
                number2 = stack.pop()
                number1 = stack.pop()
                if token in ['//', '%']:  # Операции только для целых чисел
                    if check_int_numbers(number1, number2):
                        result = operators[token](number1, number2)
                        stack.append(result)
                    else:
                        print("Ошибка: Операции '//' и '%' работают только с целыми числами")
                        return None
                else:
                    result = operators[token](number1, number2)
                    stack.append(result)
            except ZeroDivisionError:
                print("Ошибка: Нельзя делить на ноль")
                return None
        else:  # Если это число
            try:
                num = float(token)
                stack.append(num)
            except ValueError:
                print(f"Ошибка: Неправильный токен - '{token}'")
                return None

    if len(stack) != 1:
        print("Ошибка: Выражение содержит лишние числа")
        return None
    return stack[0]


def calculator_expression(expr: str) -> float:  # Работаем с токенами
    tokens = expr.replace('(', '').replace(')', '')  # Игнорируем скобки
    tokens = tokens.split(' ')  # Делим выражение на токены
    result = process_tokens(tokens)

    if result is None:
        return 'Обнаружена ошибка'
    return result

def run():
    for line in sys.stdin:
        if line.strip():  # Проверяем, что строка не пустая
            result = calculator_expression(line.rstrip())
            print(result)

if __name__ == "__main__":
    run()

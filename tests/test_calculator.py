from src.main import calculator_expression

# Тесты легких выражений
def test_common_expressions(self):
    assert calculator_expression("10 5 +") == 15.0
    assert calculator_expression("10 3 -") == 7.0
    assert calculator_expression("5 6 *") == 30.0
    assert calculator_expression("5 2 /") == 2.5
    assert calculator_expression("2 3 **") == 8.0
    assert calculator_expression("10 3 //") == 3.0
    assert calculator_expression("7 2 %") == 1.0


# Тесты сложных выражений
def test_complex_expressions(self):
    assert calculator_expression("3 4 + 2 *") == 14.0  # (3+4)*2
    assert calculator_expression("5 1 2 + 4 * + 3 -") == 14.0  # 5+((1+2)*4)-3
    assert calculator_expression("10 2 / 3 + 4 *") == 32.0  # ((10/2)+3)*4
    assert calculator_expression("-5 3 +") == -2.0
    assert calculator_expression("5 -3 +") == 2.0
    assert calculator_expression("-2 -3 *") == 6.0



# Тесты ошибок
def test_error_expressions(self):
    assert calculator_expression("5 0 /") == "Обнаружена ошибка"
    assert calculator_expression("5.5 2 //") == "Обнаружена ошибка"
    assert calculator_expression("5 2.5 //") == "Обнаружена ошибка"
    assert calculator_expression("5.5 2 %") == "Обнаружена ошибка"
    assert calculator_expression("5 2.5 %") == "Обнаружена ошибка"


def test_insufficient_operands(self):
    assert calculator_expression("5 +") == "Обнаружена ошибка"
    assert calculator_expression("+") == "Обнаружена ошибка"
    assert calculator_expression("5 3 4 +") == "Обнаружена ошибка"


def test_extra_operands(self):
    assert calculator_expression("5 3 4") == "Обнаружена ошибка"
    assert calculator_expression("2 3 4 +") == "Обнаружена ошибка"


def test_invalid_tokens(self):
    assert calculator_expression("5 abc +") == "Обнаружена ошибка"
    assert calculator_expression("hello world") == "Обнаружена ошибка"


def test_empty_expression(self):
    assert calculator_expression("") == "Обнаружена ошибка"
    assert calculator_expression("   ") == "Обнаружена ошибка"


# Тесты со скобками (должны игнорироваться)
def test_with_parentheses(self):
    assert calculator_expression("( 3 4 + )") == 7.0
    assert calculator_expression("3 ( 4 + )") == 7.0
    assert calculator_expression("( 3 ) ( 4 ) +") == 7.0

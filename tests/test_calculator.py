from src.main import calculator_expression


# Тесты легких выражений
def test_common_expressions():
    assert calculator_expression("10 5 +") == 15.0
    assert calculator_expression("10 3 -") == 7.0
    assert calculator_expression("5 6 *") == 30.0
    assert calculator_expression("5 2 /") == 2.5
    assert calculator_expression("2 3 **") == 8.0
    assert calculator_expression("10 3 //") == 3.0
    assert calculator_expression("7 2 %") == 1.0


# Тесты сложных выражений
def test_complex_expressions():
    assert calculator_expression("(3 4) + 2 *") == 14.0
    assert calculator_expression("5 1 2 + 4 * + 3 -") == 14.0
    assert calculator_expression("( 6.25 8 ** 10 + 9 - (6 *)") == 13969844.619232178
    assert calculator_expression("-5 3 +") == -2.0
    assert calculator_expression("-2 -3 *") == 6.0
    assert calculator_expression("( 3 ) ( 4 ) +") == 7.0


# Тесты ошибок
def test_error_expressions():
    assert calculator_expression("5 0 /") == "Обнаружена ошибка"
    assert calculator_expression("5.5 2 //") == "Обнаружена ошибка"
    assert calculator_expression("5.5 2 %") == "Обнаружена ошибка"
    assert calculator_expression("5 +") == "Обнаружена ошибка"
    assert calculator_expression("+") == "Обнаружена ошибка"
    assert calculator_expression("5 3 4 +") == "Обнаружена ошибка"
    assert calculator_expression("5 3 4") == "Обнаружена ошибка"
    assert calculator_expression("") == "Обнаружена ошибка"
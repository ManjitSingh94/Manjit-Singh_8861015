# import addition
# import multiplication
import calculator
def test_integration1():
    # Test multiplying the result of adding two numbers with another number
    assert calculator.multiply(calculator.add(2, 3), 4) == 20

def test_integration2():
    # Test subtracting the result of multiplying two numbers with another number
    assert calculator.subtract(calculator.multiply(2, 3), 4) == 2

def test_integration3():
    # Test dividing the result of subtracting two numbers with another number
    assert calculator.divide(calculator.subtract(10, 2), 2) == 4


## Unit testing

# def test_addition():
#     assert calculator.add(2, 3) == 5
#
# def test_subtraction():
#     assert calculator.subtract(5, 3) == 2
#
# def test_multiplication():
#     assert calculator.multiply(2, 3) == 6
#
# def test_division():
#     assert calculator.divide(6, 3) == 2
#
# def test_divide_by_zero():
#     try:
#         calculator.divide(6, 0)
#     except ValueError as e:
#         assert str(e) == "Cannot divide by zero"
#     else:
#         assert False, "Expected ValueError"
#
#
#
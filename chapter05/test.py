op = 'y *'
num1 = 1
num2 = 2

match op:
    case '+':
        return num1 + num2
    case '-':
        return num1 - num2
    case '*':
        return num1 * num2
    case '%':
        return num1 % num2
    case '/':
        return num1 / num2
    case '**':
        return num1 ** num2
    case _:
        return 'Please choose one mathematical operation: + - * % / **'

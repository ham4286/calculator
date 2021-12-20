while True:
    first = int(input("첫번째 숫자 : "))
    second = int(input("두번째 숫자 : "))
    Operator = input("연산자 : ")
    if Operator == '+':
        print(first + second)
    elif Operator == '-':
        print(first - second)
    elif Operator == '/':
        print(first / second)
    elif Operator == '*':
        print(first * second)
    answer = input("계속 하시겠습니까?(O/X)")
    if answer == 'X':
        break
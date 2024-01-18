
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
 
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    return num1 / num2
 
print("Выберите нужную вам математику -\n" \
        "1. Прибавить\n" \
        "2. Убавить\n" \
        "3. Умножить\n" \
        "4. Разделить\n")
 
 
select = int(input("Введите 1, 2, 3, 4 для выбора :"))

number_1 = int(input("Введите первую цифру: "))
number_2 = int(input("Введите вторую цифру: "))
 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
    
                    multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
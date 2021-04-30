# 21. Индекс массы тела
_bmi = 0


def bmi(weight: float, height: float):
    _bmi = weight / (height ** 2)


def print_bmi(bmi: float):
    if _bmi < 18.5:
        print('Underweight')
    elif 18.5 <= _bmi < 25.0:
        print('Normal')
    elif 25 <= _bmi < 30.0:
        print('Overweight')
    else:
        print('Obesity')



bmi(85, 185)
print_bmi(bmi)

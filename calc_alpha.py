'''
Alpha:
x1+(Alpha^0.5/1000) Mega
x(1+Alpha^0.5/1000)^2.25 Prestige
x(1+Alpha^0.5/1000)^5.0625 Ultra
x(1+Alpha^0.5/1000)^10.125 Rebirth
x(1+Alpha^0.5/1000)^20.25 Multiplier
x(1+Alpha^0.5/1000)^40.5 Cash
'''
from time import sleep


# Создание класса Alpha
class alpha:
    def __init__(self):
        self.mega = round(1 + (x ** 0.5 / 1000))
        self.prestige = round((1 + x ** 0.5 / 1000) ** 2.25, 2)
        self.ultra = round((1 + x ** 0.5 / 1000) ** 5.0625, 2)
        self.rebirth = round((1 + x ** 0.5 / 1000) ** 10.125, 2)
        self.multi = round((1 + x ** 0.5 / 1000) ** 20.25, 2)
        self.cash = round((1 + x ** 0.5 / 1000) ** 40.5, 2)


# Создание класса Text
class text:
    def __init__(self):
        self.x2 = "Множитель"
        self.mega = f"{self.x2} Mega: "
        self.prestige = f"{self.x2} Prestige: "
        self.ultra = f"{self.x2} Ultra: "
        self.rebirth = f"{self.x2} Rebirth: "
        self.multi = f"{self.x2} Multi: "
        self.cash = f"{self.x2} Cash: "


# Создание функции для вывода множителей
def all_stat():
    print(txt.mega + str(alph.mega))
    print(txt.prestige + str(alph.prestige))
    print(txt.ultra + str(alph.ultra))
    print(txt.rebirth + str(alph.rebirth))
    print(txt.multi + str(alph.multi))
    print(txt.cash + str(alph.cash))


# Вопрос, сколько у игрока Alpha
x = int(input("Сколько у тебя Alpha?: "))
# Вопрос, нужно ли записывать все в txt-файл
# txt_file = input("Записать в текстовый документ?: ")

# Проверка для переменной txt_file (то есть нужно ли записывать в txt-файл)
'''
if txt_file == "Да":
    pass
elif txt_file == "Нет":
    pass
else:
    exit(print("Неверный ответ: Либо Да, Либо Нет"))
'''

# Пустышки для запуска функций
alph = alpha()
txt = text()

# Запуск скрипта
if __name__ == '__main__':
    all_stat()
    sleep(5)

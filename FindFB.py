try:
    with open('123.xml', encoding='utf-8') as file:
        s = file.readlines()
except FileNotFoundError:
    print("***ОШИБКА***")
    print("Вы забыли скопировать файл баланса в папку с программой. Поместите файл баланса в папку с программой, переименуйте его в '123.xml', и запустите программу повторно!!!")
    print("***ОШИБКА***")
print("""Инструкция!!!
1. Скопируйте нужный вам файл баланса в папку с программой.
2. Переименуйте файл баланса в 123.xml (расширение менять не нужно, обычно оно уже xml).
3. Подготовьте список алкокодов для которых нужно найти справки FB. Алкокоды должны быть разделены пробелами, то есть должны быть написаны через пробел.
4. После запуска нужно вставить скопированный ранее список алкокодов в строке ввода. (Напоминание: список алкокодов должен быть разделен пробелами, то есть алкокоды должны быть написаны через пробел!)
5. Потом нажмите Enter. Выведется список справок FB соответствующих списку алкокодов. Поиск ведется из файла баланса, который вы поместили в папку с программой. 
6. Теперь можно скопировать ФБ-шки выделив и нажав CTRL+C.
""")
j = 0
i = 0
z = list(map(str, input("Введите алкокоды через пробел: ").split()))
iALC = 0
iFB = 0
countALC = 0
sdvig = 0

bal = "".join(s)


for j in range(len(z)):
    countALC = bal.count(z[j])
    for i in range(countALC):
        iALC = bal.find(z[j], sdvig, -1)
        iFB = bal.rfind("FB-", 0, iALC)
        print(bal[iFB:iFB + 18])
        sdvig = iALC + 25
    sdvig = 0

input()





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
3. Подготовьте список алкокодов для которых нужно посчитать количество из баланса. Алкокоды должны быть разделены пробелами, то есть должны быть написаны через пробел.
4. После запуска нужно вставить скопированный ранее список алкокодов в строке ввода. (Напоминание: список алкокодов должен быть разделен пробелами, то есть алкокоды должны быть написаны через пробел!)
5. Потом нажмите Enter. Выведется список продукции и остаток из файла баланса. Поиск ведется из файла баланса, который вы поместили в папку с программой.
""")
j = 0
i = 0
z = list(map(str, input("Введите алкокоды через пробел: ").split()))
iALC = 0
iQ = 0
countALC = 0
sdvig = 0
sumQ = 0
inameB = 0
inameE = 0
name = ""
for j in range(len(z)):
    countALC = s[0].count(z[j])
    for i in range(countALC):
        iALC = s[0].find(z[j], sdvig, -1)
        iQ = s[0].rfind("Quantity", 0, iALC)
        inameB = s[0].rfind("<pref:FullName>", 0, iALC)
        inameE = s[0].rfind("</pref:FullName>", 0, iALC)
        name = s[0][inameB + 15:inameE]
        sumQ += float(s[0][iQ - 12:iQ - 6])
        sdvig = iALC + 25
    sdvig = 0
    print(f"Сумма по алкокоду {z[j]} {name} = {sumQ}")
    sumQ = 0

input()






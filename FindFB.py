with open('123.xml', encoding='utf-8') as file:
    s = file.readlines()
print("""Инструкция!!!
1. Скопируйте файл баланса в папку с программой.
2. Переименуйте файл баланса в 123.xml (расширение менять не нужно, обычно оно уже xml).
3. Подготовьте список алкокодов для которых нужно найти справки FB. Алкокоды должны быть разделены пробелами, то есть должны быть написаны через пробел.
4. После запуска нужно вставить скопированный ранее список алкокодов в строке ввода. (Напоминание: список алкокодов должен быть разделен пробелами, то есть алкокоды должны быть написаны через пробел!)
5. Потом нажмите Enter. Выведется список справок FB соответствующих списку алкокодов. Поиск ведется из файла баланса, который вы поместили в папку с программой. 
""")
j = 0
i = 0
z = list(map(str, input("Введите алкокоды через пробел: ").split()))
iALC = 0
iFB = 0
countALC = 0
sdvig = 0

for j in range(len(z)):
    countALC = s[0].count(z[j])
    for i in range(countALC):
        iALC = s[0].find(z[j], sdvig, -1)
        iFB = s[0].rfind("FB-", 0, iALC)
        print(s[0][iFB:iFB + 18])
        sdvig = iALC + 25
    sdvig = 0

# 0350643000001280221 0350542000003758973 0350566000001313125 0001826000001525053 0177281000001258510 0177281000001283347 0350566000001258962 0001826000002559345 0001291000004198980






# a = b = c = 0
# print(a ,b, c)
# #это каскадное присваивание
# a, b = 1, 2# множественное присваивание
#Для чего используется функция type? для определения типа переменной или объекта

#Числа и операции над ними
#типы int - целые числа, float - дробюные, complex - комплексные

# print(abs(-5))#вычисление модуля числа
# #функция вызывается всегда с числовым аргументом, без аргумента или со строкой будет ошибка
# a = abs(-3)
# print(a)
# b = min(1, 2, -2, 4, 6, 10)#минимальный элемент 
# print(b)
# с = max(1, 2, -2, 4, 6, 10)#максимальный элемент
# pow(6, 2)# возведение в степень, 6 в квадрате
# pow(27, 1/3)#в качестве аргумента можно записывать арифметическую операцию, так тоже можно
# round(0.6)#округление к ближайшему целому, при этом если наисать 1,5 эти пять десятых округляются либо в большую либо в меньшую сторону
#также эта функция принимает второй аргумент, это до скольки числе после запятой округлять
#print(round(0.6345345345, 2))#округлит до 2 цифр после запятой
#если второй аргумент будет отрицательным, то округление будет до десятков, то есть округление будет до дробной точки
#print(round(1234.6345345345, -1))#округление до целых десятков
#все эти мат функции могут вызываться друг из друга
#print(max(1, 2, abs(-3), -10))#будет сначала выполнена фунция abs потом max потом print, вложенность может быть какая угодно, то есть сколько угодно
#также есть и встроенные функции которые нужно импортировать
#import math
#чтобы посмотреть функции из модуля math нужно написать название модуля и потом точку. Но это сработает только в pycharm скорее всего
# math.ceil(5.2)#округление до наибольшего целого будет 6
# math.ceil(-5.2)# будет -5
# math.floor(5.99)#окргуляет до наименьшего целого, будет 5
# math.floor(-5.1)#будет -6
# print(math.factorial(6))#функция факториал это перемножение числе от 1 до той цифры от которой мы считаем факториал, в нашем случае перемножаем цифры от 1 до 6
# math.trunc(5.5)#просто отбрасывает дробную часть
# int(4.7)#аналог trunc
# math.log2(4)
#print(math.log10(1000))
# print(math.log(2.7))# натуральный логарифм у которого основание это число E равное примено 2,7, резульатт вычисления такого логарифма в нашем случае примерно 1
# #также эта функция может вычислять логарифм по любому основанию
# print(math.log(27, 3))#просто нужно написать второй аргумент для функции, по умолчанию туда ставится число примерно E = 2.7
# math.sqrt(4)#квадартный корень из числа в скобках
# math.sin(3.14/2)#синус
# math.cos(0)#косинус
# math.pi#получение числа пи
# math.e#получение числа е = 2,72 примерно

# d1, d2, d3, d4, d5 = map(int, input().split())

# print(min(map))

#Индексы и срезы строк
#все строки это упорядоченный набор символов
#все символы у строк имеют индекс с номеро от 0 и далее
#можно обращаться к элементу строки по индексу
# a = "Hello world"
# print(a[0])#будет буква H
# #если обратить к несуществующему индексу то будет ошибка
# print(len(a)-1)#вычисление длины строки
# print(a[len(a)-1])#вывод последнего элемента строки
# #если строка нулевая, то есть в ней нет символов, то будет ошибка
# print(a[-1])#более простой вывод последнего элемента строки
# #также можно написать строку и вывести из нее символ
# print("Hello"[2])#выведется l
#во всех случаях выше мы на выходе получали новую строку только с одним символом
#срезы!!!
# b = "Privet mir"
# print(b[0:3])#обратились к срезу, последняя цифра игнорится, то есть выведутся символы синдексами 0 1 2, цифра 3 игнорится, последняя цифра не включается в срез
# #если после двоеточися ничего не написать, то будет выведен срез от той цифры которую мы написали, до конца строки, или наоборот, ничего не напишем до двоеточия, тогда вывдется все символы сначала и до того символа котоырй напишем после двоеточия
# print(b[:4])#от начала до 4
# print(b[3:])#от 3 до конца
# s = b[:]#тут по сути приравнивание будет
# print(id(s), "\n", id(b), sep="")
# #также можно указывать часть строки с помощью среза
# print(b[1, -2])
#срезы с шагом строка[начальный символ:конечный символ:шаг], по умолчанию шаг равен единице, но можно указать другой, это по сути и есть конструкция обращения к срезу
# s = "Hello python"
# print(s[1:8:2])#с до 8 символа с шагом 2, то есть через одни элемент прыгаем
#если шаг написать отрицательным то перебор символов будет с конца, то есть в обратную сторону. С отрицательным индексом началоа всегда будет с последнего символа строка, то есть с первого символа конца строки
#строки это неизменяемый тип данных, то есть если обратиться к отдельному символу то изменить его нельзя
#можно сделать хитрости, но сами строки это неизменяемые типы данных, то есть неизменяемый объект. Например создать отдельную переменную с нужным символом, и прибавать строку без нужного нам символа, тогда будет замена
# a = input()
# print(a[1::2])
# a = input()
# b = input()
# print(a[0::2] + " " + b[1::2])
# a = "hello"
# print(len(a))
# a, b = map(str, input().split())
# print(a[1:len(b):2] == b[1::2])

#Основные методы строк!!!!!!
#если мы создаем переменную и присваиваем ей строкое значение то в памяти компа создается объект с типом данных str
#каждый такой объект связан с методами для строк
#конструкция использования метода: объект.метод(аргументы), объектом может как значение строки, так и переменная которая имеет строкое значение, то есть ссылается на объект со строкой. Также можно вызвать несколько функций через точку, то есть одну, потом точка и далее вторую и они будут действовать поочередно.
#s = "python"
#print(type(s))
#если написать название переменной и потом точку, то потом пайчарм выдаст список методов для строк
#print(s.upper())#на выходе получаем новую строку состоящую из заглавных букв, при этом исходная строка не меняется, так как строки относятся к неимзеняемым типам данных
#чтобы сохранить результат функции нужно его присвоить в какую то переменную
#res = s.upper()#для вызова функции нужно писать круглые скобки
#print(res)
#print(res.lower())#переводит к нижнему регистру
#метод count : String.count(sub,[start],[end]) - возвращает число повторений подстроки sub из строки String, и есть не обязательные параметры start и end, start это цифра индекса с которого начинается поиск, end это цифра индекса которой заканчивается поиск
#то что в квадратных скобках это не обязательные параметры, то есть их указывать не обязательно
# msg = "abrakadabra"
# print(msg.count("ra"))#выведется колво этих подстрок в строке msg
# print(msg.count("ra", 4))#выведется колво этих подстрок в строке msg начиная с индекса 4
# print(msg.count("ra", 4, 10))#выведется колво этих подстрок в строке msg начиная с индекса 4 и до 10 не включая 10
#print(msg.find(sub,[start],[end]))#конструкция msg.find(sub,[start],[end]), где msg это строка в которой мы ищем, find это функция которая возвращает индекс первой найденной подстроки sub из основной строки msg в которой мы ищем
#также обязательно должна найтись вся подстрока, если не найдется то значение будет -1
# print(msg.find("ka"))#выведется индекс подстроки k, другие буквы из поиска не срабатывают
# print(msg.find("ra", 4))
# print(msg.find("ka", 5))#также обязательно должна найтись вся подстрока, если не найдется то значение будет -1, то есть если написали ka то должно найтись слово ka, а не только буква k, хотя индекс вывдется только буквы k
#rfind поиск справа налево, остальное все то же самое что в find
#msg.index(sub,[start],[end] - этот метод работает также как find, но если указанная подстрока не находится, то метод возвращает ошибку, эта ошибка нужна для обработчика исключений, то есть ошибки можно записывать в определенную функцию и программа будет работать по другому
#string.replace(old, new, count=-1) - заменяет подстроку old на подстроку new. 
#count - максимальное колво замен, count=-1 означает без ограничений(это по умолчанию, но можно поставить свое число). Также этот метод можно юзать несколко раз и заменять разные символы, то есть через точку последовательно замены делать
# print(msg.replace("a", "B"))#заменили буквы a на B
#в заменяющий аргумент можно писать любую строку, даже пустую, тогда элементы просто удалится
#String.isdigit() этот метод возвращает истина если строка целиком состоит из букв и ложь в противном случае 
# print(msg.isalpha())#будет тру так как в переменной одни буквы, то есть именно буквенные символы, пробле это не буквенный символ
# print("hello world".isalpha())#будет фолз так как есть пробел
#String.isdigit()  этот метод возвращает истина если строка целиком состоит из цифр и ложь в противном случае, дробные числа это числа с точкой, а точка это не цифра, поэтому будет фолз с дробными, получается тру только для целых чисел
# a = "56.2"
# b = "578"
# print(a.isdigit())# тут будет фолз так как число с точкой
# print(b.isdigit())#тут будет тру так как тут целое число без точки
# #отрицательные число тоже содержат нецифровой символ "-" и из-за него будет фолз с отрицательными, то есть по сути метод возвращает только целые положительные числа в тру
# c = "-4"
# print(c.isdigit())#будет фолз, так 
#метод string.rjust(width, [fillchar = '']) возвращает строку rjust с заданным числом символом width, и при необходимости добавляет символы fillchar слева их указать в кавычках
# a = "asd"
# print(a.rjust(5))#добавит пробелы вначале строки чтобы колво символов соответствовало тому числу что в скобках
# b = "456"
# print(b.rjust(5, "0"))#добавит символы 0 чтобы всего символов было 5 к переменной b. Добавляемый символ нужно указывать всегда только 1, больше 1 нельзя указать так как будет ошибка
# #если указать длину строки меньше чем сама строка, то результат будет та же самая строка
# #метод string.ljust(width, [fillchar = '']) тоже самое что и rjust только добавляет символы справа
# print(b.ljust(5, "0"))
#String.split(sep=None, maxsplit=-1) возвращает список строк которые разбиваются по символу который мы указали в sep, то есть в строке как только находится нужный нам символ то далее будет следующий элемент списка, то нашли пробел и далее второй элемент, потом опять нашли следующий пробел и будет следующий элемент, можно и не по пробелу разбивать по любому другому символу. То есть split делает список из строки
#sep фрагмент разбиения строки
# z = "Иванов Иван Иванович"
# print(z.split(" "))#будет возвращаться выведен список строк разделенных пробелом, так как мы его указали как аргумент функции, то есть метод ищет пробелы и там где пробел там начинается следующий элемент списка
#d = "1   ,  2 , 5 ,  3,  1, 7"
#print(d.replace(" ", "").split(","))#replace возвращает строку, потом разбивается на список с разделителем по запятым, то есть там где запятая будет начинаться элемент списка. Очень удобно можно сортировать чередуя элементы. В питоне можно вызывать методы поочередно через точку, то есть первый метод потом точка, потом второй, и работают они поочередно

#метод join из списка собирает целую строку
#x = d.replace(" ", "").split(",")
#конструкция join : "разделяющая список строка".join(переменная списка или название списка) и получается будет строка с элементами списка разделенная нужными нам элементами. То есть эта функция делает из списка строку с нужным нам разделителем
#print(", ".join(x))#сделали список строкой с разделителем на ", "
#z = "Иванов Иван Иванович"
#print(", ".join(fio.split()))#сделали разделитель на список и потом соединили с в строку обратно но с разделениями на запятые
#String.strip() удаляет все символы пробелов и переносов строк вначале в конце строки. Конструкция "   строка с пробелами    ".strip()
#print("    hello world    ".strip())
#есть еще lstrip удаляет не нужные символы слева и rstrip удаляет не нужные символы справа

# a = input()
# print(a[0].upper() + a[1:].lower())
# a = input()
# print(a.count("-"))

# a = input()
# print(a.replace("---", "-").replace("--", "-"))

# a, b, c = map(str, input().split())
# print(a.rjust(3, "0"),"\n", b.rjust(3, "0"),"\n" , c.rjust(3, "0"), sep="")
# a = input()
# print(len(a.split(sep=" ")))

# a = input()
# print(a.replace(" ", ";"))

#Форматирование строк и F-строки
# age = 18
# name = "Иван"
# print("Меня зовут " + name + " мне " + str(age) + " лет")
# print("Меня зовут {0} мне {1} лет".format(name, age))#в метод format можно передать переменные в виде параметров, в строке в фигурных скобках можно указать индекты по порядку для параметров в скобках
# #также результат можно присвоить в переменную
# msg = ("Меня зовут {0} мне {1} лет и я люблю {0} пайтон".format(name, age))#вставлять индексы можно много раз
# print(msg)
# asd = ("Меня зовут {fio} мне {old} лет и я люблю пайтон".format(fio=name, old=age))#использовали ключи, то есть параметрам дали имена и теперь код стал понятнее, понятно что где используется
# #если указали ключи, то уже нельзя указать название переменных в фигурных скобках, именно ключи
# #F-строки, пишутся так f"текст в кавычках"
# print(f"Меня зовут {name} мне {age} лет и я люблю пайтон")#в фигурных скобках можно писать название переменных и сразу будут вставляться значения переменных, также там можно писать любые конструкции функции циклы и тд
# print(f"Меня зовут {name.upper()} мне {age*2} лет и я люблю пайтон")
# print(f"Меня зовут {len(name)} мне {age*2} лет и я люблю Python")

# name = input()
# lastname = input()
# age = input()
# print("Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!".format(name, lastname, age))

# a, b = map(int, input().split())
# res = [a, b]
# print(f"{min(res)} {max(res)}")

#Вводится адрес (каждое значение с новой строки) в формате: город, улица, номер дома (целое число), номер квартиры (целое число). Сформировать строку по шаблону: "г. <город>, ул. <улица>, д. <номер дома>, кв. <номер квартиры>", используя F-строку. Результат вывести на экран.

# city = input()
# street = input()
# number_h = int(input())
# number_f = int(input())
# print(f"г. {city}, ул. {street}, д. {number_h}, кв. {number_f}")
# d = float(input())
# r = int(input())
# print(f"Вы можете получить {int(r/d)}$ за {r} рублей по курсу {d}")

#Списки и операции над ними!!!!
#списки это наборы данных
# city = ["Москва", "Питер", "Новосиб", "Яровое"]#список значений строк для городов
# marks= [4, 5, 3, 2, 5]#список значений оценок
# #у списка есть индексы, начинаются они с нуля и тд
# print(marks[0])#обратились к элементу списка
# sr = (marks[0] + marks[1] + marks[2]+ marks[3]+ marks[4])/5#посчитали среднюю оценку
#print(sr)
#к несуществующему элементу списка нельзя обращаться будет ошибка
#print(marks[-1])#обратились к последнему элементу списка
#отрицательные индексы перебирают элементы с конца списка
#списки относятся к изменяемым типам данных, в отличии от строк
#marks[0] = 5# заменили значение первого элемента в списке
#print(marks[0])
#списки это изменяемый тип данных, который может меняться при работе программы в отличии от строк, то есть в строке нельзя присвоить элементу строки другое значение а в списке можно
#списки могут содержать разные типы данных, в том числе и другие списки, любые типы данных, значит любые объекты
# ls = [1,2,3,"ВАся", [5,6,7,3]]
# print(ls)
#a = []#создали пустой список
#b = list()#возвращает соответствующий список, если написать без аргументов то возвратит пустой список, то есть как бы берет список и возвращает его поэлементно, например если это строка то посимвольно разобьет строку, если это просто какой-то список то разобьет этот же список по элементно
#b = list([1, False])
#print(b)
#с помощью функции list можно создавать копии списков
#c = list("python")#функция разобьет строку на список символов, то есть эта функция перебирает списки. Эти перебираемые объекты называются итерируемые
#функция перебирает любые списки или уже существующие списки или любые другие перебираемые итерируемые объекты
#print(c)
#функции списков
#len() - длинна списка, max() - нахождение максимального значения, min() нахождение минимального значения, sum() - вычисление суммы, sorted() для сортировки коллекции
#чтобы использовать функции нужно в скобках указать название списка
# print(len(c))
# t = [23.3, 34.2, 12.3, 45.3, 32.4]
# print(sum(t)/len(t))#посчитали с помощью функций для списокв среднее значение элементов, то есть сумму разделили на колво элементов
#функция sorted возвращает новый отсортированный список по возрастанию, его можно или вывести на экран или присвоить это значение в другую переменную
# sort = sorted(t)#присвоили отсортированный список в другую переменную
# print(sort)
#у функции sorted есть аргумент sorted(i, reverse=True), если написать reverse=True то сортировка будет по убыванию
#функции max min sorted работают также и со строками
# print(max("python"))#возвратится символ с максимальным кодовым значением, значения берутся из таблицы кодов
# print(min("python"))##возвратится символ с минимальным кодовым значением, значения берутся из таблицы кодов
# print(sorted("python"))#отсортируется по возрастанию кодовых значений элементов списка
#вобщем эти функции можно использовать с теми типами данных которые можно сравнить на > или <
#функция суммы для строк не сработает
#оперции над списками
#+ соединение двух списков в один, * дублирование списков, in проверка вхождения элемента в список, del удаление элемента списка
# a = [1, 2, 3] + [4, 5]#объединяются 2 списка и будет одни общий список
# print(a)#вывели его на экран
# #складывать можно именно списки, если просто прибавить число то будет ошибка. Значени в складываемых списках могут быть какие угодно
# #оператор * дублирует эелменты списка и формирует новый список с этими дублями
# a = [1, 2, 3, 4, 5] * 2#умножили список на 2
# #or
# a *= 2#это будет тоже самое
# print(a)
# #умножать нужно именно на целые числа, на дробные нельзя
# #умножать можно и отдельные списки и потом складывать с другими и тд
# #оператор in
# print(5 in a)#выведется тру или фолз в зависимости от того есть ли такое значение в нашем списке
# print(55 in a)
# b = [1, 2, 3, 4, 5, [1, 2]]
# print([1, 2] in b)#проверка есть ли такой вложенный список
# #оператор del
# del b[0]#просто удалили элемент из списка, теперь его там нет
# print(b)
#индексы не удаляются а пересчитываются то есть передвигаются и в любом случае нулевой индекс будет он просто будет для другого элдемента после удаления
# cities = input().split()#split разбивает список по пробелам по умолчанию
# print("Москва" in cities)
# print(cities[0])

#print(input().split()[-1])

# marks = list(map(int, input().split()))
# print(round(sum(marks)/len(marks), 1))

# name = input()
# avtor = input()
# ls = int(input())
# pay = float(input())
# book = [input(), input(), int(input()), float(input())]
# del book[2]
# book[1] = "Пушкин"
# book[2] *=2
# print(book)

# p = list(map(int, input().split()))
# print(max(p), min(p), sum(p))

# p = list(map(int, input().split()))
# lst = sorted(p, reverse=True)
# print(*lst)

# c = list(map(str, input().split()))
# cities = ["Москва", "Тверь", "Вологда"]
# lst = cities + c
# print(*lst)
#значок * убирает запятые и квадратные скобки при выводе

# c = list(map(str, input().split()))
# cities = ["Москва", "Тверь", "Вологда"]
# lst = c + cities
# print(*lst)

#Срезы списков. Операторы сравнения списков!!!!!!
#конструкция среза -  список[старт:стоп] , возможно есть еще шаг
# cities = ["Москва", "Тверь", "Вологда", "Казань", "Питер"]
# print(cities[1:3])#выведутся элементы с 1 по 3, и 3 не включительно
# #при использовании среза выходит новый список, и его можно записать в другую переменную списка, то есть сделать новый список и работать с ним далее
# print(cities[:3])#если не писать начальный индекс, то будет начинаться срез с самого начала
# print(cities[1:])#если не писать конец среза до конца списка будет срез
# #если не писать цифры с квадратных скобках, а просто поставить двоеточие, то будет копия списка то есть срез всего списка, но не дубль списка, то есть id объектов будут разные
# lst = cities[:]
# print(id(lst), id(cities))
# ls = list(cities)#это тоже будет копия списка по аналогии со срезом
# #но если сделеать просто равенство, то это не будет копия списка, так как обе пеерменные будут ссылаться на один и тот же объект
# s = cities
# print(id(s), id(cities))
# marks = [4, 2, 3, 5, 3]
# print(marks[2:-1])#также и отрицательные индексы можно юзать
# #конструкция среза с шагом список[старт:стоп:шаг]
# print(marks[1:4:2])#выведутся элементы с 1 по 4 с шагом 2 то есть через 1
# print(marks[1::2])
# print(marks[::2])#сначала до конца с шагом 2 срез
# #если шаг отрицательный, то стартуем всегда с конца и далее идем с тем шагом какая у нас будет цифра
# print(marks[::-2])#шаг 2 но с конца списка, такой будет срез
# #можно заменять срез списка на другие элементы списка, тем самым меняя основной список, то есть с помощью среза можно обратиться к части списка и изменить его
# marks[2:4] = ["Плохо", "Хорошо"]#теперь 2 оценки будут написаны словами, то есть 2 элемента списка мы заменили на другой список
# print(marks)
#также при присваивании нужно иметь ввиду, что длина среза должна соответствовать длине присваиваемого списка, то есть если срез из 2 элементов то и присвоить нужно ему 2 элемента не меньше это только в случае если элементы идут не подряд то есть шаг больше 1 или не указан последняя граница среза
# marks = [4, 2, 3, 5, 3]
# marks += [4]
# marks[::3] = ["Плохо", "Хорошо"]
# print(marks)
# #также можно просто через запятую присвоить значения
# marks[::3] = 45, 55
# print(marks)
#< > == != операторы сравнения списков
# print([1, 2, 3]==[1, 2, 3])
# print([1, 2, 3]>[1, 2, 3])
# print([1, 2, 3]<[1, 2, 3])
# print([1, 2, 3]!=[1, 2, 6])
#будет значения тру или фолз
#проверка происходит поэлементно, то есть первый элемент сравнивается со первым элементом второго списка и как только проверка пройдет то есть будет тру, то дальше она не проходит
#также больше тот список у которого колво элементов больше при всех прочих равных элементов
#числа со строками в списках не могут сравниваться так как будет ошибка
#строки со строками можно сравнить, сравнение идет также по аскикодам
#print([1, 2, "abc"]>[1, 2, "abd"])
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[-6:-11:-1])
#print([1, 2, 3, "4"] > [1, 2, 3, "5"])

#15. Основные методы списков !!!!!
#список это объект и с ним связаны определенные функции
#методы для списков: append(), insert(), remove(), pop(), clear(), copy(), count(), index(), reverse(), sort(). 
# a = [0, 1, -54, 3, 23, 42, -45, 0, 0]
# a.append(100)# добавление элемента в конец списка, при этом можно просто вызвать функцию и элемент добавится. Присваивать переменной а функции append не нужно, если так сделать то будет в списке присвоено значение None
#сама функция append ничего не возвращает, а только добавляет элемент к списку, поэтому если присвоить эту функцию в переменную и будет None
#a = a.append(100) #так нельзя так как будет None
#добавлять можно любые типы данных, но только по одному, больше 1 если написать то будет ошибка
#если несколько раз использовать функцию то будут добавлять элементы в конец каждый раз при испольовании, то есть добавили 1 элемент он добавится, потом еще один он тоже добавится и также в конец списка
#insert() позволяет вставлять в список элемент, при это другие последующие элементы сдвигаются на следующите индексы. Конструкция список.insert(индекс куда вставляем, значение элемента который вставляем)
# print(a)
# a.insert(3, 555)#вставили на третий индекс цифра 555
# print(a)
#список.remove(значение) удаляет элемент по первому найденному значению из списка, то есть находит первое значение из списка которые мы указали и удаляет его
#a.remove(0)#было 2 нуля теперь будет 1 ноль
#print(a)
#также булевые значения True или False имеют числовые знаения 1 и 0, и если через метод remove удаляем True то может удалиться первая найденная цифра 1 вместо True, тоже самое с цифрой 0 и False
#при удалении несуществующего значения списка будет ошибка
#список.pop() удаляет последний элемент списка если писать без аргументов и при этом он возвращает значение удаленного элемента, то есть его(удаленное значение) можно присвоить в другую переменную
# b = a.pop()#удалили последний элемент и присвоили его в переменную b
# print(b)
# print(a)
#в скобках pop() можно написать цифру индекса элемента который мы хотим удалить, и также его можно и присвоить в другую переменную
#список.clear() удаляет все элементы списка, очищает
#список.copy() делает копию списка, при этом копия списка это будет другой объект, который можно записать в другую переменную, то есть функция возвращает копию списка. Срезы [:] и фунцкия list тоже создают копии списков. То что подходит то и используем
# z = a.copy()
# print(id(z))
# print(id(a))
#список.count(значение) позволяет вывести колво значений из списка, то есть в скобках указываем значение и функция выведет колво таких значений из списка
# print(a.count(0))#в списке у нас 2 нуля, выведется цифра 2
# print(a.count("qweqwe"))#будет 0, так как в списке такого нет
# #список.index(значение, стартовый индекс) позволяет получить индекс первого найденного значения из списка. Второй аргумент функции это стартовый индекс с которого будет начинаться поиск значения
# print(a.index(0))#тут будет найден первый ноль
# print(a.index(0,2))#тут будет найден второй ноль из списка
# #если указать несуществующее значение, то будет ошибка. МОжно перед выполнением функции сделать проверку вхождления с помощью оператор in, а если входит тогда использовать index
# #список.reverse() меняет порядок следования элементов на обратный
# a.reverse()
# print(a)
#список.sort() выполняет сортировку списка по возрастанию или более правильно говорить по неубыванию. Равные элементы идут друг за другом. Этот метод sort() ничего не возвращает, то есть присвоить результат нельзя в переменную, он вернет значение None. То есть его нужно просто применять к списку нужному и все. Функция sorted() возвращает отсортированный список но сам список не затрагивает, а функция сорт только меняет сам список но ничего не возвращает, их нужно не путать
# a.sort()#сортировка по возрастанию
# print(a)
# a.sort(reverse=True)#сортировка по убыванию
#сортировку можно выполнять по тем элементам к которым можно применить знаки < >, то есть строки тоже можно сравнить

#Вводится строка из целых чисел через пробел. Если первое число не равно последнему, то нужно добавить значение True, а иначе - значение False. Результирующий список lst вывести на экран командой:

# lst = list(map(int, input().split()))
# lst.append(lst[0]!=lst[-1])
# print(*lst)

# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1, "Ульяновск")
# print(*cities)

# Вводится строка с номером телефона в формате: 

# +7(xxx)xxx-xx-xx

# Необходимо преобразовать ее в список lst (посимвольно, то есть, элементами списка будут являться отдельные символы строки). Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы. Отобразить полученный список на экране командой:

# print("".join(lst))
# Sample Input:

# +7(912)123-45-67
# Sample Output:

# 8(912)1234567

lst1 = list(input())
lst1.pop(0)
lst = lst1.replace("7", "8")
lst.pop(9)
lst.pop(11)
print("".join(lst))



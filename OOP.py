# ООП - объектно-ориентированное программирование
# Раньше все программы писали без ООП это было до 60-х годов прошлого века. И вплоть до 90-х могли писать без ООП. Но потом зародилась коцепция ООП и стало доминирующим направлением. Самым популярным языком программирования был С++.
# Как представить ООП. Например, нам нужно представить котов. Создаем класс Cats. Этот клас это некий шаблон, на основе которого будут формироваться данные о котах. К примеру шаблоне классе Cats есть свойства: порода, имя, возраст. Вообще свойства мы можем сами прописывать, для примера указали эти свойства. И объектами этого класса будут конкретные коты
# Например 3 обътекта котов: 
# первый объект
# порода Бурма
# Имя Васька
# возраст 3
# второй объект
# порода Саванна
# Имя КРасик
# возраст 5
# третий объект
# порода Русская
# Имя Рыжик
# возраст 2
# с этими объеками потом можно работать как с единым целым
# также в классе есть и функции, для работы с этими объектами. То есть например у класса можно определить функцию, которая будет рисовать кота. Тогда у каждого объекта можно будет вызывать функцию для рисования кота. ТО есть эта функция будет взаимодействовать с объектами с его свойствами
# методов класса может быть много, и они будут взаимодейстовать с свойствами объектов для которого вызываются
# и можно написать программу которая будет работать в каждом объекте этого класса, то есть отдельно в каждом объекте
# еще один пример с объектами
# например у нас есть 3 графика, мы делаем класс graphs, в нем есть свойства для объектов. Создаем на основе этого класса объекты - графики, с нужными нам свойствами и методами
# класс долэен восприниматься как единая целостная конструкция. Все данные внутренние должны быть не доступны извне, все манипуляции с его данными должны быть сокрыты в этом классе. Доступ должен быть только к некоторым, разрешенным данным.
# инкапсуляция - это скрытие данных и методов класса, чтобы их нельзя было использовать вне класса, то есть к ним можно ограничить доступ. Либо разрешить доступ к определенным элементам класса и использовать вне класса.
# Наследование - это когда есть класс в которором есть основные элементы для все объектов, а другие классы будут являться наследниками этого класса и они будут перенимать основные свойства для объекта от класса родителя, и в классах наследниках могут быть дополнительные свойства или методы, то есть расширенный функционал
# Полиморфизм - возможность работать через единый интерфейс с объектами разных классов
# Виды: Ad hoc и Параметрический
# Ad hoc реализовывался через перегрузку функций и приведение различных типов данных, применялся до появления ООП. В питоне он не используется
# Параметрический
# то есть когда мы создаем объект от дочернего класса, то обращаемся к базовому классу родителю

# базовый класс Figure, свойства coords, width, color, метол draw()
# наследники
# Line
# Rect
# Ellipse

# Полиморфизм:
# можно все объекты от дочерних классов привести к базовому классу и использовать общий метод который есть в базовом классе для всех объектов, и он будет переопределяться то есть модифицироваться в зависимости от того на основании кокого класса создан объект, то есть базовый метод будет переделываться под класс наслденик, то наследник будет добавлять функционал или изменять его. И если будут добавляться новые наследники, то базовый метод будет переопределяться под новый метод нового наследника. То есть полиморфизм это модификая функций класса с переопределением и добавлением функций

# Классы и объекты. Атрибуты классов и объектов!!!!!!!!!!!!!!!!!
# определение класса, конструкция:
# class <название класса>:
# 	тело класса
# пример:
# class Point:
# 	pass

# в соответствии со стандартом PEP8 название класса пишется с большой буквы и должно отражать суть класса. Также нельзя разделять название класса нижним подчеркииванием.

# class Point:
# 	color = "red"
# 	circle = 2

# переменные внутри класса называют атрибутами класса или его свойствами
# класс образует пространство имен с именем класса, с этом пространстве имен есть переменные. У ним можно обращаться используя синтаксис для пространства имен
# обращаться к элементу можно написав название класса и поставить точку и потом написать название переменной
# Point.color = "Black"#присвоили другое значение элементу и значение изменилось
# print(Point.color)#обратились к элементу и вызвали его
# print(Point.circle)#обратились к другому элементу и тоже его вызвали, то есть прочитали
# чтобы прочитать все атрибуты класса можно написать следующее:
# print(Point.__dict__)#в нем будут все стандартыне элементы и также наши 2 атрибута
# Создание объекта класса. В переменную присваиваем название класса и пишем круглые скобки
# a = Point()
# теперь a является экземпляром класса Point. Через нее теперь доступны переменные атрибуты 
# b = Point()#создали второй экземпляр объекта класса. Это совершенно другой объект, но значения атрибутов те же самые. Можно создавать любое колво экземпляров класса
# можно опредилть какому типу то есть классу принадлежит объект с помощью функции type
# print(type(a))#выведется инфа об объекте класса Point
# print(type(a) == Point)#тут будет тру
# print(isinstance(a, Point))#тут тоже тру
# то имя класса здесь выступает в качестве типа данных
# объекты a и b обруют пространство имен экземпляров класса. Они не содержат никаких собственных атрибутов. Свойства color и circle берутся из класса Point. Внутри объектов этих свойств не существует, и они ссылаются на соответствующие атрибуты класса Point.То есть если атрибуты класса в нашем случае изменить, то этот атрибут изменится во всех объектах. Атрибуты класса общие для всех экземпляров
# print(a.color)
# print(b)#тут будет ссылка на объект
# Point.circle = 3#изменили атрибут, и он изменится для всех объектов
# print(a.__dict__)#вывели все атрибуты объекта, там будет пусто, так как сам по себе не содержит атрибутов
# print(b.__dict__)#тут будет тоже пусто
# то есть в объектах a и b есть пространства имен, но они пустые. Но через объекты можно обращаться к атрибутам класса Point
# print(b.circle)
# А если мы обратимся к объекту a к атрибуту color и присвоить ему значение, то значение изменится только у объекта a
# a.color = "green"
# print(a.color)#тут будет green
# print(b.color)#тут будет все еще black
#в пайчарме есть сбоку панель в питон консоли, там отображаются объекты и атрибуты в папках, сначала атрибуты подсвечиваются красным, это когда они берутся только из класса, а когда такой же атрибут создается у самого объекта в этой папке он становится зеленым
# это a.color = "green" работает так, когда мы обратились через переменную объекта "a", то мы обратились к пространству имен "a", и атрибуту color и когда написали оператор присваивания, то в этот момент в пространстве имен "a" создалась переменная color, то есть свой атрибут или свойство создался и ему присвоилось значение
# а объект b по прежнему ссылается на атрибут класса Point
#в этом можно убедиться если вывести в консоль все атрибуты объекта a
# print(a.__dict__)#тут будет выведен 1 атрибут color со значением green в виде словаря
# на таком принципе в питоне построено формирование атрибутов класов и атрибутов экземпляров объектов
# также можно добавлять и новые атрибуты в класс через простое присваивание
# Point.type_pt = "disk"#в теперь в классе Point появился новый атрибут, и этот атрибут будет распространен на все объекты на основе этого класса
# print(a.type_pt)
# еще можно добавлять атрибут с помощью функции setattr. Если в классе не существует атрибута с таким имененем, то такой атрибут добавляется в него динамически. Если такой атрибут есть, то мы можем с помощью этой функции поменять в нем значение
# Конструкция функции setattr:
# setattr(<название класса>, <название нового аттрибута в кавычках>, <значние атрибута>)
# setattr(Point, "prop", 777)#добавили новый атрибут
# print(Point.prop)
# res = Point.circle#можно обратиться к атрибуту класса и записать его значение в переменную
#если обратиться к несуществующему атрибуту, то питон выдаст ошибку
# но можно использовать функцию getattr
# print(getattr(Point, "asd"))#если обратиться к несуществующему атрибуту, то также питон также выдаст ошибку
# print(getattr(Point, "asd", False))#но можно прописать третий атрибут, и он будет возвращаться если атрибут не обнаруживается
# Конструкция: getattr(<название класса>, <название аттрибута в кавычках>, <значение которое будет возвращаться в случае если аттрибут не найден>) третий параметр не обязательный
# print(getattr(Point, "color", False))#если указать существующий аттрибут, то он возвратится
# удаление аттрибутов!!!
# del Point.prop#теперь аттрибут prop удален
# дважды удалять нельзя, так как питон напишет ошибку если аттрибут уже удален
# но можно использовать функцию hasattr для проверки существования аттрибута в классе
# print(hasattr(Point, "prop"))#если такого аттрибута в классе нет, то возвратится false, если бы этот атрибут был, то мы бы увидели значение тру
# print(hasattr(Point, "circle"))#тут будет тру
# еще можно использовать для удаления аттрибута delattr
# конструкция: delattr(<Название класса>, <название атрибута в кавычках>)
# delattr(Point, "type_pt")#после вызова этой функции аттрибут удалится. Дважды если вызвать, то будет ошибка в питоне. Поэтому прежде чем удалять, нужно проверить существует такой аттрибут в классе или нет. С объектами тоже самое, также можно удалять, но также проверяеть существование аттрибута
# функция hasattr возвращает тру в случае если аттрибут либо есть в классе или объекте, либо доступен через экземпляр объекта в случае если применяем функцию к объекту
# print(hasattr(a, "circle"))#этого атрибута в объекте нет, но этот аттрибут доступен через класс, поэтому здесь вернется тру. ТО есть функция проверяет текущее пространство имен и связанное пространство. 
# del удаляет только если аттрибут есть в объекте или классе. Если нет, то напишет ошибку
# после удаления аттрибута из объекта, значение аттрибута объекта меняется на значение аттрибута класса
# del a.color#теперь color будет опять black
# print(a.color)
#вообще поиск аттрибута происходит так, сначала поиск идет из внутреннего пространства имен, потом из внешнего пространства, то есть в нашем случае из класса на основании которого создан объект
# задача, формирование объектов точек на плоскости
#написали класс
# class Point:
# 	"Класс для представления координат точек на плоскости"#сделали описание класса, оно просто пишется в кавычках без присвоения в какую либо переменную
# 	color = "red"
# 	circle = 2

# # создали объекты
# a = Point()
# b = Point()
# # теперь запишем координаты точек, они должны принадлежать экземплярам объекта
# a.x = 1#значение по оси x
# a.y = 2#значение по оси y
# b.x = 10#тоже самое для объекта b
# b.y = 20
# #тут мы динамически создали аттрибуты для точек координат на плоскости. Эти аттрибуты принадлежат только объектам a и b
# # print(a.y)
# print(Point.__doc__)#вывели описание класса на экран. Описание нужно для того чтобы проще было читать код в случае если большой класс пишем со с одной структурой
# итоги
# getattr(obj, name[, default]) - возвращает значение атрибута объекта
# hasattr(obj, name) - проверяет на наличие атрибута name в obj
# setattr(obj, name, value) - задает значение атрибута(если аттрибута не существует, то он создается)
# delattr(obj, name) - удаляет атрибут с именем name

# __doc__ - содержит строку с описанием класса
# __dict__ - содержит набор атрибутов экземпляра класса

# Задачки!!!!!!!!!!!

# Объявите класс с именем DataBase, который бы хранил в себе следующую информацию:

# pk: 1
# title: "Классы и объекты"
# author: "Сергей Балакирев"
# views: 14356
# comments: 12
# Имена переменных (атрибутов класса) используйте такие же (pk, title, author, views и comments) с соответствующими значениями.

# мое решение
# class DataBase:
# 	pk = 1
# 	title = "Классы и объекты"
# 	author = "Сергей Балакирев"
# 	views = 14356
# 	comments = 12


#  Объявите класс с именем Goods и пропишите в нем следующие атрибуты (переменные):
# title: "Мороженое"
# weight: 154
# tp: "Еда"
# price: 1024
# Затем, после объявления класса, измените его атрибут price на значение 2048 и добавьте еще один атрибут:

# inflation: 100

# class Goods:
# 	title = "Мороженое"
# 	weight = 154
# 	tp = "Еда"
# 	price = 1024

# Goods.price = 2048
# Goods.inflation = 100


# Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:

# model: "Тойота"
# color: "Розовый"
# number: "П111УУ77"
# Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
# мой вариант
# class Car:
# 	pass

# setattr(Car, "model", "Тойота")
# setattr(Car, "color", "Розовый")
# setattr(Car, "number", "П111УУ77")
# print(Car.__dict__["color"])

#через цикл
# class Car:
#     pass

# d = {'model': "Тойота", 'color': "Розовый", 'number': "О111АА77"}

# for n in d:
#    setattr(Car, n, d[n])

# print(Car.__dict__['color'])

# через генератор
# class Car:
#     pass
# d = {
#     'model': "Тойота",
#     'color': "Розовый",
#     'number': "О111АА77"
# }
# [setattr(Car,k,v) for k,v in d.items()]

# print(Car.__dict__['color'])

# Объявите класс с именем Notes: и определите в нем следующие атрибуты:

# uid: 1005435
# title: "Шутка"
# author: "И.С. Бах"
# pages: 2
# Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author.

# class Notes:
# 	uid = 1005435
# 	title = "Шутка"
# 	author = "И.С. Бах"
# 	pages = 2

# print(getattr(Notes, "author"))


# Объявите класс с именем Dictionary и определите в нем следующие атрибуты:

# rus: "Питон"
# eng: "Python"
# Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута rus_word. Если такого атрибута в классе нет, то функция getattr() должна возвращать булево значение False.

# class Dictionary:
#     rus = "Питон"
#     eng = "Python"
#
# print(getattr(Dictionary, "rus_word", False))

# Объявите класс с именем TravelBlog и объявите в нем атрибут:
# total_blogs: 0
# Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:
# name: 'Франция'
# days: 6
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
# Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два локальных свойства:
# name: 'Италия'
# days: 5
# Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.
#
# P.S. На экран ничего выводить не нужно.

# class TravelBlog:
#     total_blogs = 0
#
# tb1 = TravelBlog()
# tb1.name = 'Франция'
# tb1.days = 6
# TravelBlog.total_blogs += 1
# tb2 = TravelBlog()
# tb2.name = 'Италия'
# tb2.days = 5
# TravelBlog.total_blogs += 1

# Объявите класс с именем Figure и двумя атрибутами:
#
# type_fig: 'ellipse'
# color: 'red'
# Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:
#
# start_pt: (10, 5)
# end_pt: (100, 20)
# color: 'blue'
# Удалите из экземпляра класса свойство color и выведите на экран список всех локальных свойств (без значений) объекта fig1 в одну строчку через пробел в порядке, указанном в задании.
# мой вариант
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = "blue"
# del fig1.color
# print(*fig1.__dict__.keys())#тут без keys тоже работает

# запись элементов объекта через словарь с использованием генератора списка, мой вариант кажется лучше)
# class Figure:
#     type = 'ellipse'
#     color = 'red'
#
# fig1 = Figure()
# d = {
# 'start_pt': (10, 5),
# 'end_pt': (100, 20),
# 'color': 'blue',
# }
# [setattr(fig1, key, value) for key, value in d.items()]
# del fig1.color
# print(*fig1.__dict__)

#вариант как у меня но без распаковки
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'
#
# del fig1.color
# print(*fig1.__dict__)

# Объявите класс с именем Person и атрибутами:
#
# name: 'Сергей Балакирев'
# job: 'Программист'
# city: 'Москва'
# Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное свойство с именем job. Выведите True, если оно присутствует в объекте p1 и False - если отсутствует.
#мой вариант
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
# p1 = Person()
# print("job" in p1.__dict__)

#через hasattr
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
# p1 = Person()
#
# print(hasattr(p1.__dict__, 'job'))

# через try except
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
#
# p1 = Person()
#
# try:
#     p1.__dict__['job']
#     print(True)
# except KeyError:
#     print(False)

# еще один hasattr
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
# p1 = Person()
# print(hasattr(Person, 'p1.job'))

# Методы классов. Параметр self!!!!!!!!!!!!!!
# с помощью методов можно реализовать самые разные алгоритмы
# в названии методов используют глаголы. Именами свойств выступают существительные
# class Point:
#     color = "red"
#     circle = 2
#
#     def set_coords():
#         print("вызов метода set_coords")

# print(Point.set_coords)#название метода это атрибут класса, также как название переменных. В нашем случае этот атрибут связан с определенной функцией
# этот метод также можно вызывать вне класса
# Point.set_coords()
# pt = Point()#создали объект класса Point
# print(pt.set_coords)#этот метод можно вывести, он есть в объекте, то есть передается из класса. Попробуем его вызвать
# pt.set_coords()#отобразится ошибка, напишет что там есть 1 аргумент функции, хотя мы его не прописывали. Так происходит потому, что мы не прописали параметр self. Этот параметр является ссылкой на экземпляр класса, из которого вызывается функция. То есть этот параметр как бы передает в объект эту функцию. Когда мы вызываем функцию через экземпляр класса, то этот параметр указывает и как бы передает эту функцию из класса в экземпляр класса.
# class Point:
#     color = "red"
#     circle = 2
#
#     def set_coords(self):
#         print("вызов метода set_coords")
#
# pt = Point()
# print(pt.set_coords)
# print(Point.set_coords)
# pt.set_coords()#теперь так вызвать можно, так как мы прописали параметр self, и он будет указывать на наш экземпляр, и наш экземпляр автоматом будет подставляться в параметр self для ссылки
# Point.set_coords()#а вот так вызвать теперь нельзя, будет ошибка, так как если вызывать из класса, то ожидается параметр в виде экземпляра класса, а его нет
# Point.set_coords(pt)#так будет работать, но это по факту тоже самое что и pt.set_coords()
# для чего нужен параметр self. Если нам нужно чтобы функция из класса добавляла в экземпляр класса какие либо параметры, то именно для этого нужен self, то есть это как бы ссылка, мы можем вызвать функцию и сделать новые свойства в экземпляре класса при вызове функции со значениями

# class Point:
#     color = "red"
#     circle = 2
#
#     def set_coords(self, x, y):#указали параметры функции
#         self.x = x#указали что параметры функции запишутся в атрибуты экземпляра класса
#         self.y = y#второй атрибут
#     def get_coords(self):#написали функцию которая будет возвращать эти координаты. То есть мы сначала вызвали предыдущую функцию и передали в нее параметры, а теперь мы их этой функцией возвратили
#         return (self.x, self.y)

# pt = Point()
# pt.set_coords(1, 2)#в параметр self автоматом подставился экземпляр класса, а значения передались как свойства экземпляра объекта
# print(pt.__dict__)#теперь у экземпляра появилось 2 новых свойства, атрибута
#то есть функция из класса не копируется в другие экземпляры классов, а только через параметр self ссылается на эти экземпляры, и с помощью параметра self мы можем узнать на какой экземпляр ссылается, то есть это как бы проводник к тому или иному экземпляру класса. И через методы можно менять свойства экземпляров класса
# pt2 = Point()
# pt2.set_coords(10, 20)
# print(pt2.__dict__)#тут будут параметры другие, так как self ссылается на каждый объект отдельно
# print(pt.get_coords())#вызвали функцию которая возвращает параметры функции в виде кортежа
# print(pt2.get_coords())
#все функции из класса, это атрибуты класса. И к ним доступ можно получить через функцию getattr, которая возвращает атрибут класса если он есть в классе
# f = getattr(pt, "get_coords")
# print(f)#теперь переменная f ссылается на функцию из экземпляра класса
# print(f())#и получается можно через переменную вызывать функцию, чтобы не прописывать эту функцию через точку - pt.get_coords(). Но обычно все пишут именно через точку, лишние переменные могут запутать других программистов. Этот пример для того чтобы показать что функции это тоже атрибуты, и они являются обычными данными










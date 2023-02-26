from bs4 import BeautifulSoup#это библиотека для парсинга
with open("1.html", encoding='utf-8') as file:#открываем файл страницы которую будем парсить
    src = file.read()

soup = BeautifulSoup(src, "lxml")#передали код страницы библиотеке BeautifulSoup, то есть преобразуем код в дерево объектов питона. Тут по факту мы создали объект класса BeautifulSoup, он принимает 2 параметра код страницы и название парсера, который будет использован. мы указали парсер lxml, он вроде самый быстрый
#теперь в переменной soup создан объект, и через него можно юзать методы из библиотеки BeautifulSoup и извлекать данные. Для этой библиотеки есть документация, можно порыться и найти нужную функцию
# title = soup.title#тут просто вывели title
# print(title)

# методы .find() и .find_all()     !!!!!
#.find() метод забирает данные из первого попавшего искомого элемента
# page_h1 = soup.find("h1")
# # print(page_h1)
# # .find_all() заберет все искомые загаловки со страницы сверху вниз
# page_all_h1 = soup.find_all("h1")#сохранаяет он их в список
# # print(page_all_h1)
# for i in page_all_h1:#перебрали его в цикле
#     print(i)
#можно указывать атрибут тега, например клас
# user_name = soup.find("div", class_= "user__name")#передали тег, второй аргумент это класс из сраницы html, класс пишем с нижнем слешем
# print(user_name)#тут выведется блок кода целиком. Выглядит он как текст, но по факту это объект soup, и к нему можно применить функции
# print(user_name.text.strip())#применили метод text и будет нужное нам имя выведено, и также можно использовать метод strip и он обрежет не нужные пробелы
# user_name = soup.find("div", class_= "user__name").find("span")#мможно повторно юзать метод find, чтобы искать теги дальше. МОжно не указывать тег div, так как такой класс 1 в файле, но тегов или классов в файле может быть много и лучше его указывать, так как мы можем спарсить не тот класс
#еще один способ фильтрации кода с помощью словаря
# user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text#в словаре написали ключ класс и значение название класса. Также можно указать второй элемент словаря это id из html страницы если он есть на странице, то можно искать по нему
# print(user_name)
#теперь соберем все span теги из блока user__info
# user_info_all_span = soup.find("div", {"class": "user__info"}).find_all("span")
# for i in user_info_all_span:
#     # print(i)
#     print(i.text)#без тега, только значение в теге
# print(user_info_all_span[0])#можно обращаться по индексу, так как это список
# спарсим блок с соцсетями пользователя
# social_link = soup.find("div", {"class": "social__networks"}).find("ul").find_all("a")
# print(social_link)
all_a = soup.find_all("a")
print(all_a)#тут будет выведен список ссылок a href с этим же текстом, но лучше вывести без тегов
for item in all_a:
    item_text = item.text
    item_url = item.get("href")#тут как будто к словарю обращается и выводим инфу по ключу, хотя может и не так. Вобщем юзаем метод get
    # print(item_url)#тут будут просто ссылки, без тегов
    print(f"{item_text}: {item_url}")
    #остановился на 9.32
# ссылка: youtube.com/watch?v=AFqYxaOyqy0&list=PLqGS6O1-DZLprgEaEeKn9BWKZBvzVi_la













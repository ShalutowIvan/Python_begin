#нужно сделать программу которая будет искать элементы списка в файле и выводить элементы строки выше
file = open('123.xml', encoding='utf-8')
s = file.readlines() #присвоили содержимое файла баланса в переменную списка

p = 0#это счетчик для вложенного цикла который ищет фбшки в строке
j = 0
z = list(map(str, input().split()))#это ввод списка алкокодов
f = []
a = 0
print()
for i in range(len(s)):#перебираем переменную списка

    for j in range(len(z)):
        #print(z[j])
        while z[j] in s[i]:
            #if z[p] in s[i]:
            #print(s[i][s[i].find("FB-", 0, -1):s[i].find("FB-", 0, -1)+18])
            #print(s[i][s[i].find(z[j]):s[i].find(z[j])+18])#срез алкокода
            print(s[i][s[i].rfind("FB-", s[i].find(z[j]), s[i].find(z[j])-500):s[i].rfind("FB-", s[i].find(z[j]), s[i].find(z[j])-500)+18])
            print(s[i][s[i].rfind("FB-", s[i].find(z[j], s[i].find(z[j], тут написать начало и конец), s[i].find(z[j])-500):s[i].rfind("FB-", s[i].find(z[j]), s[i].find(z[j])-500)+18])
                print(s[i][s[i].find("AlcCode", 0, -1):s[i].find("AlcCode", 0, -1)-()])
найти первую фбшку до алккоде

            # f.append(s[i][s[i].find("FB-", 0, -1):s[i].find("FB-", 0, -1)+18])
            # a = s[i][s[i].find("FB-", 0, -1):s[i].find("FB-", 0, -1)+18]
            # if a in f[::]:
            #     break
            # #нужно придумать условие для выхода из цикла
        #p += 1
    #p = 0
#print(f)
            

#фор наъодит только одну фбшку нужен цикл вайл, все фб перебрать нужно их может быть несколько

#print(s[129][s[129].find("FB-"):s[129].find("FB-")+15]) это работает


#print(a)
#print(s[0][100])
file.close()





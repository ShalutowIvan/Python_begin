#нужно сделать программу которая будет искать элементы списка в файле и выводить элементы строки выше
file = open('123.txt', encoding='utf-8')
s = file.readlines()
a = 0
z = ["безлунный", "широкой"]
for i in range(len(s)):
    for p in range(len(z)):
        if z[p] in s[i]:
            print(z[p])
            print(s[i-2][17:])


#print(a)

file.close()





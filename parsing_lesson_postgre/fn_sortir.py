
# сделать вывод с одной фамилией и далее вся еда которую ел пупс, потом по каждой дате свой список еды. То есть фамилия, дата и список еды. Не забыть про срезы в столбце дата, чтобы была только дата, без времени


data = record[0][4] + "\n"
res = []
for i in range(len(record)):	
	if data != record[i][4] + "\n":
		data = record[i][4] + "\n"
	if data not in res:
		res.append(data)
		

	for j in range(1, len(record[i])-1):
		if j == 1:
			if len(record[i][j]) < 30:
				res.append("|" + record[i][j] + "-"*(30 - len(record[i][j])))
			else:
				res.append("|" + record[i][j])
		if j == 2:
			if len(record[i][j]) < 7:
				res.append("|" + record[i][j] + "-"*(7 - len(record[i][j])))
			else:
				res.append("|" + record[i][j])

		if j == 3:
			res.append("|" + record[i][j]+"|\n")
			continue
		

res = "ФИО: " + record[0][0] + "\n|-------------Пища-------------|-Объем-|Время|" + "\n" + "".join(res)

print(res)






d = input("Введите дату: ")
if int(d[:d.find(".")]) <= 31:
	d = d[d.rfind(".")+1:] + "." + d[d.find(".")+1:d.rfind(".")] + "." + d[:d.find(".")]
elif int(d[:d.find(",")]) <= 31:
	d = d[d.rfind(",")+1:] + "-" + d[d.find(",")+1:d.rfind(",")] + "-" + d[:d.find(",")]
elif int(d[:d.find("-")]) <= 31:
	d = d[d.rfind("-")+1:] + "-" + d[d.find("-")+1:d.rfind("-")] + "-" + d[:d.find("-")]
elif int(d[:d.find("/")]) <= 31:
	d = d[d.rfind("/")+1:] + "-" + d[d.find("/")+1:d.rfind("/")] + "-" + d[:d.find("/")]
elif int(d[:d.find(":")]) <= 31:
	d = d[d.rfind(":")+1:] + "-" + d[d.find(":")+1:d.rfind(":")] + "-" + d[:d.find(":")]


print(d)
# import schedule
# import requests

# def greeting():
# 	todos_dict = {
# 	'08:00': 'Drink coffee',
# 	'11:00': 'Work meeting',
# 	'23:59': 'Hack the planet!'
# 	}
# 	print("Day's tasks")
# 	for k, v in todos_dict.items():
# 		print(f'{k} {v}')

# 	response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
# 	data = response.json()
# 	btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$"

# 	# 'last': 30630

# 	print(btc_price)


# def main():
# 	# schedule.every(4).seconds.do(greeting)#функция будет запускаться каждые 4 секунды
# 	# schedule.every(5).minutes.do(greeting)##функция будет запускаться каждые 5 минут
# 	# schedule.every().hour.do(greeting)##функция будет запускаться каждый час
# 	# schedule.every().day.at('04:38').do(greeting)#это вызов функции каждый день в определенное время
# 	# schedule.every().thursday.do(greeting)#это в определенный день недели
# 	# schedule.every().friday.at('23:50').do(greeting)#это в определнный день в определенное время




# 	while True:
# 		schedule.run_pending()

# if __name__ == '__main__':
# 	main()

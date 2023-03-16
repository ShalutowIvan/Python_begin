#в окружение поставил модули lxml, beautifulsoup4, requests для парсинга
# import requests
# from bs4 import BeautifulSoup
# import re
#
# def searcher():
#     response = requests.get("https://www.youtube.com/results?search_query=python")
#     soup = BeautifulSoup(response.content, "html.parser")
#     search = soup.find_all("script")[32]#ищем тег скрипт
#     key = '"videoId":"'
#     data = re.findall(key+r"([^*]{11})", str(search))
#     print(data)
#
# searcher()#это плохой вариант, он медленно работает, в моем случае вообще не работает
#сделаем через библиотеку youtube_search
# from youtube_search import YoutubeSearch
#
# def searcher():
#     res = YoutubeSearch("python telegram bot", max_results=1).to_dict()
#     with open("text.py", "w", encoding="utf-8") as r:#записали наш парсинг в файл в виде словаря
#         r.write(str(res))
#
# searcher()
#теперь сделаем все это в боте
import hashlib

from youtube_search import YoutubeSearch
from config import TOKEN

from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

def searcher():
    res = YoutubeSearch("python telegram bot", max_results=1).to_dict()
    return res

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.inline_handler()
async def inline_handler(q: types.InlineQuery):
    text = q.query or 'echo'
    links = searcher(text)
    articles = [types.InlineQueryResultArticle(
        id = hashlib.md5(f"{link["id"]}"),





    ) for link in links]
    await q.answer(articles, cache_time=60, is_personal=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)







#код бота

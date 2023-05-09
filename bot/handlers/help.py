from aiogram import types
from loader import dp
import emoji

@dp.message_handler(text='Помощь')
async def command_help(message: types.Message):#будет вызываться при написании команды /start
    await message.answer(f"Привет {message.from_user.full_name}!\n\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}Этот бот предназначен для учета кормлений ребенка, сна и туалета. Также есть функционал для записи к врачу с напоминаниями о записи. Еще можно записывать рост и вес после осмотров педиатра каждый месяц с последующим просмотром. Также во всех таблицах есть функционал для просмотра записей за период либо последней записи.\n\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}<b>!!!!!ВАЖНО!!!!!</b> "
                         f"При первом использовании бота сначала нужно зарегистрироваться по кнопке 'Регистрация'. Потом можно воспользоваться кнопкой вход. Первоначально нужно добавить ребенка. Если этого не сделать, то в отчетах в графе ФИО будет пусто.\n\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}Добавление ребенка. И функционал кнопки 'О ребенке'.\n"
                         f"Нужно нажать кнопку 'Информация о ребенке', далее выбрать 'Добавить ребенка'. Потом в следующем меню нажать 'добавить ребенка' и ввести необходимые данные. Можно нажать просмотр и увидеть что вы ввели. Если что-то не так, можно удалить и добавить еще раз.\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}В этом же разделе есть функционал для записи к врачу. При записи нужно указать описание записи к врачу, потом указать время для напоминания. При указании описания можете описать название врача, дату время записи, кабинет и прочую информацию.\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}Есть кнопка для указания роста и веса ребенка. Это заполнять по желанию. Рост и вес будут указаны по текущей дате добавления.\n\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}Функционал кнопки Еда.\n"                         
                         f"Можно добавлять еду, просмотривать отчет за период или последнюю запись. Также можно удалять последнюю запись.\n\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}Функционал кнопки Сон.\n"
                         f"Можно добавлять количество часов сна. Можно указывать дробное число. Есть функционал формирования отчета за период и удаления последней записи.\n\n"
                         f"{emoji.emojize(':backhand_index_pointing_right:')}Функционал кнопки Туалет.\n"
                         f"Можно указать время в момент когда сходил ребенок. Можно сформировать отчет, просмотривается все записи за все время, если таблица станет слишком большая, то можете удалять лишние записи по кнопке 'Удалить'. Либо можете оставлять так как есть.")

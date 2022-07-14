import telebot

import withstickers as stick

authors_id = ['123456', '654321', '565656']

welc_text = (
  'Здравствуй! Рад тебя видеть :)\n\nЯ помогу тебе сделать частью твоей жизни практику благодарности. Знаешь, что это такое?')

text_feel_1_male = 'Подумай о том, что ты сегодня сделал.\n\nБыли ли какие-то сложные вещи, с которыми ты справился? А может быть, простые, но важные?\n\n Мы просыпаемся, чистим зубы, готовим завтрак, идем на работу, замечаем что-то красивое, изучаем новую информацию, общаемся. За все эти привычные вещи здорово чувствовать благодарность — раньше мы их не умели делать.\n\nРаньше у нас не было таких друзей, такой работы, такого компьютера, таких мыслей, такого понимания. Мы добились этого. И важно поблагодарить себя за это.'
text_feel_1_female = 'Подумай о том, что ты сегодня сделала.\n\nБыли ли какие-то сложные вещи, с которыми ты справилась? А может быть, простые, но важные?\n\n Мы просыпаемся, чистим зубы, готовим завтрак, идем на работу, замечаем что-то красивое, изучаем новую информацию, общаемся. За все эти привычные вещи здорово чувствовать благодарность — раньше мы их не умели делать.\n\nРаньше у нас не было таких друзей, такой работы, такого компьютера, таких мыслей, такого понимания. Мы добились этого. И важно поблагодарить себя за это.'
text_feel_2 = 'Вот список благодарностей Льва @levlevitsky за 28 октября 2021:\n' \
              + 'Я благодарен за то, что...\n' \
              + '- созвонился с подругой\n' \
              + '- купил себе удобную подушку\n' \
              + '- заметил красивые ветви дерева и сфотографировал их\n' \
              + '- был красивый закат\n' \
              + '- посмотрел вечером интересный фильм\n' \
              + '- выпил чашку вкусного травяного чая с печеньем\n' \
              + 'Уверен, хоть одну благодарность у тебя получится придумать)\n'

text_write_grate_male = 'Продолжи фразу. Сегодня я благодарен за то, что...'
text_write_grate_female = 'Продолжи фразу. Сегодня я благодарна за то, что...'

text_writed_grate_male = 'Я был благодарен за то, что '
text_writed_grate_female = 'Я была благодарна за то, что '

awesome_text_male = "Потрясающе! Только что ты записал свою первую благодарность.\n\nНу как, начинаешь чуть больше ценить себя и свою жизнь?"
awesome_text_female = "Потрясающе! Только что ты записала свою первую благодарность.\n\nНу как, начинаешь чуть больше ценить себя и свою жизнь?"

good_female = 'Хорошо! Ты нереальная умничка, что начала свой путь.'
good_male = 'Хорошо! Ты нереальный молодец, что начал свой путь.'

list_moments = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00',
                '19:00', '20:00', '21:00', '22:00', '23:00', '0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00',
                '7:00']

# bot_team_text = 'Идея и продукт:\nЛев Левицкий\n@levlevitsky | @levlevitsky\_channel\n\nCтратегия и коммуникация:\nДенис Симонов\n@simonovdenis | @siimonovd\n\nРазработка:\nVladimir Networker\n@piofant\n\n[Поддержать команду бота](https://www.tinkoff.ru/rm/levitskiy.lev1/Rh9ZI13482)'
##bot_team_text = 'Идея и продукт:\nЛев Левицкий\n@levlevitsky\n\nCтратегия и коммуникация:\nДенис Симонов\n@simonovdenis\n\nРазработка:\nVladimir Networker\n@piofant\n\nProject Manager & Localisation:\nАнастасия Широбокова\n@hedgehoggyhoge\n\n[Поддержать команду бота](https://www.donationalerts.com/r/levlevitsky)'
bot_team_text = 'Идея и продукт:\n' \
                + 'Лев Левицкий\n' \
                + '@levlevitsky // @levlevitsky\_channel\n\n' \
                + 'Cтратегия и коммуникация:\n' \
                + 'Денис Симонов\n' \
                + '@simonovdenis // @siimonovd\n\n' \
                + 'Разработка:\n' \
                + '@piodao // @pioblog\n' \
                + '(Если что-то не работает – пишите мне)\n\n' \
                + 'Вся команда:\n' \
                + 'mental-health-matters.ru/botik-zabotik'

help_contacts = 'Если ты чувствуешь, что тебе нужна помощь прямо сейчас, позвони на бесплатную горячую линию МЧС России:\n+78003334434. Это бесплатно и анонимно.\n\nКруглосуточная психологическая помощь для жителей Москвы: +74992165050\n\nСайты, где можно найти психолога или психотерапевта:\nbemeta.co\nzigmund.online\npsyalter.ru\nyasno.live'

support_male = "Да! Не забывай, что ты прекрасен и ценен именно таким, какой ты есть.\n\nПослушай вот это: https://shellsays.art/ru\n\nВот 5 твоих случайных благодарностей за последний месяц. Уверен, они тебя порадуют :)\n\n"
support_female = "Да! Не забывай, что ты прекрасна и ценна именно такой, какая ты есть.\n\nПослушай вот это: https://shellsays.art/ru\n\nВот 5 твоих случайных благодарностей за последний месяц. Уверен, они тебя порадуют :)\n\n"

knowledge_base = 'Мы вместе с командой собрали бесплатный гайд для изучения ментального здоровья:\n\n' \
                 + 'https://mental-health-matters.ru\n\n' \
                 + 'В нем собраны видео, статьи и подкасты на темы:\n' \
                 + '— эмоции\n' \
                 + '— выгорание\n' \
                 + '— работа и эффективность\n' \
                 + '— смысл жизни и счастье\n' \
                 + '— общение\n' \
                 + '— отношения\n' \
                 + '— перфекционизм\n\n' \
                 + '… и многие другие\n\n' \
                 + 'Если ты знаешь классное видео или подкаст, которого еще нет на сайте, пришли его в личку @levlevitsky'

empty = telebot.types.ReplyKeyboardRemove()
yes_no = telebot.types.ReplyKeyboardMarkup(True).row('Да', 'Нет')
back = telebot.types.ReplyKeyboardMarkup(True).row('Назад')
aga = telebot.types.ReplyKeyboardMarkup(True).row('Ясно')
cont = telebot.types.ReplyKeyboardMarkup(True).row('Далее')
cont_back = telebot.types.ReplyKeyboardMarkup(True).row('Далее').row('Назад')
support_1 = telebot.types.ReplyKeyboardMarkup(True).row('Правда?')
about2_text = telebot.types.ReplyKeyboardMarkup(True).row('А что об этом думает наука?')
about3_text = telebot.types.ReplyKeyboardMarkup(True).row('Как именно нужно делать практику благодарности?')
about4_text = telebot.types.ReplyKeyboardMarkup(True).row('А у других людей были такие проблемы?')
about5_text = telebot.types.ReplyKeyboardMarkup(True).row(stick.thanks_2)

what_to_do = telebot.types.ReplyKeyboardMarkup(True).row('Что мне делать?')
lets_try = telebot.types.ReplyKeyboardMarkup(True).row('Хочу попробовать!')
gender = telebot.types.ReplyKeyboardMarkup(True).row('Я благодарен').row('Я благодарна')
readiness = telebot.types.ReplyKeyboardMarkup(True).row('Да!').row('Не знаю, что написать')
feel_1_key = telebot.types.ReplyKeyboardMarkup(True).row('Готов чувствовать благодарность!').row(
  'Все еще ничего не приходит на ум')
run = telebot.types.ReplyKeyboardMarkup(True).row('Погнали')
result_feel = telebot.types.ReplyKeyboardMarkup(True).row('Да, чувствую!', 'Пока нет :(')
how_1 = telebot.types.ReplyKeyboardMarkup(True).row('Как например?')
grate_again = telebot.types.ReplyKeyboardMarkup(True).row('Хочу!', 'Пока нет')
what_time = telebot.types.ReplyKeyboardMarkup(True).row('А в какое время лучше?')
i_understood = telebot.types.ReplyKeyboardMarkup(True).row('Понятно. Главное — каждый день!')
many_moments = telebot.types.ReplyKeyboardMarkup(True).row('Отключить напоминания').row('8:00', '9:00', '10:00',
                                                                                        '11:00').row('12:00', '13:00',
                                                                                                     '14:00',
                                                                                                     '15:00').row(
  '16:00', '17:00', '18:00', '19:00').row('20:00', '21:00', '22:00', '23:00').row('0:00', '1:00', '2:00', '3:00').row(
  '4:00', '5:00', '6:00', '7:00').row('Назад')
again_or_not = telebot.types.ReplyKeyboardMarkup(True).row('Хочу записать еще благодарность').row('Пока хватит')
many_moments_onboarding = telebot.types.ReplyKeyboardMarkup(True).row('8:00', '9:00', '10:00', '11:00').row('12:00',
                                                                                                            '13:00',
                                                                                                            '14:00',
                                                                                                            '15:00').row(
  '16:00', '17:00', '18:00', '19:00').row('20:00', '21:00', '22:00', '23:00').row('0:00', '1:00', '2:00', '3:00').row(
  '4:00', '5:00', '6:00', '7:00')

last_grates_buttons = telebot.types.ReplyKeyboardMarkup(True).row('В главное меню').row('Показать все').row(
  'Неделю назад')
# main_menu_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Новая благодарность', 'Мои благодарности').row('Получить поддержку','О практике благодарности').row('Настройки','Команда бота')
###main_menu_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Новая благодарность', 'Мои благодарности').row('Получить поддержку','О практике благодарности').row('Настройки','Команда бота').row('База знаний', stick.insp)
# main_menu_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Новая благодарность', 'Мои благодарности').row('Получить поддержку','О практике благодарности').row('Настройки','Команда бота').row(stick.insp)
main_menu_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Новая благодарность', 'Мои благодарности').row(
  'Получить поддержку', 'О практике благодарности').row(stick.insp).row('Настройки', 'Команда бота', 'База знаний')

settings_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Имя').row('Обращение').row('Напоминалки').row(
  'Благодарности').row('Достижения').row('В главное меню')
support_2 = telebot.types.ReplyKeyboardMarkup(True).row('Мне нужна помощь').row('Спасибо, мне лучше')

after_setting = telebot.types.ReplyKeyboardMarkup(True).row('Другие настройки').row('Записать благодарность').row(
  'В главное меню')

to_main_munu_button = telebot.types.ReplyKeyboardMarkup(True).row('В главное меню')

thanks_button = telebot.types.ReplyKeyboardMarkup(True).row(stick.thanks)
grate_settings_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Удалить все благодарности').row('Назад')
grate_settings_buttons_confirm = telebot.types.ReplyKeyboardMarkup(True).row('Подтвердить').row('Назад').row(
  'В главное меню')
safety = telebot.types.ReplyKeyboardMarkup(True).row('Обязательно! Кстати, а что с безопасностью?')
exellent = telebot.types.ReplyKeyboardMarkup(True).row('Отлично!')
confirm_voice_request_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Принять', 'Отклонить')
achieve_methods = telebot.types.ReplyKeyboardMarkup(True).row('Круглое видеосообщение').row('Голосовое сообщение').row(
  'Текстовое сообщение')
after_notif_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Новая благодарность').row(
  'Выбрать другое время напоминания').row('Отключить напоминания').row('Главное меню', 'Команда бота')
notif_off_text = 'Напоминания больше не будут приходить. Ты всегда можешь включить их в настройках, выбрав удобное время для напоминания.\n\nТы в главном меню.'
notif_off_text_from_settings = 'Напоминания больше не будут приходить. Ты всегда можешь включить их в настройках, выбрав удобное время для напоминания.'

check_that_new_grate_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Да', 'Нет')

insp_1_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Получить', 'Поделиться').row('В главное меню')
insp_share_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Голосом', 'Текстом').row('Назад')
insp_get_buttons = telebot.types.ReplyKeyboardMarkup(True).row('Послушать', 'Почитать').row('Назад')
after_text_insp = telebot.types.ReplyKeyboardMarkup(True).row('Ещё', 'Назад').row('В главное меню')
after_voice_insp = telebot.types.ReplyKeyboardMarkup(True).row('Ещё', 'Назад').row('В главное меню')

insp_one_button = telebot.types.ReplyKeyboardMarkup(True).row(stick.insp)

notif_texts_list = [
  'Привет-привет! Пора уделить минуту практике благодарности, чтобы стать еще немножко счастливее 😌',
  'Давай запишем несколько хороших вещей, которые произошли в твоей жизни? Смело нажимай на «Новую благодарность»! 🌿',
  'Хееей! Самое время потратить пару минут на практику благодарности, чтобы сформировать у себя привычку чаще замечать хорошее 🍀',
  'За что ты сегодня хочешь поблагодарить себя и мир вокруг? Запиши несколько вещей, когда у тебя будет время ☀️',
  'Что порадовало и вдохновило тебя сегодня? Давай запишем несколько благодарностей 🦋',
  'Если тебе сейчас тревожно, попробуй ненадолго оторваться от дел и записать несколько благодарностей! Обещаю — тебе сразу станет радостнее и спокойнее 🌌',
  'Поделишься со мной своими благодарностями за сегодня? Я очень жду и уже готов радоваться вместе с тобой 🥳',
  'Расскажешь, что хорошего с тобой произошло сегодня? Меня каждый раз так вдохновляют твои успехи 💫'
]
notif_off = 'Изменить время или отключить напоминания: /set_notification'

digest_text_1 = 'Привет! Давай вспомним про прекрасные и радостные вещи, которые произошли с тобой за эту неделю 😉\n\n' \
                + 'Количество твоих благодарностей за неделю: '
digest_text_2 = '.\n\n'
digest_text_3 = '\n' \
                + 'Перечитай их и попробуй снова почувствовать радость и благодарность, которая наполняла тебя в моменте 🔆\n\n' \
                + 'Перечитывать благодарности важно, чтобы сформировать более позитивное восприятие прошлого.\n\n' \
                + 'В качестве бонуса — ты чаще начинаешь замечать, какая у тебя классная и разнообразная жизнь 🌊'

import telebot

main_phrase = "Хочешь начать больше ценить свою жизнь, свои действия и успехи? Тогда очень здорово, что мы встретились.\n\nЯ помогаю людям делать практику благодарности. Это тот самый работающий способ стать немного счастливее. Его используют в когнитивно-поведенческой терапии, чтобы приучить мозг обращать внимание на хорошее, а не на плохое.\n\nСкорее нажимай /start — и я все тебе расскажу 💜\n\nЕсли что-то не работает или есть мысли, как сделать меня лучше, напиши Льву Левицкому @levlevitsky"
notifi = 'Приветик! Пора уделить минуту практике благодарности, чтобы стать еще немножко счастливее ☺️️️\n\n5 твоих последних благодарностей:\n'
dofamin_male = ['Великолепно! Не устаю тобой восхищаться 🌸',
                'Это просто потрясающе! У меня даже других слов нет 💜',
                'Ого, невероятно круто! 😍',
                'Молодчина! 🥰',
                'Вау, как же ты хорош! ✨',
                'Умничка! 😎',
                'Я невероятно ценю то, что ты делаешь. Спасибо тебе ❤️',
                'Отлично! Я в восторге 💙',
                'Вау! Ты нереальный красавчик! 💫',
                'Огонь! Ты просто супер 🔥',
                'Ура! Так держать 🌟',
                'Слушай, это просто фантастика! 🤟',
                'Как же здорово! Я горжусь тобой 🌿',
                'Я с тобой, ты умничка 🤍',
                'Все, что ты делаешь — важно и нужно 🌱',
                'Я горжусь тем, что ты делаешь! Не останавливайся❣️',
                'Продолжай видеть хорошее в том, что ты делаешь💗',
                'Я так радуюсь, когда тебе хорошо и комфортно 🌻',
                'Я в восторге! Это было просто легендарно 🏆',
                'У меня дух захватывает от этой благодарности 🥰',
                'Ты все делаешь правильно 🦋',
                'Это просто космос! 🌌',
                'Путь в тысячу миль начинается с одного шага! И ты его только что сделал ✅',
                'Вспомни, с чего ты начинал! Это огромный прогресс ✊']

dofamin_female = ['Великолепно! Не устаю тобой восхищаться 🌸',
                  'Это просто потрясающе! У меня даже других слов нет 💜',
                  'Ого, невероятно круто! 😍',
                  'Молодчина! 🥰',
                  'Вау, как же ты хороша! ✨',
                  'Умничка! 😎',
                  'Я невероятно ценю то, что ты делаешь. Спасибо тебе ❤️',
                  'Отлично! Я в восторге 💙',
                  'Вау! Ты нереальная красотка! 💫',
                  'Огонь! Ты просто супер 🔥',
                  'Ура! Так держать 🌟',
                  'Слушай, это просто фантастика! 🤟',
                  'Как же здорово! Я горжусь тобой 🌿',
                  'Я с тобой, ты умничка 🤍',
                  'Все, что ты делаешь — важно и нужно 🌱',
                  'Я горжусь тем, что ты делаешь! Не останавливайся❣️',
                  'Продолжай видеть хорошее в том, что ты делаешь💗',
                  'Я так радуюсь, когда тебе хорошо и комфортно 🌻',
                  'Я в восторге! Это было просто легендарно 🏆',
                  'У меня дух захватывает от этой благодарности 🥰',
                  'Ты все делаешь правильно 🦋',
                  'Это просто космос! 🌌',
                  'Путь в тысячу миль начинается с одного шага! И ты его только что сделала ✅',
                  'Вспомни, с чего ты начинала! Это огромный прогресс ✊']
about_6_text = '@projectgratefulbot нужен, чтобы люди могли становиться позитивнее и счастливее, тратя на это меньше усилий. Приятного тебе путешествия в мире благодарностей 💜'
about_7_text = 'Тебе спасибо, что доверяешь нам)\n\nЕсли тебе нравится бот, можешь поделиться им в соцсетях, рассказать о нем друзьям и [поддержать нашу команду](https://www.tinkoff.ru/rm/levitskiy.lev1/Rh9ZI13482).\n\nТак еще больше людей получат возможность стать немного счастливее ✨'
thanks = 'Спасибо 💜️'
thanks_2 = 'Спасибо ☺️'
cute = telebot.types.ReplyKeyboardMarkup(True).row('Здорово ☺️')

achieve_text_10 = "Вау! У тебя уже 10 благодарностей!"
achieve_text_50 = "Ух ты! У тебя уже целых 50 благодарнстей!"
achieve_text_100 = "Здорово! У тебя целых 100 благодарностей!"
insp = 'Вдохновение ✨'

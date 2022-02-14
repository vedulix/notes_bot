from datetime import datetime

import pymysql
from telegraph import Telegraph

import config


def base_connect():
    conn = pymysql.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        db=config.db,
        charset='utf8mb4')
    return conn


def ex_command(command):
    conn = base_connect()
    with conn:
        try:
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()
            return ("wow")
        except Exception as ex:
            print(type(ex), ex, "!!!   Ошибка при изменении БД   !!!", sep='\n')
            return ("bad")


def data_command(command):
    conn = base_connect()
    with conn:
        try:
            cur = conn.cursor()
            cur.execute(command)
            rows = cur.fetchall()
            return rows
        except Exception as ex:
            print(ex, type(ex), "!!!   Ошибка при выборке данных из БД!!!   ", sep='\n')
    return []


def to_telegraph_link(text, chat_id):
    telegraph = Telegraph()
    html_co = 'Количество благодарностей: ' + count_all(chat_id) + ".<br>" + text.replace('•', '<br>•')[4:]
    telegraph.create_account(short_name='@projectgratefulbot')

    response = telegraph.create_page(
        'Ваши благодарности' + ' (' + str(datetime.now())[11:19] + ')',
        html_content=html_co
    )
    ex_command(
        "update bot_users set last_notes = '" + str('http://telegra.ph/{}'.format(response['path'])) + "' where chat_id = '" + str(chat_id) + "';")
    return ('http://telegra.ph/{}'.format(response['path']))


def to_str_grid(rows):
    str_grid = ""
    try:
        for row in rows:
            a = str(row[0:-2])[1:-1] + "\n"
            a = a.replace("(", " ")
            a = a.replace(")", " ")
            a = a.replace(", ", "-")
            a = a.replace("datetime.datetime", "Дата и время: ")
            str_grid += (a + str(row[-2:-1])[1:-1] + "\n\n")
    except Exception as ex:
        print(type(ex), "!!!   Ошибка при конвертировании таблицы в строку   !!!")
    return str_grid


def to_id_list(column):
    a = str(column)
    num_list = []
    num = ''
    for char in a:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return num_list


def to_time_list(column):
    num_list = list(column)
    for i in range(len(num_list)):
        num_list[i] = str((num_list[i]))[2:-3]
    return num_list


def gender_text(id, male_text, female_text):
    k = (data_command("select gender from bot_users WHERE chat_id = '" + str(id) + "';")[0][0])
    if k == 'female':
        return (female_text)
    elif k == 'male':
        return (male_text)
    else:
        return (male_text)


def gratelist_to_str(timelist):
    text = ""
    for a in range(len(timelist)):
        text = text + "•  " + str(timelist[a][0]) + " (" + nice_date(timelist[a][1]) + ")\n"
    return text


def get_number_of_users():
    return data_command("select count(*) from bot_users")[0][0]


def nice_date(dt):
    text = dt.strftime("%d ") + dt.strftime("%B")[:3]
    return text


def last_grates(interval, max_interval, idd):
    if max_interval == 0 and interval == 7:
        text = "Твои благодарности за последние 7 дней:\n\n"
    elif max_interval == 7 and interval == 14:
        text = "Неделю назад ты был благодарен за то, что:\n\n"
    else:
        text = "Еще неделю назад ты был благодарен за то, что:\n\n"
    if max_interval == "last":
        text = ""
        timelist = data_command(
            "SELECT note, date FROM notes WHERE chat_id = '" + str(idd) + "' ORDER BY date DESC LIMIT 5;")
    elif max_interval == "all":
        timelist = data_command(
            "SELECT * FROM (SELECT note, date FROM notes WHERE chat_id = " + str(idd) + ") t ORDER BY date DESC;")
        text = ""
    else:
        timelist = data_command(
            "SELECT * FROM (SELECT note, date FROM notes WHERE date > DATE_SUB(NOW(), INTERVAL " + str(
                interval) + " DAY) AND date < DATE_SUB(NOW(), INTERVAL " + str(
                max_interval) + " DAY) AND chat_id = " + str(idd) + ") t ORDER BY date DESC;")
    text = text + gratelist_to_str(timelist)
    return text


def double_list():
    timelist = data_command("SELECT chat_id, scheduler FROM bot_users;")
    return timelist

def parse_list():
    timelist = data_command("SELECT user_photo, first_name, last_name, username, last_notes FROM bot_users;")
    return timelist

def double_list_username():
    timelist = data_command("SELECT chat_id, username FROM bot_users;")
    return timelist


def rand_grate(id, num, interval):
    text = ""
    timelist = data_command(
        "SELECT * FROM (SELECT note, date FROM notes WHERE date > DATE_SUB(NOW(), INTERVAL 30 DAY) AND chat_id = '" + str(
            id) + "' ORDER BY rand() LIMIT " + str(num) + ") t ORDER BY date DESC;")
    print(timelist)
    text = gratelist_to_str(timelist)
    return text


def delete_all(id):
    ex_command("DELETE FROM notes WHERE chat_id = '" + str(id) + "'")


def count_all(chat_id):
    result = data_command("SELECT COUNT(id) FROM notes WHERE chat_id=" + str(chat_id) + ";")
    return str(result[0][0])


def get_username(chat_id):
    return '@' + str(bfunc.data_command("SELECT * FROM `bot_users` WHERE chat_id = " + str(chat_id))[0][5])


def delete_user(chat_id):
    ex_command("DELETE FROM bot_users WHERE chat_id = '" + str(chat_id) + "'")
    print('Удалил лентяя ' + str(chat_id))


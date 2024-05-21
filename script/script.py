import platform
from datetime import datetime
import time


start = datetime.now()
finish = datetime.now()

path_to_hosts = r'C:\Windows\System32\drivers\etc\hosts'

# if platform.system() == 'Windows':
#     path_to_hosts = r'C:\Windows\System32\drivers\etc\hosts'

redirect = '127.0.0.1'
websites = []
blocked_sites = []


def block():
    while True:
        site = input("Введите сайт для блокировки: ")
        if site == 'exit':
            break
        websites.append(site)
        print(f'Ссылка {site} добавлена! ')
        print("Для выхода отправьте 'exit' ")

    with open(path_to_hosts, 'r+') as f:
        content = f.read()
        for site in websites:
            if site in content:
                pass
            else:
                f.write(f'{redirect} {site}\n')

def unblock():
    while True:
        site = input("Введите сайт для разблокировки: ")
        if site == 'exit':
            break
        websites.append(site)
        print(f'Ссылка {site} добавлена! ')
        print("Для выхода отправьте 'exit' ")

    with open(path_to_hosts, 'r+') as f:
        content = f.readlines()
        f.seek(0)
        for line in content:
            if not any(site in line for site in websites):
                f.write(line)
        f.truncate()

def time_block():
    while True:
        print(blocked_sites)
        check = input('Чтобы продолжить введите 1, чтобы закончить работу введите 2\n')
        if check == '2':
            break
        try:
            start_block_time = float(input('Введите время, с которого доступ на сайт будет ограничен! Пример: 8.10\n'))
            finish_block_time = float(input('Введите время, с которого доступ на сайт будет разрешен! Пример: 20.00\n'))
        except:
            print('Ошибка, время было введено некорректно!')


        global start, finish
        start_list = str(start_block_time).split('.')
        finish_list = str(finish_block_time).split('.')
        start = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(start_list[0]), int(start_list[1]))
        finish = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(finish_list[0]), int(finish_list[1]))
        # print(start)
        website = input('Введите название сайта:\n')
        if website == 'exit':
            break
        else:
            blocked_sites.append(website)
        if start < datetime.now() < finish:
            with open(path_to_hosts, 'r+') as f:
                content = f.read()

                for site in blocked_sites:
                    if site in content:
                        pass
                    else:
                        f.write(f'{redirect} {site}\n')
        else:
            with open(path_to_hosts, 'r+') as f:
                content = f.readlines()
                f.seek(0)

                for line in content:
                    if not any(site in line for site in blocked_sites):
                        f.write(line)
                f.truncate()

        time.sleep(5)




while True:
    choosing_action = input('1. Заблокировать сайт\n2. Разблокировать сайт\n3. Заблокировать на определенный период времени.\n')
    if choosing_action == '1' or choosing_action == '2' or choosing_action == '3':
        break
    print('Выберите вариант ответа!')

if choosing_action == '1':
    block()
elif choosing_action == '2':
    unblock()
elif choosing_action == '3':
    time_block()



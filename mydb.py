import sqlite3


def connect():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    return conn, cursor


def create_table():
    conn, cursor = connect()

    cursor.execute(f'CREATE TABLE video_card (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE cpu (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE motherboard (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE cooling (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE ram (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE ssd (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE hdd (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE housing (name TEXT, price FLOAT, info TEXT)')
    conn.commit()

    cursor.execute(f'CREATE TABLE power_supply (name TEXT, price TEXT, info TEXT)')
    conn.commit()

    conn.close()


def update_table():
    conn, cursor = connect()

    cpu_list = [
    [
        'Процессор AMD Ryzen 7 3700X OEM',
        28989,
        """
Ядро:
Matisse
Гнездо процессора:
SocketAM4
Количество ядер:
8
Количество потоков:
16
Частота:
3.6 ГГц и 4.4 ГГц в режиме Turbo
L3 кэш:
32 МБ
Технологический процесс:
7 нм
Тип поставки:
OEM
Тип памяти:
DDR4
Количество каналов памяти:
2
Версия PCI Express:
PCI Express 4.0
        """
    ],
    [
        'Процессор AMD Ryzen 5 3600',
        16990,
        """
Ядро:
Matisse
Гнездо процессора:
SocketAM4
Количество ядер:
6
Количество потоков:
12
Частота:
3.6 ГГц и 4.2 ГГц в режиме Turbo
L3 кэш:
32 МБ
Технологический процесс:
7 нм
Тип поставки:
OEM
Тип памяти:
DDR4
Количество каналов памяти:
2
Версия PCI Express:
PCI Express 4.0
        """
    ],
    [
        'Процессор AMD Ryzen 7 2700',
        12390,
        """
Ядро
Pinnacle Ridge
Гнездо процессора
SocketAM4
Количество ядер
8
Количество потоков
16
Частота
3.2 ГГц и 4.1 ГГц в режиме Turbo
L3 кэш
16 МБ
Технологический процесс
12 нм
Тип поставки
OEM
Тип памяти
DDR4
Количество каналов памяти
2
Версия PCI Express
PCI Express 3.0
        """
    ],
    [
        'Процессор INTEL Core i5 9400F',
        11590,
        """
Ядро
Coffee Lake
Гнездо процессора
LGA 1151v2
Количество ядер
6
Количество потоков
6
Частота
2.9 ГГц и 4.1 ГГц в режиме Turbo
L3 кэш
9 МБ
Технологический процесс
14 нм
Тип поставки
OEM
Максимальный объем памяти
128 ГБ
Тип памяти
DDR4
Количество каналов памяти
2
Версия PCI Express
PCI Express 3.0
        """
    ],
    [
        'Процессор AMD Ryzen 5 2600',
        10790,
        """
Ядро
Pinnacle Ridge
Гнездо процессора
SocketAM4
Количество ядер
6
Количество потоков
12
Частота
3.4 ГГц и 3.9 ГГц в режиме Turbo
L3 кэш
16 МБ
Технологический процесс
12 нм
Тип поставки
OEM
Тип памяти
DDR4
Количество каналов памяти
2
Версия PCI Express
PCI Express 3.0
        """
    ],
    ]

    for cpu in cpu_list:
        sql = f'INSERT INTO cpu VALUES (?, ?, ?)'
        cursor.execute(sql, (
            cpu[0],
            cpu[1],
            cpu[2]
        ))
        conn.commit()

    conn.close()


def get_table(table):
    conn, cursor = connect()

    cursor.execute(f'SELECT * FROM {table}')
    data = cursor.fetchall()

    conn.close()

    return data


def get_full_info(code, name):
    conn, cursor = connect()
    
    sql = f'SELECT * FROM {code} WHERE name = ?'
    cursor.execute(sql, (name, ))
    data = cursor.fetchone()
    
    conn.close()

    text = data[0]
    price = data[1]
    info = data[2]

    return text, price, info

    
# print(get_full_info('cpu', 'Процессор AMD Ryzen 7 3700X OEM'))
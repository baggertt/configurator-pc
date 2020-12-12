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

    video_card_list = [
[
	'Видеокарта MSI nVidia GeForce GTX 1660TI', # 1
  	28690,
  	"""
Видеочипсет
nVidia GeForce GTX 1660TI
Частота графического процессора
1536 МГц (1875 МГц, в режиме Boost)
Объем видеопамяти
6 ГБ
Тип видеопамяти
GDDR6
Частота видеопамяти
12000 МГц
Поддержка технологий
DirectX 12/OpenGL 4.5
Разъемы дополнительного питания
8 pin
Рекомендуемая производителем мощность БП
450 Вт
  	"""
],
[
	'Видеокарта MSI NVIDIA GeForce RTX 3090', # 2
  	152990,
  	"""
Видеочипсет
NVIDIA GeForce RTX 3090
Частота графического процессора
1725 МГц
Объем видеопамяти
24 ГБ
Тип видеопамяти
GDDR6X
Частота видеопамяти
19500 МГц
Поддержка режимов
NVLink
Поддержка технологий
DirectX 12 Ultimate/OpenGL 4.6
Разъемы дополнительного питания
8+8 pin
Рекомендуемая производителем мощность БП
750 Вт
  	"""
],
[
	'Видеокарта GIGABYTE nVidia GeForce GTX 1050TI', # 3
  	11690,
  	"""
Видеочипсет
nVidia GeForce GTX 1050TI
Частота графического процессора
1290 МГц (1430 МГц, в режиме Boost)
Объем видеопамяти
4 ГБ
Тип видеопамяти
GDDR5
Частота видеопамяти
7008 МГц
Поддержка технологий
DirectX 12/OpenGL 4.5
Разъемы дополнительного питания
без дополнительного питания
Рекомендуемая производителем мощность БП
300 Вт
  	"""
],
[
	'Видеокарта ASUS nVidia GeForce GTX 1650', # 4 
  	13790,
  	"""
Видеочипсет
nVidia GeForce GTX 1650
Частота графического процессора
1485 МГц (1755 МГц, в режиме Boost)
Объем видеопамяти
4 ГБ
Тип видеопамяти
GDDR5
Частота видеопамяти
8002 МГц
Поддержка технологий
DirectX 12/OpenGL 4.5
Разъемы дополнительного питания
без дополнительного питания
Рекомендуемая производителем мощность БП
300 Вт
  	"""
],
[
	'Видеокарта SAPPHIRE AMD Radeon RX 5500XT', # 5
  	17450,
  	"""
Видеочипсет
AMD Radeon RX 5500XT
Частота графического процессора
1737 МГц (1845 МГц, в режиме Boost)
Объем видеопамяти
4 ГБ
Тип видеопамяти
GDDR6
Частота видеопамяти
14000 МГц
Поддержка технологий
DirectX 12/OpenGL 4.6
Разъемы дополнительного питания
8 pin
Рекомендуемая производителем мощность БП
500 Вт

  	"""
],
    ]

    for video_card in video_card_list:
        sql = f'INSERT INTO video_card VALUES (?, ?, ?)'
        cursor.execute(sql, (
            video_card[0],
            video_card[1],
            video_card[2]
        ))
        conn.commit()

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


    motherboard_list = [
[
	'Материнская плата GIGABYTE B450M S2H', # 1
  	5100,
  	"""
Гнездо процессора
SocketAM4
Чипсет
AMD B450
Частотная спецификация памяти
2933 МГц
Слотов памяти DDR4
2
Форм-фактор
mATX
  	"""
],
[
	'Материнская плата GIGABYTE B450M DS3H', # 1
  	5750,
  	"""
SocketAM4
Чипсет
AMD B450
Поддержка SLI/CrossFire
CrossFire
Частотная спецификация памяти
2933 МГц
Слотов памяти DDR4
4
Форм-фактор
mATX
  	"""
],
[
	'Материнская плата ASUS TUF B450M-PRO GAMING', # 1
  	8060,
  	"""
SocketAM4
Чипсет
AMD B450
Поддержка SLI/CrossFire
CrossFire
Частотная спецификация памяти
2666 МГц
Слотов памяти DDR4
4
Форм-фактор
mATX
  	"""
],
[
	'Материнская плата ASUS ROG STRIX B450-E', # 1
  	13640,
  	"""
Гнездо процессора
SocketAM4
Чипсет
AMD B450
Поддержка SLI/CrossFire
CrossFire
Частотная спецификация памяти
2666 МГц
Слотов памяти DDR4
4
Форм-фактор
ATX
  	"""
],
[
	'Материнская плата MSI B450I GAMING PLUS AC', # 1
  	9370,
  	"""
Гнездо процессора
SocketAM4
Чипсет
AMD B450
Поддержка SLI/CrossFire
CrossFire
Частотная спецификация памяти
2666 МГц
Слотов памяти DDR4
4
Форм-фактор
ATX
  	"""
],
    ]

    for motherboard in motherboard_list:
        sql = f'INSERT INTO motherboard VALUES (?, ?, ?)'
        cursor.execute(sql, (
            motherboard[0],
            motherboard[1],
            motherboard[2]
        ))
        conn.commit()


    cooling_list = [
[  
	'DEEPCOOL GAMMAXX 300 FURY',
  	1290,
  	"""
Количество вентиляторов
1
Диаметр вентилятора
92 мм
Скорость вращения вентилятора
900 - 1800 об/мин
Максимальное тепловыделение процессора
130 Вт
Основание кулера
с открытыми тепловыми трубками, материал - алюминий
Использование тепловых трубок
с тепловыми трубками
Материал радиатора
алюминий+медь
Питание вентилятора от материнской платы
4-pin
Высота кулера
130.5 мм 
  	"""
],   
[
	'DEEPCOOL REDHAT',
  	1290,
  	"""
Количество вентиляторов
1
Диаметр вентилятора
92 мм
Скорость вращения вентилятора
900 - 1800 об/мин
Максимальное тепловыделение процессора
130 Вт
Основание кулера
с открытыми тепловыми трубками, материал - алюминий
Использование тепловых трубок
с тепловыми трубками
Материал радиатора
алюминий+медь
Питание вентилятора от материнской платы
4-pin
Высота кулера
130.5 мм 
  	"""
],
[
  'ZALMAN CNPS10X Optima II',
  	2420,
  	"""
1
Диаметр вентилятора
120 мм
Скорость вращения вентилятора
800 - 1500 об/мин
Максимальное тепловыделение процессора
180 Вт
Основание кулера
с открытыми тепловыми трубками, материал - алюминий/медь
Использование тепловых трубок
с тепловыми трубками
Материал радиатора
алюминий+медь
Питание вентилятора от материнской платы
4-pin
Высота кулера
160 мм
  	"""
],
[  
	'AEROCOOL Cylon 4',
  	2320,
  	"""
1
Диаметр вентилятора
120 мм
Скорость вращения вентилятора
800 - 1800 об/мин
Максимальное тепловыделение процессора
145 Вт
Основание кулера
с открытыми тепловыми трубками, материал - алюминий/медь
Использование тепловых трубок
с тепловыми трубками
Материал радиатора
алюминий+медь
Питание вентилятора от материнской платы
4-pin
Высота кулера
25 мм
  	"""
],
[  
	'DEEPCOOL Watercooler CASTLE 240 V2',
  	8030,
  	"""
Количество вентиляторов
2
Диаметр вентилятора
120 мм
Скорость вращения вентилятора
500 - 1800 об/мин
Максимальное тепловыделение процессора
250 Вт
Основание кулера
цельное
Материал радиатора
алюминий
Питание вентилятора от материнской платы
4-pin
  	"""
],   
    ]

    for cooling in cooling_list:
        sql = f'INSERT INTO cooling VALUES (?, ?, ?)'
        cursor.execute(sql, (
            cooling[0],
            cooling[1],
            cooling[2]
        ))
        conn.commit()


    ram_list = [
[
	'CORSAIR Vengeance LPX CMK16GX4M2B3200C16 DDR4', 
  	6690,
  	"""
Форм-фактор
DIMM
Количество контактов
288-pin
Латентность
CL16
Тип поставки
Ret
  	"""
],
[
	'CORSAIR Vengeance LPX CMK16GX4M2A2666C16 DDR4', 
  	6590,
  	"""
Форм-фактор
DIMM
Количество контактов
288-pin
Латентность
CL16
Тип поставки
Ret
  	"""
],
[
	'PATRIOT Viper Steel PVS416G320C6K DDR4', 
  	6190,
  	"""
Форм-фактор
DIMM
Количество контактов
288-pin
Латентность
CL16
Тип поставки
Ret
  	"""
],
[
	'KINGSTON HyperX FURY Black HX426C16FB3K2', 
  	6090,
  	"""
Форм-фактор
DIMM
Количество контактов
288-pin
Латентность
CL16
Тип поставки
Ret
  	"""
],
[
	'KINGSTON VALUERAM KVR26N19D8', 
  	5590,
  	"""
Форм-фактор
DIMM
Количество контактов
288-pin
Латентность
CL19
Тип поставки
Ret
  	"""
],]

    for ram in ram_list:
        sql = f'INSERT INTO ram VALUES (?, ?, ?)'
        cursor.execute(sql, (
            ram[0],
            ram[1],
            ram[2]
        ))
        conn.commit()


    ssd_list = [
[
	'SSD накопитель SAMSUNG 970 EVO Plus', # 1
  	31990,
  	"""
Форм-фактор
M.2 2280
Интерфейс
PCI-E x4
Максимальная скорость чтения
3500 МБ/с
Максимальная скорость записи
3300 МБ/с
Тип памяти NAND
V-NAND
Ресурс TBW
1200 ТБ
  	"""
],
[
	'SSD накопитель SAMSUNG 860 EVOSSD накопитель SAMSUNG 860 EVO', # 1
  	3990,
  	"""
Форм-фактор
2.5"
Интерфейс
SATA III
Максимальная скорость чтения
550 МБ/с
Максимальная скорость записи
520 МБ/с
Тип памяти NAND
3D TLC
Ресурс TBW
150 ТБ
Толщина
6.8 мм
  	"""
],
[
	'SSD накопитель KINGSTON UV500 SUV500M8/240G 240ГБ, M.2 2280, SATA III', # 1
  	3990,
  	"""
Форм-фактор
M.2 2280
Интерфейс
SATA III
Максимальная скорость чтения
520 МБ/с
Максимальная скорость записи
500 МБ/с
Тип памяти NAND
3D NAND TLC
Ресурс TBW
100 ТБ
  	"""
],
[
	'SSD накопитель KINGSTON A400-R KC-S44256-6F 256ГБ, 2.5", SATA III', # 1
  	2690,
  	"""
Форм-фактор
2.5"
Интерфейс
SATA III
Максимальная скорость чтения
500 МБ/с
Максимальная скорость записи
350 МБ/с
Тип памяти NAND
TLC
Ресурс TBW
80 ТБ
Толщина
7 мм
  	"""
],
[
	'SSD накопитель KINGSTON Fury 3D KC-S44240-6F 240ГБ, 2.5", SATA III', # 1
  	2690,
  	"""
Форм-фактор
2.5"
Интерфейс
SATA III
Максимальная скорость чтения
500 МБ/с
Максимальная скорость записи
500 МБ/с
Тип памяти NAND
3D TLC
Ресурс TBW
80 ТБ
Толщина
7 мм
  	"""
],
    ]

    for ssd in ssd_list:
        sql = f'INSERT INTO ssd VALUES (?, ?, ?)'
        cursor.execute(sql, (
            ssd[0],
            ssd[1],
            ssd[2]
        ))
        conn.commit()


    hdd_list = [
[
	'Жесткий диск WD Blue WD10EZRZ, 1ТБ, HDD, SATA III, 3.5', # 1
  	3390,
  	"""
Тип жесткого диска
HDD
Форм-фактор
3.5 "
Объем накопителя
1 ТБ
Интерфейс
SATA III
Буферная память
64 МБ
Скорость вращения шпинделя
5400 об/мин
  	"""
],
[
	'Жесткий диск WD Purple WD40PURZ, 4ТБ, HDD, SATA III, 3.5"', # 1
  	9990	,
  	"""
Тип жесткого диска
HDD
Форм-фактор
3.5 "
Объем накопителя
4 ТБ
Интерфейс
SATA III
Буферная память
64 МБ
Скорость вращения шпинделя
5400 об/мин
  	"""
],
[
	'Жесткий диск WD Purple WD60PURZ, 6ТБ, HDD, SATA III, 3.5"', # 1
  	15590,
  	"""
Тип жесткого диска
HDD
Форм-фактор
3.5 "
Объем накопителя
6 ТБ
Интерфейс
SATA III
Буферная память
64 МБ
Скорость вращения шпинделя
5400 об/мин
  	"""
],
[
	'Жесткий диск TOSHIBA X300 HDWE140EZSTA, 4ТБ, HDD, SATA III, 3.5"', # 1
  	8590,
  	"""
Тип жесткого диска
HDD
Форм-фактор
3.5 "
Объем накопителя
4 ТБ
Интерфейс
SATA III
Буферная память
128 МБ
Скорость вращения шпинделя
7200 об/мин
  	"""
],
[
	'Жесткий диск TOSHIBA X300 HDWE140EZSTA, 4ТБ, HDD, SATA III, 3.5"', # 1
  	8590,
  	"""
Тип жесткого диска
HDD
Форм-фактор
3.5 "
Объем накопителя
4 ТБ
Интерфейс
SATA III
Буферная память
128 МБ
Скорость вращения шпинделя
7200 об/мин
  	"""
],
[
	'Жесткий диск TOSHIBA P300 HDWD110UZSVA, 1ТБ, HDD, SATA III, 3.5"', # 1
  	3190,
  	"""
Тип жесткого диска
HDD
Форм-фактор
3.5 "
Объем накопителя
1 ТБ
Интерфейс
SATA III
Буферная память
64 МБ
Скорость вращения шпинделя
7200 об/мин
  	"""
],
    ]

    for hdd in hdd_list:
        sql = f'INSERT INTO hdd VALUES (?, ?, ?)'
        cursor.execute(sql, (
            hdd[0],
            hdd[1],
            hdd[2]
        ))
        conn.commit()

    housing_list = [
[
	'ATX ZALMAN N5 MF', 
  	3390,
  	"""
Тип жесткого диска
HDD
Форм-фактор
3.5 "
Объем накопителя
1 ТБ
Интерфейс
SATA III
Буферная память
64 МБ
Скорость вращения шпинделя
5400 об/мин
  	"""
],
[
	'ATX AEROCOOL Aero One Frost-G-BK-v1', 
  	3970,
  	"""
Midi-Tower
Отсеки 3,5" внутренние
2
Фронтальные разъемы USB 3.0
2
Мощность БП
не установлен
Материал корпуса
сталь/стекло
Толщина стенок корпуса
0.5 мм
Максимальная длина видеокарты
327 мм
  	"""
],
[
   	'ATX AEROCOOL Aero One Frost-G-WT-v1', 
  	3870,
  	"""
Типоразмер
Midi-Tower
Отсеки 3,5" внутренние
2
Фронтальные разъемы USB 3.0
2
Мощность БП
не установлен
Материал корпуса
сталь/стекло
Толщина стенок корпуса
0.5 мм
Максимальная длина видеокарты
327 мм
  	"""
],
[
	'ATX AEROCOOL Aero One Frost-G-BK-v1', 
  	3970,
  	"""
Midi-Tower
Отсеки 3,5" внутренние
2
Фронтальные разъемы USB 3.0
2
Мощность БП
не установлен
Материал корпуса
сталь/стекло
Толщина стенок корпуса
0.5 мм
Максимальная длина видеокарты
327 мм
  	"""
],
    ]

    for housing in housing_list:
        sql = f'INSERT INTO housing VALUES (?, ?, ?)'
        cursor.execute(sql, (
            housing[0],
            housing[1],
            housing[2]
        ))
        conn.commit()
    

    power_supply_list = [
[
	'Блок питания AEROCOOL AERO BRONZE, 650Вт, 120мм', # 1
  	4630 ,
  	"""
Форм-фактор
ATX
Мощность
650 Вт
Сертифицирован в стандарте
80 PLUS BRONZE
Цвет
черный
Питание материнской платы и процессора
24+4+4 pin
Питание видеокарты
2х(6+2) pin
Разъемы SATA
6 шт
Разъемы Peripheral (Molex)
4 шт
Размер вентилятора(ов)
120мм
  	"""
],
[
	'Блок питания THERMALTAKE Toughpower Grand RGB Sync, 850Вт, 140мм', # 1
  	11580,
  	"""
Форм-фактор
ATX
Мощность
850 Вт
Сертифицирован в стандарте
80 PLUS GOLD
Цвет
черный
Питание материнской платы и процессора
24+2x(4+4) pin
Питание видеокарты
6х(6+2) pin
Разъемы SATA
12 шт
Разъемы Peripheral (Molex)
4 шт
Размер вентилятора(ов)
140мм
  	"""
],
[
	'Блок питания GIGABYTE GP-P750GM, 750Вт, 120мм', # 1
  	8170,
  	"""
Форм-фактор
ATX
Мощность
750 Вт
Сертифицирован в стандарте
80 PLUS GOLD
Цвет
черный
Питание материнской платы и процессора
24+2x(4+4) pin
Питание видеокарты
4х(6+2) pin
Разъемы SATA
8 шт
Разъемы Peripheral (Molex)
3 шт
Размер вентилятора(ов)
120мм
  	"""
],
[
	'Блок питания COOLER MASTER MWE Bronze 700W V2, 700Вт, 120мм', # 1
  	6000,
  	"""
Форм-фактор
ATX
Мощность
700 Вт
Сертифицирован в стандарте
80 PLUS BRONZE
Цвет
черный
Питание материнской платы и процессора
24+4+4 pin
Питание видеокарты
4х(6+2) pin
Разъемы SATA
8 шт
Разъемы Peripheral (Molex)
4 шт
Размер вентилятора(ов)
120мм
  	"""
],
[
	'Блок питания AEROCOOL KCAS PLUS 700, 700Вт, 120мм', # 1
  	4110,
  	"""
Форм-фактор
ATX
Мощность
700 Вт
Сертифицирован в стандарте
80 PLUS BRONZE
Цвет
черный
Питание материнской платы и процессора
24+4+4 pin
Питание видеокарты
4х(6+2) pin
Разъемы SATA
7 шт
Разъемы Peripheral (Molex)
4 шт
Размер вентилятора(ов)
120мм
  	"""
],
    ]

    for power_supply in power_supply_list:
        sql = f'INSERT INTO power_supply VALUES (?, ?, ?)'
        cursor.execute(sql, (
            power_supply[0],
            power_supply[1],
            power_supply[2]
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

create_table()
update_table()
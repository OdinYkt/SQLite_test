# -*- coding: windows-1251 -*-
from random import randrange, randint
import datetime

names = ['Ivanov', 'Vasilev', 'Petrov', 'Smirnov', 'Mihajlov', 'Fedorov', 'Sokolov', 'Jakovlev', 'Popov', 'Andreev', 'Alekseev', 'Aleksandrov', 'Lebedev', 'Grigorev', 'Stepanov', 'Semenov', 'Pavlov', 'Bogdanov', 'Nikolaev', 'Dmitriev', 'Egorov', 'Volkov', 'Kuznetsov', 'Nikitin', 'Solovev', 'Timofeev', 'Orlov', 'Afanasev', 'Filippov', 'Sergeev', 'Zaharov', 'Matveev', 'Vinogradov', 'Kuzmin', 'Maksimov', 'Kozlov', 'Ilin', 'Gerasimov', 'Markov', 'Novikov', 'Morozov’', 'Romanov', 'Osipov', 'Makarov', 'Zajtsev', 'Beljaev', 'Gavrilov', 'Antonov', 'Efimov', 'Leontev', 'Davydov', 'Gusev', 'Danilov', 'Kiselev', 'Sorokin', 'Tihomirov', 'Krylov', 'Nikiforov', 'Kondratev', 'Kudrjavtsev', 'Borisov', 'Zhukov', 'Vorobev', 'Scherbakov', 'Poljakov', 'Savelev', 'Shmidt', 'Trofimov', 'Chistjakov', 'Baranov', 'Sidorov', 'Sobolev', 'Karpov', 'Belov', 'Miller', 'Titov', 'Lvov', 'Frolov', 'Ignatev', 'Komarov', 'Prokofev', 'Bykov', 'Abramov', 'Golubev', 'Ponomarev', 'Pokrovskij', 'Martynov', 'Kirillov', 'Shults', 'Mironov', 'Fomin', 'Vlasov', 'Troitskij', 'Fedotov', 'Nazarov', 'Ushakov', 'Denisov', 'Konstantinov', 'Voronin', 'Naumov']
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def auto_users(n, letter='auto'):
    users = ''
    if letter == 'auto':
        new_names = names
    else:
        new_names = []
        for name in names:
            if name[0] == letter.upper():
                new_names.append(name)

    for i in range(n):
        users += str((create_human(new_names))) + ',\n'

    return users[:-2]


def create_human(new_names):
    sex = ('female', 'male')[randrange(0, 2)]

    if sex == 'male':
        name = new_names[randrange(0, len(new_names))] + ' ' + abc[randrange(0, len(abc))] + '.' + abc[randrange(0, len(abc))] + '.'
    else:
        name = new_names[randrange(0, len(new_names))] + 'a ' + abc[randrange(0, len(abc))] + '.' + abc[randrange(0, len(abc))] + '.'

    date_birth = str(random_birthdate())

    return name, date_birth, sex


def random_birthdate(start_year=1943, end_year=2005):
    random_year = randint(start_year, end_year)
    random_month = randint(1, 12)
    random_day = randint(1, 31)

    # Обработка некорректных дат
    if random_day > 28 and random_month == 2:
        random_day = 28
    elif (random_month in [4, 6, 9, 11]) and random_day > 30:
        random_day = 30
    random_date = datetime.date(random_year, random_month, random_day)
    return random_date

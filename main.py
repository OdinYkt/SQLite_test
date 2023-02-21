import sys
from commands import *
from user_generation import *
import time
start = time.time()

def main():
    arg = int(sys.argv[1])

    if arg in [1, 2, 3, 4, 5]:      #проверка правильности аргумента
        connection = create_connection()
    else:
        print('Неверный параметр, посмотрите README')
        return

    if arg == 1:      #Создание таблицы
        execute_query(connection, create_users_table)
        print('Table created')
    elif arg == 2:    #Создание записи
        name = ' '.join([sys.argv[2], sys.argv[3]])
        date_birth = sys.argv[4]
        sex = sys.argv[5].lower()
        execute_queries(connection, create_user, (name, date_birth, sex))
        print('Table entry:'
              f'{name}, {date_birth}, {sex}'
              'created')
    elif arg == 3:    #Вывод всех строк + сортировка + новый столбец
        print_sql(execute_read_query(connection, select_all))
    elif arg == 4:    #Автоматическое заполнение
        for i in range(100):
            users = auto_users(10000-100)
            execute_query(connection, create_many_users(users))
        users = auto_users(100, 'F')
        execute_query(connection, create_many_users(users))
        print('Done')
    elif arg == 5:    #Выборка F + замер времени
        print_sql(execute_read_query(connection, filter_F))
        end = time.time() - start
        print(f'Time:{end}')

if __name__ == "__main__":
    main()

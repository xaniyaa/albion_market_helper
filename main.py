from xlsxwriter.exceptions import FileCreateError
import os
from loader import workbook
from excel_table import init_table, close_table, fill_table


if __name__ == "__main__":
    try:
        os.remove(f'{os.curdir}/price_table.xlsx')
        init_table()
        fill_table()
        close_table(workbook)
    except FileNotFoundError:
        init_table()
        fill_table()
        close_table(workbook)
    except PermissionError:
        print('Ошибка при пересоздании таблицы, закройте программы, использующие таблицу, и перезапустите программу')
    except FileCreateError:
        print('Не удалось создать файл')
    

    
from xlsxwriter.exceptions import FileCreateError
import os
from loader import workbook
from excel_table import init_table, close_table, fill_item_names

# with open('response.txt', 'r') as file:
#     json_data = loads(file.read())
#     for j in range(len(json_data)):
#         print(json_data[j].get("buy_price_min"), item_list1[json_data[j].get("item_id")], qualities[json_data[j].get("quality")], json_data[j].get('city'))

if __name__ == "__main__":
    try:
        os.remove(f'{os.curdir}/price_table.xlsx')
        init_table()
        fill_item_names()
        close_table(workbook)
    except FileNotFoundError:
        init_table()
        fill_item_names()
        close_table(workbook)
    except PermissionError:
        print('Ошибка при пересоздании таблицы, закройте программы, использующие таблицу, и перезапустите программу')
    except FileCreateError:
        print('Не удалось создать файл')
    

    
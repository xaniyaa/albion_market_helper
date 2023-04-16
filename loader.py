from xlsxwriter import Workbook


workbook = Workbook(f'price_table.xlsx')
worksheet = workbook.add_worksheet('Prices')


import gspread
from pprint import pprint
import pandas as pd

# more info about the library
# https://gspread.readthedocs.io/en/latest/index.html
# creates an access object to work with sheets
gc = gspread.service_account(filename='secret/python_service.json')

# creates a new spreadsheet
# sh = gc.create('A new spreadsheet')
# don't forget to share the access otherwise you won't see the file
# sh.share('otto@example.com', perm_type='user', role='writer')

# opens a file
sh = gc.open("ROI продавцов")
# opens a first sheet
worksheet = sh.get_worksheet(0)

#Getting All Values From a Worksheet as a List of Lists
#list_of_lists = worksheet.get_all_values()

#Getting All Values From a Worksheet as a List of Dictionaries
#list_of_dicts = worksheet.get_all_records()

# update a cell with the value
# worksheet.update('B1', 'Bingo!')

# update a cell with a formula
# worksheet.update_acell('c2', '=sum(E2:E13)')
# worksheet.update_cell(2, 4, '=sum(E2:E13)')

# formatting https://github.com/robin900/gspread-formatting

#pprint(sht1.sheet1.get('A:E'))

# loads sheet to dataframe
dataframe = pd.DataFrame(worksheet.get_all_records())
# advanced usage https://github.com/robin900/gspread-dataframe
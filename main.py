import pandas as pd
from google_sheets_class import GoogleSheets
from google_sheets_init import Create_Service

if __name__ == '__main__':
    service = Create_Service('secret/credentials_python.json', 'https://www.googleapis.com/auth/spreadsheets')
    my_sheet = GoogleSheets(service)
    values = my_sheet.get_values('19ckopCxamrv8g0sQQOtiHycRdwgTqS9h4-PC2IxxXCM')
    df = pd.DataFrame(values[1:], columns=values[0]) 
    # new_table = my_sheet.create('New Data')

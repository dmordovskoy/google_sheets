from google_sheets_init import Create_Service

# sourced from https://github.com/gsuitedevs/python-samples/blob/master/sheets/snippets/spreadsheet_snippets.py

class GoogleSheets(object):
    """Creates a Google Sheet Object to work with Google Sheets

    Arguments:
        object {object} -- Google Sheet API object with granted rights (1 hour)
    """
    def __init__(self, service):
        self.service = service

    def create(self, title):
        """Creates new Google Sheet with the given name

        Arguments:
            title {string} -- Title for the new spreadsheet

        Returns:
            [string] -- Returns Google sheet ID
        """
        service = self.service
        # [START sheets_create]
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                            fields='spreadsheetId').execute()
        #print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
        # [END sheets_create]
        return spreadsheet.get('spreadsheetId')
    
    def rename_sheet(self, spreadsheet_id, title):
        """Renames the Google sheet with the particular ID

        Arguments:
            spreadsheet_id {string} -- ID
            title {string} -- New Title
        """
        service = self.service
        requests = []
        # Change the spreadsheet's title.
        requests.append({
            'updateSpreadsheetProperties': {
                'properties': {
                    'title': title
                },
                'fields': 'title'
            }
        })
        body = {
            'requests': requests
        }
        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body).execute()

    def find_and_replace(self, spreadsheet_id, find, replacement):
        """Find and Replace values in the Google Sheet with the particular ID

        Arguments:
            spreadsheet_id {string} -- ID
            find {string} -- What to find (non case sensitive)
            replacement {string} -- Replacement values

        """
        service = self.service

        requests = []
        # Change the spreadsheet's title.
        # Find and replace text
        # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/request#findreplacerequest
        requests.append({
            'findReplace': {
                'find': find,
                'replacement': replacement,
                'allSheets': True
            }
        })
        # Add additional requests (operations) ...

        body = {
            'requests': requests
        }
        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body).execute()
        # find_replace_response = response.get('replies')[0].get('findReplace')
        # print('{0} replacements made.'.format(
        #     find_replace_response.get('occurrencesChanged')))
        # [END sheets_batch_update]
        # return response

    def get_values(self, spreadsheet_id, range_name):
        """Returns values from the Google Sheet with the given ID

        Arguments:
            spreadsheet_id {string} -- ID
            range_name {string} -- Range, i.e. 'A1:F4'

        Returns:
            [array] -- list of rows, 2 dimension array
        """
        service = self.service
        # [START sheets_get_values]
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        # print('{0} rows retrieved.'.format(len(rows)))
        # [END sheets_get_values]
        return rows
    
    def append_values(self, spreadsheet_id, range_name,
                      _values,
                      value_input_option='USER_ENTERED'):
        """Appends values to the Google Sheet with the given ID. 
        Appends startingto from the nearest empty row after the tabla in the range

        Arguments:
            spreadsheet_id {string} -- ID
            range_name {string} -- Range, i.e. 'A1:F4'
            _values {array} -- [[cell value1, cell value2],[row2],etc.]

        Keyword Arguments:
            value_input_option {str} -- how to evaluate input data, RAW or by default (default: {'USER_ENTERED'})

        """
        service = self.service
        # values format
        values = [
            [
                # Cell values ...
            ],
            # Additional rows ...
        ]
        # [START_EXCLUDE silent]
        values = _values
        # [END_EXCLUDE]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        # print('{0} cells appended.'.format(result \
        #                                        .get('updates') \
        #                                        .get('updatedCells')))
        # # [END sheets_append_values]
        # return result

service = Create_Service('credentials_python.json', 'https://www.googleapis.com/auth/spreadsheets')

my_sheet = GoogleSheets(service)
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

SPREADSHEETS_KEY = '1lXj_D2lETF4SATbXL4LOTuLiQ0Y3oWl5mJ9UznBJ3-g'

# Find a workbook by name and open the first sheet
sheet = client.open_by_key(SPREADSHEETS_KEY).sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
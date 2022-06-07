from flask import Flask, render_template, request, redirect, url_for
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

SPREADSHEETS_KEY = '1lXj_D2lETF4SATbXL4LOTuLiQ0Y3oWl5mJ9UznBJ3-g'

# Find a workbook by name and open the first sheet
sheet = client.open_by_key(SPREADSHEETS_KEY)

@app.route('/')
def index():
    # Extract and print all of the values
    sheet_name = 'test'
    sheet_data = sheet.worksheet(sheet_name).get_all_values()
    return render_template('index.html', sheet_data=sheet_data)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add', methods=['post'])
def add_post():
    title=request.form['title']
    URL=request.form['URL']
    description=request.form['description']
    yossy = [title, URL, description]
    ws = sheet.worksheet('test')
    ws.append_row(yossy)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
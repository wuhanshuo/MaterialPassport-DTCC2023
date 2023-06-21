"""
# For DT4C^2 FS2023 by CEA@ETH.
@Author: Database Group of DT4C^2.
"""

from flask import Flask, render_template, request, send_file
import codecs
import csv

app = Flask(__name__)


def findRecord(file,db,ID):
    data =  {'db':'000','ID': '404', 'projectName': 'Not Found'}   # not found page defination
    with codecs.open(file) as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            if row['ID'] == ID:
                data = row
                data['db']= db  # for downloading
                break
    return data

@app.route('/')
def index():
    get_id = request.args.get('id')
    db = request.args.get('db')
    if not (get_id and db):
        data = {'db':'000','ID': '', 'projectName': 'Database Group', 'magic':'Congratulations, Sherlock! You have stumbled upon a mysterious hidden page.'}
    elif not (get_id.isdecimal() and get_id.isdecimal()):
        data = {'db':'000','ID': '404', 'projectName': 'Not Found'}
    else:
        try:
            file = '/home/dtcc2023/mysite/static/database/{0}/{0}.csv'.format(db)
            data = findRecord(file,db,get_id)
        except:  # if the database path does not exist:
            data = {'db':'000','ID': '404', 'projectName': 'Not Found'}
    return render_template("index.html", data=data)

@app.route('/database')
#Download the file with URL: dtcc2023.pythonanywhere.com/database
def download():
    db = request.args.get('db')
    return send_file('/home/dtcc2023/mysite/static/database/{0}/{0}.csv'.format(db),
                     as_attachment=True,
                     attachment_filename='database_{0}.csv'.format(db))


#app.run(debug=True, use_reloader=False)

from flask import Flask
from flask import jsonify
from flask import render_template
app = Flask(__name__)
import csv 
  
csvFilePath = r'overclockers.csv'

@app.route('/')
def helloWorld():
    msg = ""
    return render_template('index.html', msg=msg)

@app.route('/rjson')
def serveFile():
    data = {} 
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            print(rows[0])
            key = rows['id']
            data[key] = rows
    return jsonify(data)



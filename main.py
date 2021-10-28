#!/usr/bin/python3
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#mport forms
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'Abc1234*'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)
"""
mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="12345678",
)"""

@app.route('/')
def index():
    return render_template('singin.html')

@app.route('/singin', methods=['POST'] )
def singin():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)' , (fullname, phone, email))
        mysql.connection.commit()
    return 'recivido' #render_template('singin.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
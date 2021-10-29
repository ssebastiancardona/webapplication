#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#credential for Db connection
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'Abc1234*'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('singin.html', contacts = data)

@app.route('/singin', methods=['POST'] )
def singin():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)' , (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added successfully')
    return redirect(url_for('index')) #render_template('singin.html')

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
          UPDATE contacts
          SET fullname = %s,
          email = %s,
          phone = %s
          WHERE id = %s
        """, (fullname, email, phone, id))
        mysql.connection.commit()
        flash('Contact Update Successfully')
        return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(_name_)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ims_db'

mysql = MySQL(app)


# API to get stock information
@app.route('/get_stock', methods=['GET'])
def get_stock():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stock_list")
    stock_records = cur.fetchall()
    cur.close()
    return jsonify({"stock": stock_records})


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8000, debug=True)

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(_name_)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ims_db'

mysql = MySQL(app)


# API to add sale return
@app.route('/add_sale_return', methods=['POST'])
def add_sale_return():
    data = request.json
    cur = mysql.connection.cursor()

    for return_item in data:
        cur.execute(
            "INSERT INTO return_list (Barcode, customer_Name, item_Name, quantity, cost, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (return_item["Barcode"], return_item["customer_name"], return_item["item_name"], return_item["quantity"],
             return_item["cost"], 1))  # Setting status=1 for sale return

    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "success", "message": "Sale return added successfully."})


# API to add purchase return
@app.route('/add_purchase_return', methods=['POST'])
def add_purchase_return():
    data = request.json
    cur = mysql.connection.cursor()

    for return_item in data:
        cur.execute(
            "INSERT INTO return_list (Barcode, supplier_Name, item_Name, quantity, cost, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (return_item["Barcode"], return_item["supplier_name"], return_item["item_name"], return_item["quantity"],
             return_item["cost"], 2))  # Setting status=2 for purchase return

    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "success", "message": "Purchase return added successfully."})


# API to get all sale return records
@app.route('/get_sale_returns', methods=['GET'])
def get_sale_returns():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM return_list WHERE status = 1")
    returns_records = cur.fetchall()
    cur.close()
    return jsonify({"sale_returns_records": returns_records})


# API to get all purchase return records
@app.route('/get_purchase_returns', methods=['GET'])
def get_purchase_returns():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM return_list WHERE status = 2")
    returns_records = cur.fetchall()
    cur.close()
    return jsonify({"purchase_returns_records": returns_records})


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8000, debug=True)

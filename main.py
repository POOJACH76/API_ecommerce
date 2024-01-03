from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ims_db'

mysql = MySQL(app)


# API to add sale for different items in different rows
@app.route('/add_sale', methods=['POST'])
def add_sale():
    data = request.json
    cur = mysql.connection.cursor()
    for sale_item in data:
        cur.execute(
            'INSERT INTO sale_list(Barcode, Customer_Name, Item_Name, Quantity, cost, total) VALUES (%s, %s, %s, %s, %s, %s)',
            (sale_item["Barcode"], sale_item["Customer_Name"], sale_item["Item_Name"], sale_item["Quantity"],
             sale_item["cost"], sale_item["total"]))
    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "success", "message": "Sales added successfully."})


# API to get all sales records
@app.route('/sale_list', methods=['GET'])
def get_sales():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sale_list")
    sales_records = cur.fetchall()
    cur.close()
    return jsonify({"sales_records": sales_records})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

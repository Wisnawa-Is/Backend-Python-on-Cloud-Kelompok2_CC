import mysql.connector
from flask import Flask, request, jsonify

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='kelompok2',
    auth_plugin='mysql_native_password'
)
conn.autocommit = True
app = Flask(__name__)

@app.route('/')
def home():
    return(f'Selamat Datang di Website Kelompok 2')

@app.route('/anggota', methods=['GET'])
def ambil_barang():
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM anggota_kelompok')
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
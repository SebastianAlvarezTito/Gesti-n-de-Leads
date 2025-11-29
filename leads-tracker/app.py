from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'clave_secreta_temporal'

# Configuración de la base de datos MySQL
DB_CONFIG = {
    'host': 'prueba.cbmycpr1lzst.us-east-1.rds.amazonaws.com',
    'user': 'admin',  # Asumiendo usuario por defecto
    'password': 'asdQWE123',
    'database': 'leads_db'
}

def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        interest = request.form['interest']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO leads (name, email, phone, interest) VALUES (%s, %s, %s, %s)',
            (name, email, phone, interest)
        )
        
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('¡Lead registrado exitosamente!', 'success')
        
    except mysql.connector.IntegrityError:
        flash('Error: El correo electrónico ya existe en la base de datos.', 'error')
    except Exception as e:
        flash(f'Error al registrar lead: {str(e)}', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
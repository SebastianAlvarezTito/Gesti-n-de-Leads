import os

class Config:
    # Configuración de la base de datos MySQL
    DB_HOST = 'prueba.cbmycpr1lzst.us-east-1.rds.amazonaws.com'
    DB_NAME = 'leads_db'
    DB_USER = 'admin'
    DB_PASS = 'asdQWE123'
    
    # Clave secreta para Flask (en producción usar variables de entorno)
    SECRET_KEY = 'clave_secreta_temporal_para_desarrollo'
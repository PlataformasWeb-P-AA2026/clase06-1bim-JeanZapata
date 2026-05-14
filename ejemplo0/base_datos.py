"""
    Crear la base de datos de Python en la misma carpeta que el script
"""
import sqlite3
import os

ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(ruta_carpeta, 'base_ejemplo.db')

conn = sqlite3.connect(ruta_db)
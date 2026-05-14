import csv
import os
from base_datos import conn

def importar():
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Autor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            cedula TEXT, 
            edad INTEGER
        )
    """)

    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(directorio_actual, 'data', 'info.csv')

    print(f"Buscando archivo en: {ruta_csv}")

    if not os.path.exists(ruta_csv):
        print(f"ERROR: No se encontró info.csv en la carpeta 'data'.")
        return

    try:
        with open(ruta_csv, encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            
            for fila in reader:
                cursor.execute("""
                    INSERT INTO Autor (nombre, apellido, cedula, edad) 
                    VALUES (?, ?, ?, ?)
                """, (fila['nombre'], fila['apellido'], fila['cedula'], int(fila['edad'])))
        
        conn.commit()
        print("¡Datos importados con éxito!")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        conn.rollback()
    finally:
        cursor.close()

    print("\n--- Contenido en la Base de Datos ---")
    cursor_ver = conn.cursor()
    cursor_ver.execute("SELECT * FROM Autor")
    for r in cursor_ver.fetchall():
        print(r)
    cursor_ver.close()

if __name__ == "__main__":

    importar()












import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar docentes
# session.query me obtiene todo lo de la clase saludo
# saludos -> lista de objetos 
saludos = session.query(Saludo).all()

# Mostrar con Streamlit
st.title("Presentación de todos los Saludos")

for saludo  in saludos:
    cadena = f"{saludo.mensaje.upper()} {saludo.tipo.upper()}"
    st.write(cadena)
    st.markdown("---")

st.markdown("---")
st.title("Presentación de todos los Saludos en Tabla")
lista = []

for s in saludos:
    diccionario = {"id": s.id, "mensaje": s.mensaje, "tipo": s.tipo}
    lista.append(diccionario)

st.dataframe(lista)

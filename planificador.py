import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth

# --- CONFIGURACIÓN DE FIREBASE ---
# REEMPLAZA ESTOS DATOS CON LOS DE TU CONSOLA DE FIREBASE
firebaseConfig = {
    "apiKey": "AIzaSyA3vLkE2v4LnqJA084ICmkyOfQhuoFuJA",
    "authDomain": "apa-sistema-educativo.firebaseapp.com",
    "projectId": "apa-sistema-educativo",
    "storageBucket": "apa-sistema-educativo.firebasestorage.app",
    "messagingSenderId": "774126994405",
    "appId": "1:774126994405:web:be8ad590cbb9439eb7a50c",
    "databaseURL": "https://apa-sistema-educativo-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth_fire = firebase.auth()
db = firebase.database()

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(layout="wide", page_title="Arquitectura Pedagógica Avanzada")

def centrar_logo():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo_apa.png", width=200)

# --- LÓGICA DE SESIÓN ---
if 'logueado' not in st.session_state:
    st.session_state['logueado'] = False

if not st.session_state['logueado']:
    centrar_logo()
    st.title("Arquitectura Pedagógica Avanzada (APA)")
    tab_login, tab_recuperar = st.tabs(["Iniciar sesión", "Recuperar contraseña"])
    
    with tab_login:
        email = st.text_input("Correo electrónico")
        password = st.text_input("Contraseña", type="password")
        if st.button("Iniciar sesión"):
            try:
                user = auth_fire.sign_in_with_email_and_password(email, password)
                st.session_state['logueado'] = True
                st.session_state['user_info'] = user
                st.rerun()
            except:
                st.error("Correo o contraseña incorrectos.")

    with tab_recuperar:
        email_recuperar = st.text_input("Ingresa tu correo para recuperar")
        if st.button("Enviar correo"):
            auth_fire.send_password_reset_email(email_recuperar)
            st.success("Correo enviado.")
else:
    # --- MOTOR DE PLANIFICACIÓN (CONTENIDO PRIVADO) ---
    st.title("Motor de Planificación")
    correo_actual = st.session_state['user_info']['email']
    st.write(f"Bienvenido, **{correo_actual}**")
    
    # ... (Aquí va todo tu código de formularios de planificación existente) ...

    if st.sidebar.button("Cerrar sesión"):
        st.session_state['logueado'] = False
        st.rerun()

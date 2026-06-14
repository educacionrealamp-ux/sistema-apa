import streamlit as st
from firebase_config import auth
from db import db

# Configuración de página
st.set_page_config(layout="wide", page_title="Arquitectura Pedagógica Avanzada")

def centrar_logo():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo_apa.png", width=200)

# --- Lógica de Autenticación ---
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
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state['logueado'] = True
                st.session_state['user_info'] = user # Guardamos toda la info del usuario
                st.rerun()
            except:
                st.error("Correo o contraseña incorrectos.")
                
    with tab_recuperar:
        email_recuperar = st.text_input("Ingresa tu correo para recibir instrucciones")
        if st.button("Enviar correo de cambio de contraseña"):
            try:
                auth.send_password_reset_email(email_recuperar)
                st.success("¡Correo enviado! Revisa tu bandeja de entrada.")
            except:
                st.error("No se pudo enviar el correo.")

else:
    # --- MOTOR DE PLANIFICACIÓN ---
    centrar_logo()
    st.title("Motor de Planificación")
    
    # Obtener correo del usuario logueado
    correo_actual = st.session_state['user_info']['email']
    st.write(f"Bienvenido, **{correo_actual}**")
    
    # 1. TEMPORIZACIÓN
    st.header("1. Temporización")
    coll1, coll2 = st.columns(2)
    with coll1: f_i = st.date_input("Fecha Inicio:")
    with coll2: f_f = st.date_input("Fecha Fin:")

    # 2. IDENTIFICACIÓN Y DESTREZAS
    st.header("2. Identificación Administrativa y Destrezas")
    subnivel = st.selectbox("Subnivel:", ["Preparatoria", "Elemental", "Básica Media", "Básica Superior", "Bachillerato"])
    cursos_map = {
        "Preparatoria": ["Primero"],
        "Elemental": ["Segundo", "Tercero", "Quinto"],
        "Básica Media": ["Quinto", "Sexto", "Séptimo"],
        "Básica Superior": ["Octavo", "Noveno", "Décimo"],
        "Bachillerato": ["1ero BGU", "2do BGU", "3ero BGU"]
    }
    curso = st.selectbox("Curso:", cursos_map[subnivel])

    # 3. METODOLOGÍA E INTEGRACIÓN ENEIS
    st.header("3. Metodología e Integración ENEIS")
    metodologia = st.selectbox("Metodología:", ["ERCA", "ABP", "Clase Invertida", "ACC"])
    trabaja_eneis = st.radio("¿Va a trabajar con contenidos ENEIS?", ["NO", "SI"])

    # 4. FORMATO
    st.header("4. Formato de Presentación")
    formato_uso = st.radio("Formato:", ["Formato Institucional", "Estándar APA"])

    # GUARDADO AUTOMÁTICO CON CORREO
    if st.button("Generar Planificación APA"):
        datos = {
            "correo_docente": correo_actual,
            "fecha_inicio": str(f_i),
            "fecha_fin": str(f_f),
            "subnivel": subnivel,
            "curso": curso,
            "metodologia": metodologia,
            "trabaja_eneis": trabaja_eneis,
            "formato": formato_uso
        }
        try:
            db.child("planificaciones").push(datos)
            st.success(f"¡Planificación guardada con éxito por {correo_actual}!")
        except Exception as e:
            st.error(f"Error al guardar: {e}")

    if st.sidebar.button("Cerrar sesión"):
        st.session_state['logueado'] = False
        st.session_state['user_info'] = None
        st.rerun()
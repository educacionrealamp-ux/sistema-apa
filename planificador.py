import streamlit as st
import pyrebase

# --- Configuración de Firebase ---
firebaseConfig = {
    "apiKey": "AlzaSyA3vlKzE2v4LnqJAO84ICmkyOfQhuoFuJA",
    "authDomain": "sistema-apa.firebaseapp.com",
    "databaseURL": "https://sistema-apa-default-rtdb.firebaseio.com", # <--- ESTO ES LO QUE FALTABA
    "projectId": "sistema-apa",
    "storageBucket": "sistema-apa.appspot.com",
    "messagingSenderId": "910237730940",
    "appId": "1:910237730940:web:86e492211624c65360f73c"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# --- Lógica de Sesión ---
if 'user' not in st.session_state:
    st.session_state['user'] = None

# --- Interfaz de Autenticación ---
if st.session_state['user'] is None:
    st.title("Iniciar sesión")
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state['user'] = email
            st.rerun()
        except Exception as e:
            st.error(f"Error técnico: {e}")
else:
    # --- Interfaz del Motor (APA) ---
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.update({'user': None}))
    
    st.title("🚀 APA: Arquitectura Pedagógica Avanzada")
    st.subheader("Motor de Planificación - Unidad Educativa San Miguel de los Bancos")
    st.write(f"Bienvenido, {st.session_state['user']}")

    # --- Formulario de Entrada ---
    with st.form("form_planificacion"):
        col1, col2 = st.columns(2)
        
        with col1:
            dcd = st.text_input("Ingresa la DCD (ej. M.4.1.28)")
            curso = st.selectbox("Curso", ["8vo EGB", "9no EGB", "10mo EGB"])
            tema = st.text_input("Tema de la clase")
            
        with col2:
            incluir_eneis = st.checkbox("¿Incluir inserción ENEIS en esta planificación?")
            dim_eneis = None
            tema_eneis = None
            
            if incluir_eneis:
                st.info("Configuración de Inserción")
                dim_eneis = st.text_input("Dimensión de la inserción")
                tema_eneis = st.text_input("Tema de la inserción")

        submit_button = st.form_submit_button("Generar Planificación")

    # --- Lógica de Procesamiento ---
    if submit_button:
        if not dcd or not tema:
            st.error("Por favor, completa al menos la DCD y el tema.")
        else:
            st.success(f"Generando planificación para: {tema}")
            st.write("### Vista Previa de la Planificación")
            st.write(f"**DCD:** {dcd}")
            if incluir_eneis:
                st.warning(f"📌 **Inserción ENEIS:** {dim_eneis} - {tema_eneis}")
            st.markdown("---")
            st.write("*(El motor APA está listo para procesar la metodología ACC/DUA aquí)*")

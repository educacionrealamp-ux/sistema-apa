import streamlit as st

st.set_page_config(page_title="APA - Motor de Planificación", layout="wide")

st.title("🚀 APA: Arquitectura Pedagógica Avanzada")
st.subheader("Motor de Planificación - Unidad Educativa San Miguel de los Bancos")

# --- Formulario de Entrada ---
with st.form("form_planificacion"):
    col1, col2 = st.columns(2)
    
    with col1:
        dcd = st.text_input("Ingresa la DCD (ej. M.4.1.28)")
        curso = st.selectbox("Curso", ["8vo EGB", "9no EGB", "10mo EGB"])
        tema = st.text_input("Tema de la clase")
        
    with col2:
        # Checkbox para la flexibilidad del ENEIS
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
        
        # Aquí es donde el motor APA procesará el formato
        st.write("### Vista Previa de la Planificación")
        st.write(f"**DCD:** {dcd}")
        
        if incluir_eneis:
            st.warning(f"📌 **Inserción ENEIS:** {dim_eneis} - {tema_eneis}")
        
        st.markdown("---")
        st.write("*(Aquí se integrará la lógica del formato que analizamos anteriormente)*")

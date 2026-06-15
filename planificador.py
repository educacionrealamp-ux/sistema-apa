import streamlit as st
import pyrebase
# (Configuración de Firebase se mantiene igual que antes)

def generar_planificacion_html(datos):
    # Esta función crea la estructura del documento con formato profesional
    html = f"""
    <h1>Planificación Pedagógica APA</h1>
    <p><b>Docente:</b> {datos['docente']}</p>
    <p><b>DCD:</b> {datos['dcd']}</p>
    <h2>1. Inserciones Obligatorias</h2>
    <ul>
        <li>Educación Cívica, Ética e Integridad</li>
        <li>Educación para el Desarrollo Sostenible</li>
        <li>Educación Socioemocional</li>
        <li>Educación Financiera</li>
        <li>Educación para la Seguridad Vial</li>
    </ul>
    """
    if datos['incluir_eneis']:
        html += f"<h2>2. Inserción Específica (ENEIS/ITS)</h2><p>{datos['detalle_eneis']}</p>"
    
    html += "<h2>3. Secuencia Didáctica (ERCA + DUA)</h2>"
    # Aquí irá el prompt que generará el contenido pedagógico
    return html

# Interfaz de Streamlit
st.title("🚀 APA: Arquitectura Pedagógica Avanzada")
docente = st.text_input("Nombre del Docente")
dcd = st.text_input("Ingresa la DCD (ej. M.4.1.28)")
incluir_eneis = st.checkbox("¿Incluir inserción ENEIS/ITS?")
detalle_eneis = ""
if incluir_eneis:
    detalle_eneis = st.text_area("Detalle de la Inserción ENEIS/ITS")

if st.button("Generar Planificación"):
    datos = {'docente': docente, 'dcd': dcd, 'incluir_eneis': incluir_eneis, 'detalle_eneis': detalle_eneis}
    contenido = generar_planificacion_html(datos)
    
    # Aquí llamarías a la herramienta de creación de documentos
    st.success("¡Planificación generada con éxito!")
    st.markdown(contenido, unsafe_allow_html=True)

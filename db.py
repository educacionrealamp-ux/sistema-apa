from firebase_config import firebase

# Conexión a la base de datos de Firebase
db = firebase.database()

# Tu "cerebro" pedagógico existente
def obtener_base_conocimiento():
    # Esta base de datos será el "cerebro" de APA
    return {
        "DCD.LL.4.1.1": {
            "descripcion": "Indagar sobre las variaciones lingüísticas...",
            "objetivo_area": "OG.LL.1. Desempeñarse como usuarios competentes...",
            "objetivo_general": "Analizar la diversidad lingüística...",
            "indicador": "I.LL.4.1.1. Explica la variación lingüística...",
            "estrategias_dua": {
                "tecnologico": ["Videos interactivos", "Grabación de podcast sobre variantes"],
                "analogo": ["Entrevistas presenciales", "Mapa físico de dialectos"]
            }
        },
        # Aquí irán todas tus DCDs siguiendo este formato
    }
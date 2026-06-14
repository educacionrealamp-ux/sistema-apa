import pyrebase

# Configuración de Firebase
config = {
    "apiKey": "AIzaSyA3vlKzE2v4LnqJA084ICmkyOfQhuoFuJA",
    "authDomain": "apa-sistema-educativo.firebaseapp.com",
    "databaseURL": "https://apa-sistema-educativo.firebaseio.com",
    "projectId": "apa-sistema-educativo",
    "storageBucket": "apa-sistema-educativo.appspot.com",
    "messagingSenderId": "774126994405",
    "appId": "1:774126994405:web:be8ad590cbb9439eb7a50c",
    "measurementId": "G-98L9HZSRY7"
}

# Inicializar la app y la autenticación
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate('firebase.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

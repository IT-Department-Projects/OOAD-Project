import pyrebase

config = {
	"apiKey"            : "AIzaSyC-Qcib030qwMmi5j12tQ2Qf-zjXgJyLck",
	"authDomain"        : "hospitalmanagementsystem-edfd9.firebaseapp.com",
	"databaseURL"       : "https://worapp-8bba7.firebaseio.com",
	"storageBucket"     : "https://hospitalmanagementsystem-edfd9.firebaseio.com",
	"messagingSenderId" : "814886885492",
	"serviceAccount"    : "HospitalManagementSystem-3826ac933f8b.json"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# To-Do authenticate a user
#User = auth.sign_in_with_email_and_password("william@hackbrightacademy.com", "mySuperStrongPassword")

db = firebase.database()

# test = db.child('test').get(user['idToken']).val()

# db.child('test').update({'value': False});

# print(test)
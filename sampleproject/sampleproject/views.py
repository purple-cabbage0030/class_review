
from django.shortcuts import render
import pyrebase
 
config={
    "apiKey": "AIzaSyA1EgxUYqmYdjrU0WYWPgZOGReMHmA8EXs",
    "authDomain": "test-0915-71b01.firebaseapp.com",
    "databaseURL": "https://test-0915-71b01-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "test-0915-71b01",
    "storageBucket": "test-0915-71b01.appspot.com",
    "messagingSenderId": "289505718091",
    "appId": "1:289505718091:web:00037fa76e7f927359c2ce"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 
def home(request):
    day = database.child('Data').child('Day').get().val()
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('Projectname').get().val()
    return render(request,"Home.html", {"day":day,"id":id,"projectname":projectname })
from django.shortcuts import render
from imaplib import _Authenticator
from django.http import HttpResponse
import pyrebase

config = {
    "apiKey": "AIzaSyBX0XRViev80IcoabEVfTaDttuVjz2ywkw",
    "authDomain": "my-app-e19da.firebaseapp.com",
    "projectId": "my-app-e19da",
    "storageBucket": "my-app-e19da.appspot.com",
    "messagingSenderId": "1014631219188",
    "appId": "1:1014631219188:web:ab0161de5e43c292d8c3a1",
    "databaseURL": "https://my-app-e19da-default-rtdb.firebaseio.com",
    "measurementId": "G-TCFY2GZ9K8",
}

# Create your views here.; everything in database is stored in 'firebase' variable
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()


# Create your views here.
def index(request):
    person_age = database.child("testdata").child("age").get().val()
    person_major = database.child("testdata").child("major").get().val()
    person_name = database.child("testdata").child("name").get().val()

    return render(
        request,
        "index.html",
        {
            "person_age": person_age,
            "person_major": person_major,
            "person_name": person_name,
        },
    )


def home(request):
    return HttpResponse("PlanIt")

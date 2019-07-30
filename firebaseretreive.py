from firebase import firebase



firebase = firebase.FirebaseApplication("https://pythondbtest-d9f06.firebaseio.com/", None)
result = firebase.get('/pythondbtest-d9f06/Customer', '')
print(result)

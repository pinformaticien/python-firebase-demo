from firebase import firebase

firebase = firebase.FirebaseApplication("https://pythondbtest-d9f06.firebaseio.com/", None)
firebase.put('/pythondbtest-d9f06/Customer/-Ll38yBumpNivMq-Gfn9', 'Name', 'Bouba')
print("Record Updated")

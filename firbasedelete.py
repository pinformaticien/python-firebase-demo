from firebase import firebase

firebase = firebase.FirebaseApplication("https://pythondbtest-d9f06.firebaseio.com/", None)
firebase.delete('/pythondbtest-d9f06/Customer/', '-Ll38yBumpNivMq-Gfn9')
print("Record Deleted")

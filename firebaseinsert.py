from firebase import firebase



firebase = firebase.FirebaseApplication("https://pythondbtest-d9f06.firebaseio.com/", None)
data = {
    'Name':'John Doe',
    'Email':'jandoe@gmail.com',
    'Phone':708029034
}

result = firebase.post('/pythondbtest-d9f06/Customer', data)
print(result)

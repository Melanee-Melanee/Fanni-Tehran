

def writeHospital():
    sno = input('Enter serial number:')
    name = input('Enter patient name:')
    age = input('Enter patient age')             
    sex = input('enter patient sex')
    heigth = input('enter patient heigth:')             
    weight = input('enter weight')
    bgroup = input( 'enter blood group')
    fname = input("enter father name")
    address = input('enter address')
    city = input('enter city')
    state = input('enter state')
    pno = input('enter phone number:')
    email = input('enter email')
    doctor = input('enter doctor name')
    dname = input('enter disease name')
    med = input('enter prescribed medicine')
    bill = input('enter bill amount: Rs.')
                 
                 
    record = {
       'serial_number':sno,
       'name': name,
       'age': age,
       'sex' : sex,
       'heigth' : heigth,
       'weigth': weight,
       'bgroup' : bgroup,
       'fname': fname, 
       'address': address,
       'city': city,
       'state': state,
       'pno' : pno,
       'email': email,
       'doctor': doctor,
       'dname': dname,
       'med': med,
       'bill': bill,
   } 
                 
    return record
# from Hospitalproject import allrecords
from allrecords import writeHospital

def show_menu():
    all_patient = list()
    print('simple hospital management system \n\n')
    print('1. SHOW ALL RECORDS')
    print('2. SEARCH BY SERIAL NUMBER')
    print('3. WRITE RECORD')
    print('4. SEARCH BY BLOOD GROUP')
    print('5. SEARCH BY CONTACT NUMBER')
    print('6. SEARCH BY AGE')
    print('7. SEARCH BY SEX')
    print('8. SEARCH BY DISEASE NAME')
    print('9. SEARCH BY DOCTOR NAME ')
    print('10. SEARCH BT PAYMENT METHOD')
    print('11. SEARCH BY EMAIL')
    print('12. MODIFY RECORD')
    print('13. DELETE RECORD ')
    print('14. EXIT ')
    ch=eval(input('PLEASE INTER YOUR CHOICE:'))
    if ch==1:
        rec = writeHospital()
        all_patient.append(rec)
       
    if ch==14:
            exit()
    
          
show_menu()       
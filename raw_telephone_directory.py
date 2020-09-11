name_contact = {}
name_address = {}
name_email = {}

def AddContact():
    print('---------------------------')
    print('         ADD CONTACT       ')
    print('---------------------------')
    name = input("Enter the Name : ")
    contact_no = int(input('Contact number : '))
    address = input("Enter the Address : ")
    email = input('Enter the Email : ')
    
    if name not in name_contact:
        name_contact[name] = contact_no
        name_address[name] = address
        name_email[name] = email
    else:
        print('Contact Allredy Available')
        
def ShowContact():
    name = input('Enter the name : ')
    if name in name_contact:
        print('---------------------------')
        print('       CONTACT INFO        ')
        print('---------------------------')
        info = ''' Name : {} \n Contact : {} \n Address : {} \n Email : {}'''.format(name,name_contact[name],name_address[name],name_email[name])
        print(info)
    else:
        print('Contact name not Found : ')
    print('---------------------------')
    
def DeleteContact():
    name = input('Enter the name : ')
    if name in name_contact:
        print('---------------------------')
        print('       DELETE CONTACT      ')
        print('---------------------------')
        del name_contact[name]
        del name_address[name]
        del name_email[name]
    else:
        print('Contact Not Found') 
    print('Contact Deleted Successfully...!')   
    
def UpdateContact():
    name = input('Enter the name : ')
    if name in name_contact:
        name_contact[name] = int(input('Enter the Updated Contact : '))
        name_address[name] = input('Enter the updated Address : ')
        name_email[name] = input('Enter the updated Email : ')
    else:
        print('Contact not found for update..!')
        
def MaketextFile():
    file_to_save = open('Contact.txt','a+')
    for name , contact in name_contact.items():
        file_to_save.write('''\nName : {}\nContact : {}\nAddress : {}\nEmail : {}\n'''.format(name,contact,name_address[name],name_email[name]))

def PrintAllDetails():
    print('-------------')
    print('ALL CONTACT')
    print('-------------')
    for name , contact in name_contact.items():
        print('''\nName : {}\nContact : {}\nAddress : {}\nEmail : {}\n'''.format(name,contact,name_address[name],name_email[name]))
    
      
choise = ''
while choise != 'n':
    print('-------------------------------')
    print('         MAIN MENU             ')
    print('-------------------------------')
    print('1.Add Contact')
    print('2.Show Contact')
    print('3.Updates Contact')
    print('4.Delete Contact')
    print('5.Stire in text File')
    print('6.View All Details')
    opt = int(input('Enter your choise : '))
    if opt == 1:
        AddContact()
    elif opt == 2:
        ShowContact()
    elif opt == 3:
        UpdateContact()
    elif opt == 4:
        DeleteContact()
    elif opt == 5:
        MaketextFile()
    elif opt == 6:
        PrintAllDetails()
    else:
        print('Enter Valid choise')    
    choise = input('Do you Want to go For Main Menu (y/n) :')
        
        

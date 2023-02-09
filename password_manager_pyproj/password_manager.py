'''
Password Manager
What does the code do?
1. When the user enters "2", he/she can enter the password, to store in encrypted format.
2. When the user enters "1", he/she can view the stored password.
'''

print("\n")
print('********************************************')
print("      Welcome to the Password Manager       ")
print('********************************************')

from cryptography.fernet import Fernet

master_pwd = input("Enter The Master Password: ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file: # wb stands for write in bytes, & creates key.key file
        key_file.write(key) # write key in the file that was generated called fernet

write_key()

def view():
    with open('passwords.txt' , 'r') as f: # r stands for read only mode, reads passwords.txt file
        for line in f.readlines():
            print(line.rstrip()) # removes the spaces,newline from the end of things written in the file

def add():
    acc_name = input('\nAccount Name: ')
    id = input("          ID: ")
    pwd = input("    Password: ")

    with open('passwords.txt' , 'a') as f: # a stands for adding to existing file / creating a new file if not available, creates&adds pass to passwords.txt file
        f.write("Account Name: " + acc_name + "\n" + "ID: " + id + "\n" + "Password: " + pwd + "\n" + "\n")

while True:

    print('\n" You Are Now Inside the Password Manager "\n')
    mode = input("1. To View the Password (press:1) \n"
                 "2. To Add a New Password (press:2) \n"
                 "3. To Quit Password manager (press:3) \n"
                 "\nKindly Enter your Choice is: ")

    if mode == '3':
        print("\nHave a Nice Day!")
        print("** Goodbye **\n")
        break
    if mode == '2':
        add()
    elif mode == '1':
        view()
    else:
        print("Invalid Selection")
def create_acc():
    name = input("Enter username: ")
    password = input("Enter password: ")
    if len(password) < 6:
        print('Password too short.')
        exit()
    password_repeat = input("Repeat the password: ")
    if password == password_repeat:
        with open('password.csv', "w") as f:
            f.write(name + "\n")
            f.write(password)
    else:
        print('Passwords dont match')
try:
    with open('password.csv', "r") as f:
        lines = f.readlines()
        password = lines[1]
        user = lines[0]
        
except FileNotFoundError:
    create_acc()
password_ask = input(f'Enter password for {user}: '.replace('\n', ''))
if password == password_ask:
    print('Acsess Granted!')
else:
    print('Acsess Denied!')
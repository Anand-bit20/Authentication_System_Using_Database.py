import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="anand")
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS registration (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), contact VARCHAR(15), address VARCHAR(255))")
    conn.commit()

def reg(): # Function Created For Registration
    print("Registration Page".center(90))
    print("*"*100)
    # Validating Name
    while True:
        name = input("ENTER NAME: ")
        if name.isalpha():
            print("You've entered a valid name:", name)
            print()
            break
        else:
            print("Invalid input. Only alphabets are allowed.")

    # Validating Email Address
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.'
    valid_domains = ['com', 'in', 'ac', 'org', 'edu']

    while True:
        print("Note: Entered email address should contain alphabets, numbers, @ symbol, and valid domain names like .com, .in, .ac, .org, and .edu")
        print("-"*130)
        email = input("Enter an email address: ")
        valid_email = True
        for c in email:
            if c not in valid_chars:
                valid_email = False
                break

        if valid_email:
            parts = email.split('@')
            if len(parts) == 2 and parts[1].split('.')[-1] in valid_domains:
                print("You've entered a valid email address:", email)
                print()
                break
            else:
                print("Invalid input. Please enter a valid email address containing alphabets, numbers, @ symbol, and valid domain names like .com, .in, .ac, .org, and .edu")
        else:
            print("Invalid input. Please enter a valid email address containing alphabets, numbers, @ symbol, and valid domain names like .com, .in, .ac, .org, and .edu")

    # Validating Password
    while True:
        print("Note: Entered password should contain at least one uppercase letter, one lowercase letter, one special character, and one digit.")
        print("-"*130)
        password = input("Enter a password: ")
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_special = any(c in '!@#$%^&*()-_+=' for c in password)
        has_digit = any(c.isdigit() for c in password)

        if has_upper and has_lower and has_special and has_digit:
            print("You've entered a valid password:", password)
            print()
            break
        else:
            print("Invalid password. Please enter a password containing at least one uppercase letter, one lowercase letter, one special character, and one digit.")

    # Validating Contact number
    while True:
        print("NOTE: Entered contact number should contain only 10-digits.")
        print("-"*130)
        contact = input("ENTER CONTACT NUMBER: ")
        valid_contact = True

        for c in contact:
            if c not in '0123456789':
                valid_contact = False
                break

        if valid_contact and len(contact) == 10:
            print("You've entered a valid contact number:", contact)
            print()
            break
        else:
            print("Invalid input. Please enter a valid 10-digit contact number containing only digits.")

    # Validating Address
    while True:
        print("NOTE: Please enter an address containing at least one uppercase letter, one lowercase letter, one special character, and one digit.")
        print("-"*130)
        address = input("ENTER ADDRESS: ")
        has_upper = any(c.isupper() for c in address)
        has_lower = any(c.islower() for c in address)
        has_special = any(c in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '/'] for c in address)
        has_digit = any(c.isdigit() for c in address)

        if has_upper and has_lower and has_special and has_digit:
            print("You entered a valid address:", address)
            print()
            break
        else:
            print("Invalid Address. Please enter an address containing at least one uppercase letter, one lowercase letter, one special character, and one digit.")

    cur.execute("INSERT INTO registration (name, email, password, contact, address) VALUES (%s, %s, %s, %s, %s)", (name, email, password, contact, address))
    conn.commit()

    print("Registration Successful!!\n")
    main()


def login():
    email = input("Enter Your Email: ")
    password = input("Enter your Password: ")

    cur.execute("SELECT * FROM registration WHERE email=%s AND password=%s", (email, password))
    user = cur.fetchone()

    if user:
        print("Login success")
        print("Your email id is:", user[2])
        print("Your password is:", user[3])
    else:
        print("Invalid credentials")

    main()


def main(): # Main Function

    print("AUTHENTICATION SYSTEM".center(93))
    print("*"*100)
    print("1. Registration".center(90))
    print("2. Login".center(90))
    print("3. Exit".center(90))
    n = int(input('Enter your Choice: '))
    if n == 1:
        reg()
    elif n == 2:
        login() 
    elif n == 3:
        print("Exit")
    else:
        print("Invalid choice. Please enter a valid option.")
        main()


if __name__ == "__main__":
    create_table()
    main()

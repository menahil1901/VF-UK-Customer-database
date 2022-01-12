import re
import sqlite3


# Defining Functions ***************************

def connect():
    return sqlite3.connect("customer.db")

# Query the db which returns all records


def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    print("TITLE " + "\t\tFIRST NAME" + "\t\tSECOND NAME" + "\t\tEMAIL" + "\t\t\t\t\tDOB" + "\t\t\t\t\tADDRESS" + \
          "\t\t\t\t\tCONTRACT TYPE" + "\tMarketing Comms?")
    for item in items:
        print(item[1] + "\t\t\t" + item[2] + "\t\t\t" + item[3] + "\t\t\t" + item[4] + "\t\t\t" + item[5] + "\t\t" +\
              item[6] + "\t" + item[7] + "\t\t" + item[7] + "\t\t\t" + item[8])

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Add a new record to the table


def add_one(title, first_name, last_name, email, date_of_birth, home_address, contract_type, marketing_comms):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?,?,?,?,?,?)",\
              (title, first_name, last_name, email, date_of_birth, home_address, contract_type, marketing_comms))
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?,?,?,?,?,?)", (list))
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


# Delete a record


def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", [id])
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their email


def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their title


def title_lookup(title):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (title,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their first name


def first_lookup(first_name):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (first_name,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their last name


def last_lookup(last_name):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (last_name,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their Address


def address_lookup(home_address):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (home_address,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their date of birth


def dob_lookup(date_of_birth):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (date_of_birth,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their contract type


def con_lookup(contract_type):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (contract_type,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Query user via their marketing communications choice


def comms_lookup(marketing_comms):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (marketing_comms,))
    items = c.fetchall()
    for item in items:
        print(items)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# Defining Function END ********************


def print_menu():  # Your menu design here
    print(30 * "-", "Vodafone UK Customer DataBase", 30 * "-")
    print("1. Show All Records 1")
    print("2. Add a Record  2")
    print("3. Delete 3")
    print("4. Exit")
    print(67 * "-")


loop = True

while loop:  # While loop which will keep going until loop = False
    print_menu()  # Displays menu
    name = input("Enter your username in letters only to gain access") # Validation
    pattern = "[a-zA-Z]" # Letters only
    if re.search(pattern, name):
        print("Valid username") # Argument for validation
    else:
        print("Invalid username, you cannot have access to the Vodafone Customer Database")
        break
    password = input("Enter your password - Hint! Num")
    pattern = "[0-9]"
    if re.search(pattern, password):
        print("Valid password")
    else:
        print("Invalid password")
        break
    choice = input("Enter your choice [1-4]: ")

    if choice == "1":
        print("You have chosen to show all records of the Vodafone UK Customers")
        show_all()

    elif choice == "2":
        print("You have chosen to add a new VF customer")
        title = input("Enter title: ")
        pattern = "[a-zA-Z]"
        if re.search(pattern, title):
            print("Valid title")
        else:
            print("Invalid username, you cannot have access to the Vodafone Customer Database")
            break
        first_name = input("Enter first name: ")
        pattern = "[a-zA-Z]"
        if re.search(pattern, first_name):
            print("Valid first name")
        else:
            print("Invalid username, you cannot have access to the Vodafone Customer Database")
            break
        last_name = input("Enter second name: ")
        pattern = "[a-zA-Z]"
        if re.search(pattern, last_name):
            print("Valid last name")
        else:
            print("Invalid username, you cannot have access to the Vodafone Customer Database")
            break
        email = input("Enter email: ")
        pattern = "[a-zA-Z]"
        if re.search(pattern, email):
            print("Valid email")
        else:
            print("invalid username, you cannot have access to the Vodafone Customer Database")
            break
        date_of_birth = input("Enter Date Of Birth: ")
        pattern = "[0-9]+ [a-zA-Z]"
        if re.search(pattern, date_of_birth):
            print("Valid D.O.B")
        else:
            print("Invalid username, you cannot have access to the Vodafone Customer Database")
            break
        home_address = input("Enter address: ")
        pattern = "[0-9]+ [a-zA-Z]"
        if re.search(pattern, home_address):
            print("Valid home address")
        else:
            print("Invalid username, you cannot have access to the Vodafone Customer Database")
            break
        contract_type = input("Enter customer's contract type with Vodafone: ")
        pattern = "[a-zA-Z]"
        if re.search(pattern, contract_type):
            print("Valid contract type")
        else:
            print("Invalid username, you cannot have access to the Vodafone Customer Database")
            break
        marketing_comms = input("Does the customer wish to opt into marketing communications?")
        pattern = "[a-zA-Z]"
        if re.search(pattern, marketing_comms):
            print("Valid marketing communications given")
        else:
            print("Invalid username, you cannot have access to the Vodafone Customer Database")
            break

        add_one(title, first_name, last_name, email, date_of_birth, home_address, contract_type, marketing_comms)

    elif choice == "3":
        id = int(input("Enter the row id you would like to delete"))
        delete_one(id)

    elif choice == "4":
        print("Thank you for using the Vodafone Customer Database")
        break

    else:
        print("You have selected the wrong option, please select a valid option to continue")

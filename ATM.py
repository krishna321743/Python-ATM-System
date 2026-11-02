import math

data = {
    1234: {
        "name": "x",
        "balance": 10000000.00,
        "password": "1234",
        "aadhaar": "00000000000",
        "mobile number": "00000000000"
    },
    4567: {
        "name": "y",
        "balance": 9900000.00,
        "password": "4321",
        "aadhaar": "00000000000",
        "mobile number": "00000000000"
    },
    7980: {
        "name": "z",
        "balance": 8500000.00,
        "password": "1243",
        "aadhaar": "00000000000",
        "mobile number": "00000000000"
    }
}


# Function to verify PIN and password
def authenticate(pin_no, password):
    user_data = data.get(pin_no)

    if user_data and user_data["password"] == password:
        return user_data

    return None


# Function to display account information
def check_information(user):
    print("\n====== ACCOUNT INFORMATION ======")
    print("NAME =", user["name"])
    print("BALANCE =", f"₹{user['balance']:.2f}")
    print("AADHAAR =", "*" * 8 + user["aadhaar"][-4:])
    print("MOBILE NUMBER =", "*" * 6 + user["mobile number"][-4:])
    print("PASSWORD = HIDDEN")


try:
    user_pin = int(input("ENTER YOUR PIN: "))
    password = input("ENTER PASSWORD: ")

    result = authenticate(user_pin, password)

    if result is None:
        print("INVALID PIN OR PASSWORD")

    else:
        print("\nWELCOME", result["name"].upper())

        while True:
            print("\n====== ATM MENU ======")
            print("1. CHECK BALANCE")
            print("2. DEPOSIT MONEY")
            print("3. WITHDRAW MONEY")
            print("4. CHECK INFORMATION")
            print("5. EXIT")

            try:
                choice = int(input("ENTER YOUR CHOICE: "))

                if choice == 1:
                    print("YOUR BALANCE =", f"₹{result['balance']:.2f}")

                elif choice == 2:
                    amount = float(input("ENTER DEPOSIT AMOUNT: "))

                    if math.isfinite(amount) and amount > 0:
                        result["balance"] += amount
                        print("DEPOSIT SUCCESSFUL")
                        print("UPDATED BALANCE =",
                              f"₹{result['balance']:.2f}")
                    else:
                        print("INVALID AMOUNT")

                elif choice == 3:
                    amount = float(input("ENTER WITHDRAWAL AMOUNT: "))

                    if not math.isfinite(amount) or amount <= 0:
                        print("INVALID AMOUNT")

                    elif amount > result["balance"]:
                        print("INSUFFICIENT BALANCE")

                    else:
                        result["balance"] -= amount
                        print("WITHDRAWAL SUCCESSFUL")
                        print("WITHDRAWN AMOUNT =", f"₹{amount:.2f}")
                        print("REMAINING BALANCE =",
                              f"₹{result['balance']:.2f}")

                elif choice == 4:
                    check_information(result)

                elif choice == 5:
                    print("THANK YOU FOR VISITING!")
                    break

                else:
                    print("INVALID CHOICE! SELECT 1 TO 5.")

            except ValueError:
                print("PLEASE ENTER A VALID NUMBER.")

except ValueError:
    print("PIN MUST BE A VALID NUMBER.")

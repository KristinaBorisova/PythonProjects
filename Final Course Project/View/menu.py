def menu():
    print("----User Menu----")
    print("[1] Show list of Doctors")
    print("[2] Show list of Patients")
    print("[3] Show list of Visitors")
    print("[4] Show average waiting time")
    print("[5] Add new doctor/patient/visitor")
    print("[0] Exit Menu")
    print("----------------")

option = int(input("Please enter your option:"))

while option != 0:
    if option == 1:
            # Do This
        print("You have chosen option 1")
        pass
    elif option == 2:
            # Do this
        print("You have chosen option 2")
        pass
    else:
        print("Invalid Optoin. Please try again!")
        print()
        menu()
        option = int(input("Enter your option:"))

print("Action completed. Thank you for using this program!")

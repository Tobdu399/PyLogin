import time
import os
import pickle
import data

validSignIn = data.user_is_signed_in

validSignIn = False

username = ""
password = ""

with open("savefile.dat", "rb") as f:
    correct_username, correct_password = pickle.load(f)


def clear():
    os.system("clear")

# -----------------------------------------

try:
    def loading():
        loadingDuration = 0

        while loadingDuration < 3:
            mainCopy()
            print("|")
            time.sleep(0.1)

            mainCopy()
            print("/")
            time.sleep(0.1)

            mainCopy()
            print("-")
            time.sleep(0.1)

            mainCopy()
            print("\ ")
            time.sleep(0.1)

            mainCopy()
            print("|")
            time.sleep(0.1)

            mainCopy()
            print("/")
            time.sleep(0.1)

            mainCopy()
            print("-")
            time.sleep(0.1)

            mainCopy()
            print("\ ")
            time.sleep(0.1)
            loadingDuration += 1

            if loadingDuration == 2:
                main2()
                break


    def main():
        global username
        global password

        clear()

        print("******************* LOGIN ********************")
        username = input("Username: ")
        print("----------------------------------------------")
        password = input("Password: ")
        print("----------------------------------------------")

        loading()


    def mainCopy():
        global username
        global password

        clear()

        print("******************* LOGIN ********************")
        print("Username: " + username)
        print("----------------------------------------------")
        print("Password: " + password)
        print("----------------------------------------------")


    def main2():
        global validSignIn

        global username
        global password

        global correct_username
        global correct_password

        mainCopy()

        if username == correct_username:
            # Check password
            if password == correct_password:
                print("✓ Authentication Successfull: Access granted!")

                time.sleep(2)
                clear()

                validSignIn = 202101
                userMain()
                exit()

            else:
                print("✕ Authentication Failed: Invalid username or password!")
                time.sleep(3)
                main()

        else:
            print("✕ Authentication Failed: Invalid username or password!")
            time.sleep(4)
            main()


    # -----------------------------------------------------

    def title():
        global username

        print("----------------------------------------------")
        print("Current user: " + username)
        print("----------------------------------------------")


    def userMain():
        global validSignIn

        if validSignIn == 202101:
            userMain2()


    def userMain2():
        global username
        global password
        global correct_username
        global correct_password

        clear()
        title()
        print()

        print("1 = Installed OS information")
        print("2 = Open file explorer with root privilieges (Authentication Required!)")
        print("3 = Change username")
        print("4 = Change password")
        print()
        print("5 = Exit")
        print()

        user_decision = input("> ")

        if user_decision == "1":
            clear()
            os.system("neofetch")
            print()
            input("Press Enter to continue... ")
            userMain2()

        elif user_decision == "2":
            clear()
            os.system("sudo nautilus")
            print()
            input("Press Enter to continue... ")
            userMain2()

        elif user_decision == "3":
            clear()
            title()
            print()

            print("To change your current username you need to verify yourself first!")
            print()
            password_verify = input("Password: ")
            print("----------------------------------------------")
            time.sleep(1)

            if password_verify == correct_password:
                clear()
                title()
                print()

                new_name = input("Type your new username: ")
                print()
                print("----------------------------------------------")
                print("Your new username will be: " + new_name)
                print()
                print("Type 'CONFIRM' to continue")
                print()
                confirm_name_change = input("> ")
                print("----------------------------------------------")
                time.sleep(1)

                if confirm_name_change == "CONFIRM":
                    correct_username = new_name

                    with open("savefile.dat", "wb") as f:
                        pickle.dump([correct_username, correct_password], f, protocol=2)

                    print("Done! You need to login again to apply changes")
                    print()
                    input("Press Enter to continue... ")
                    clear()
                    exit()

                else:
                    print("Aborting...")
                    time.sleep(2)
                    userMain2()

            else:
                print("Wrong password!")
                time.sleep(2)
                userMain2()

        elif user_decision == "4":
            clear()
            title()
            print()

            print("To change your current password you need to verify yourself first!")
            print()
            password_verify = input("Password: ")
            print("----------------------------------------------")
            time.sleep(1)

            if password_verify == correct_password:
                clear()
                title()
                print()

                new_password = input("Type your new password: ")
                print()
                print("----------------------------------------------")
                print("Your new password will be: " + new_password)
                print()
                print("Type 'CONFIRM' to continue")
                print()
                confirm_password_change = input("> ")
                print("----------------------------------------------")
                time.sleep(1)

                if confirm_password_change == "CONFIRM":
                    correct_password = new_password

                    with open("savefile.dat", "wb") as f:
                        pickle.dump([correct_username, correct_password], f, protocol=2)

                    print("Done! You need to login again to apply changes")
                    print()
                    input("Press Enter to continue... ")
                    clear()
                    exit()

                else:
                    print("Aborting...")
                    time.sleep(2)
                    userMain2()

            else:
                print("Wrong password!")
                time.sleep(2)
                userMain2()

        elif user_decision == "5":
            clear()
            exit()

        else:
            print()
            print("Make sure you type your decision correctly!")
            time.sleep(3)
            userMain2()


    # -----------------------------------------------------
    main()  # <--- This program starts from here! ----------------------------

except (KeyboardInterrupt, SystemExit):
    def shutdown_animation():
        clear()
        print("Shutting down: Please wait...")
        print("|##-----------------------------------|")
        time.sleep(0.2)

        clear()
        print("Shutting down: Please wait...")
        print("|###----------------------------------|")
        time.sleep(0.1)

        clear()
        print("Shutting down: Please wait...")
        print("|#######------------------------------|")
        time.sleep(0.2)

        clear()
        print("Shutting down: Please wait...")
        print("|#################--------------------|")
        time.sleep(0.8)

        clear()
        print("Shutting down: Please wait...")
        print("|###################################--|")
        time.sleep(0.4)

        clear()
        print("Shutting down: Please wait...")
        print("|#####################################|")
        print()
        time.sleep(1)
        print("Shutdown Complete!")
        time.sleep(1.5)
        clear()
        exit()

    shutdown_animation()

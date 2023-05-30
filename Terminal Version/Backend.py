import sys
import os
from datetime import datetime

currentYear = datetime.now().year


def view_past_Inbody_results(user_id):
    with open(user_id + ".txt", 'r') as file:
        read_file = file.read()
        file.close()
    print(read_file)
    main_menu_after_login(user_id)


def new_Inbody_test(user_id, gender):
    print(f"""Hello {user_id}, Would you like to use your (P) previously entered information or enter (N) new information? (P/N)
    E.G. Age, Height and Weight""")
    new_inbody_test_choice = input()
    if new_inbody_test_choice.upper() == 'P':
        with open(user_id + ".txt", 'r') as file:
            previous_results = file.read()
            file.close()
        print(previous_results)
        main_menu_after_login(user_id)

    elif new_inbody_test_choice.upper() == 'N':
        age = currentYear - float(input("Please enter your birth year: "))
        height = float(input("Please enter your height in cm: "))
        weight = float(input("Please enter your weight in kg: "))

        if gender == '1':
            user_gender = 1
        elif gender == '0':
            user_gender = 0
        if user_gender == 1:
            TBW = 2.447 - (0.09156 * age) + (0.1074 * height) + (0.3362 * weight)
            water_percentage = round((TBW / weight) * 100, 1)
            muscle_mass = round((0.32810 * weight) + (0.33929 * height) - 29.5336, 1)
            BMR = round((10 * weight) + (6.25 * height) - (5 * age) + 5)

            BMI = round(weight / pow(height / 100, 2), 1)

            if 0 < age <= 15:
                fat_Percentage = round((1.51 * BMI) - (0.70 * age) - (3.6 * int(user_gender)) + 1.4, 1)
            else:
                fat_Percentage = round((1.20 * BMI) + (0.23 * age) - (10.8 * int(user_gender)) - 5.4, 1)

            VFI = round(fat_Percentage - 10)

            str(BMI)
            str(VFI)

            print("BMI: ")
            print(BMI)
            print("Fat Precentage: ")
            print(fat_Percentage)
            print("VFI: ")
            print(VFI)
            print("TBW: ")
            print(TBW)
            print("Water Precentage: ")
            print(water_percentage)
            print("Muscle Mass: ")
            print(muscle_mass)
            print("BMR: ")
            print(BMR)

            bmi_result = str(BMI)
            fat_Percentage = str(fat_Percentage)
            vfi_result = str(VFI)
            tbw_result = str(TBW)
            muscle_mass_result = str(muscle_mass)
            water_percentage_result = str(water_percentage)
            bmr_result = str(BMR)

            with open(user_id + ".txt", 'w') as file:
                file.truncate(0)
                file.write("BMI: ")
                file.write("\n")
                file.write(bmi_result)
                file.write("\n")
                file.write("Fat Precentage: ")
                file.write("\n")
                file.write(fat_Percentage)
                file.write("\n")
                file.write("VFI: ")
                file.write("\n")
                file.write(vfi_result)
                file.write("\n")
                file.write("TBW: ")
                file.write("\n")
                file.write(tbw_result)
                file.write("\n")
                file.write("Water Precentage: ")
                file.write("\n")
                file.write(water_percentage_result)
                file.write("\n")
                file.write("Muscle Mass: ")
                file.write("\n")
                file.write(muscle_mass_result)
                file.write("\n")
                file.write("BMR: ")
                file.write("\n")
                file.write(bmr_result)
                file.close()
            main_menu_after_login(user_id)

        elif user_gender == 0:
            TBW = -2.097 + (0.1069 * height) + (0.2466 * weight)
            water_percentage = round((TBW / weight) * 100, 1)
            muscle_mass = round((0.29569 * weight) + (0.41813 * height) - 43.2933, 1)
            BMR = round((10 * weight) + (6.25 * height) - (5 * age) - 161)

            BMI = round(weight / pow(height / 100, 2), 1)

            if 0 < age <= 15:
                fat_Percentage = round((1.51 * BMI) - (0.70 * age) - (3.6 * int(user_gender)) + 1.4, 1)
            else:
                fat_Percentage = round((1.20 * BMI) + (0.23 * age) - (10.8 * int(user_gender)) - 5.4, 1)

            VFI = round(fat_Percentage - 10)

            str(BMI)
            str(VFI)

            print("BMI: ")
            print(BMI)
            print("Fat Precentage: ")
            print(fat_Percentage)
            print("VFI: ")
            print(VFI)
            print("TBW: ")
            print(TBW)
            print("Water Precentage: ")
            print(water_percentage)
            print("Muscle Mass: ")
            print(muscle_mass)
            print("BMR: ")
            print(BMR)

            bmi_result = str(BMI)
            fat_Percentage = str(fat_Percentage)
            vfi_result = str(VFI)
            tbw_result = str(TBW)
            muscle_mass_result = str(muscle_mass)
            water_percentage_result = str(water_percentage)
            bmr_result = str(BMR)

            with open(user_id + ".txt", 'w') as file:
                file.truncate(0)
                file.write("BMI: ")
                file.write("\n")
                file.write(bmi_result)
                file.write("\n")
                file.write("Fat Precentage: ")
                file.write("\n")
                file.write(fat_Percentage)
                file.write("\n")
                file.write("VFI: ")
                file.write("\n")
                file.write(vfi_result)
                file.write("\n")
                file.write("TBW: ")
                file.write("\n")
                file.write(tbw_result)
                file.write("\n")
                file.write("Water Precentage: ")
                file.write("\n")
                file.write(water_percentage_result)
                file.write("\n")
                file.write("Muscle Mass: ")
                file.write("\n")
                file.write(muscle_mass_result)
                file.write("\n")
                file.write("BMR: ")
                file.write("\n")
                file.write(bmr_result)
                file.close()
            main_menu_after_login(user_id)
    else:
        print("Invalid input.")
        main_menu_after_login(user_id)


def delete_account(user_id):
    delete_account_pending = True
    while delete_account_pending:
        print("Are you sure you want to delete your account? (Yes/No)")
        delete_account_choice = input()
        if delete_account_choice.lower() == 'yes':
            os.remove(user_id + ".txt")
            os.remove(user_id + "_gender.txt")
            print("Your account has been deleted.")
            main_menu()
        elif delete_account_choice.lower() == 'no':
            main_menu_after_login(user_id)
        else:
            print("Invalid input.")


def main_menu_after_login(user_id):
    main_menu_choice = input("""
1. New InBody Test 
2. View past InBody Results 
3. Logout 
4. Delete account """)
    if main_menu_choice == '1':
        with open(user_id + "_gender.txt", 'r') as file:
            gender = file.read()
            file.close()
        print(gender)
        new_Inbody_test(user_id, gender)
    elif main_menu_choice == '2':
        view_past_Inbody_results(user_id)
    elif main_menu_choice == "3":
        main_menu()
    elif main_menu_choice == '4':
        delete_account(user_id)


def main_menu():
    global user_id_input_create
    print("*Note: This is not your username, but a unique ID that you will use to access your account.")
    print("If you do not have an ID, please create one by returning '0'.")
    user_id = input("Input your user ID: ")
    if user_id == '0':
        user_create_pending = True
        while user_create_pending:
            print("Input your desired user ID: ")
            user_id_input_create = input()
            if os.path.exists(user_id_input_create + ".txt"):
                print("That user ID already exists. Please try again.")
                main_menu()
            else:
                user_create_pending = False

        gender_create_pending = True
        while gender_create_pending:
            gender_user_create = input("Please select your gender (M/F): ")
            if gender_user_create.upper() == "M":
                with open(user_id_input_create + ".txt", 'w') as file:
                    print("")
                    file.close()
                with open(user_id_input_create + "_gender.txt", 'w') as file:
                    file.write("1")
                    file.close()
                gender_create_pending = False
            elif gender_user_create.upper() == "F":
                with open(user_id_input_create + ".txt", 'w') as file:
                    print("")
                    file.close()
                with open(user_id_input_create + "_gender.txt", 'w') as file:
                    file.write("0")
                    file.close()
                gender_create_pending = False
            else:
                print("Invalid choice. Please try again.")
        print("Please return to the main menu and log in with your new user ID.")
        print("1.Main Menu")
        print("2.Exit")
        main_menu_choice = input()
        if main_menu_choice == '1':
            main_menu()
        elif main_menu_choice == '2':
            sys.exit()
    else:
        path = user_id + '.txt'
        if os.path.exists(path):
            main_menu_after_login(user_id)
        else:
            print("That user ID does not exist. Please try again.")
            main_menu()


main_menu()

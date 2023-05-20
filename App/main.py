import os
import tkinter.messagebox as tkmb
from tkinter import *
from PIL import Image
from PIL import ImageTk
import customtkinter as ctk
import tkinter as tk
from tkinter import *
from datetime import datetime
currentYear = datetime.now().year

def arduca_backend():
        user_age = currentYear - age

        if gender == 'M':
            user_gender = 1
        elif gender == 'F':
            user_gender = 0
        if user_gender == 1:
            TBW = 2.447 - (0.09156 * user_age) + (0.1074 * height) + (0.3362 * weight)
            water_percentage = round((TBW / weight) * 100, 1)
            muscle_mass = round((0.32810 * weight) + (0.33929 * height) - 29.5336, 1)
            BMR = round((10 * weight) + (6.25 * height) - (5 * user_age) + 5)

            BMI = round(weight / pow(height / 100, 2), 1)

            if 0 < user_age <= 15:
                fat_Percentage = round((1.51 * BMI) - (0.70 * user_age) - (3.6 * int(user_gender)) + 1.4, 1)
            else:
                fat_Percentage = round((1.20 * BMI) + (0.23 * user_age) - (10.8 * int(user_gender)) - 5.4, 1)

            VFI = round(fat_Percentage - 10)

            str(BMI)
            str(VFI)

            bmi_result = str(BMI)
            fat_Percentage = str(fat_Percentage)
            vfi_result = str(VFI)
            tbw_result = str(TBW)
            muscle_mass_result = str(muscle_mass)
            water_percentage_result = str(water_percentage)
            bmr_result = str(BMR)

            with open(user_name + "_results.txt", 'w') as file:
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
                #results()

        elif user_gender == 0:

            TBW = -2.097 + (0.1069 * height) + (0.2466 * weight)
            water_percentage = round((TBW / weight) * 100, 1)
            muscle_mass = round((0.29569 * weight) + (0.41813 * height) - 43.2933, 1)
            BMR = round((10 * weight) + (6.25 * height) - (5 * user_age) - 161)

            BMI = round(weight / pow(height / 100, 2), 1)

            if 0 < user_age <= 15:
                fat_Percentage = round((1.51 * BMI) - (0.70 * user_age) - (3.6 * int(user_gender)) + 1.4, 1)
            else:
                fat_Percentage = round((1.20 * BMI) + (0.23 * user_age) - (10.8 * int(user_gender)) - 5.4, 1)

            VFI = round(fat_Percentage - 10)

            str(BMI)
            str(VFI)

            bmi_result = str(BMI)
            fat_Percentage = str(fat_Percentage)
            vfi_result = str(VFI)
            tbw_result = str(TBW)
            muscle_mass_result = str(muscle_mass)
            water_percentage_result = str(water_percentage)
            bmr_result = str(BMR)

            with open(user_name + "_results.txt", 'w') as file:
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
                #results()

def loading():
    #video w progress bar loading
    arduca.destroy()
    arduca_backend()

def arduca_page():
    def back():
        main_menu()
        arduca.destroy()
    ctk.set_appearance_mode("system")

    ctk.set_default_color_theme("blue")

    global weight
    global age
    global height
    global arduca

    arduca = ctk.CTk()
    arduca.title("Arduca")
    arduca.resizable(width=False, height=False)

    frame = ctk.CTkFrame(master=arduca)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    arduca.geometry("400x400")

    label = ctk.CTkLabel(master=frame, text='Arduca Test', font=('Arial', 30, "bold"))
    label.pack(pady=12, padx=10)

    #Input lel weight wel height

    button = ctk.CTkButton(master=frame, text='Submit', command=loading)
    button.pack(pady=12, padx=10)
    #el loading maloosh lazma howa keda keda el backend saree3 bs 7n3ml zy delay 2osayar 5aleees 3shan el user y7s en el program bye3mel processing keteer

    arduca.mainloop()


def main_menu():
    def exit():
        main_menu_page.destroy()
    ctk.set_appearance_mode("system")

    ctk.set_default_color_theme("blue")

    main_menu_page = ctk.CTk()
    main_menu_page.title("Arduca")
    main_menu_page.resizable(width=False, height=False)

    main_menu_page.geometry("400x400")

    label = ctk.CTkLabel(main_menu_page, text="Arduca")
    label.pack(pady=20)

    frame = ctk.CTkFrame(master=main_menu_page)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    # Add image
    # label_img = Label(frame, image=bg)
    # label_img.place(x = 0,y = -1010)

    label = ctk.CTkLabel(master=frame, text='Main Menu', font=('Arial', 30, "bold"))
    label.pack(pady=12, padx=10)

    label = ctk.CTkLabel(master=frame, text='Welcome ' + user_save + '!', font=('Arial', 15))
    label.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text='Start Arduca', command=arduca_page)
    button.pack(pady=12, padx=10)

    button_3 = ctk.CTkButton(master=frame, text='Exit and logout', command=exit)
    button_3.pack(pady=12, padx=10)

    main_menu_page.mainloop()


def register():
    ctk.set_appearance_mode("system")

    ctk.set_default_color_theme("blue")

    global register_page

    register_page = ctk.CTk()
    register_page.geometry("400x500")
    register_page.title("Arduca")

    frame = ctk.CTkFrame(master=register_page)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    global gender

    choices = ['Choose gender', 'Male', 'Female']
    gender = StringVar(register_page)
    gender.set('Choose gender')

    global user_name
    global user_gender

    user_name = ctk.CTkEntry(master=frame, placeholder_text="Name")
    user_name.pack(pady=12, padx=10)

    user_gender = OptionMenu(frame, gender, *choices)
    user_gender.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text='Register', command=register_backend)
    button.pack(pady=12, padx=10)

    frame_2 = ctk.CTkFrame(master=frame)
    frame_2.pack(pady=0, padx=40, fill='none', expand=True)

    label_2 = ctk.CTkLabel(master=frame_2, text="Already registered?")
    label_2.pack(pady=20)

    button_2 = ctk.CTkButton(master=frame_2, text='Login', command=move_login)
    button_2.pack(pady=12, padx=10)

    login_page.destroy()

    register_page.mainloop()


def register_backend():
    path = user_name.get() + '.txt'

    if os.path.exists(path):
        tkmb.showerror(title="Registration Failed", message="Username already exists")
    else:
        if gender.get() == 'Male':
            gender_user = 'M'
        elif gender.get() == 'Female':
            gender_user = 'F'
        with open(path, 'w') as f:
            f.write(gender_user)
        move_login()


def login_pagetk():
    # Selecting GUI theme - dark, light , system (for system default)
    ctk.set_appearance_mode("system")

    # Selecting color theme - blue, green, dark-blue
    ctk.set_default_color_theme("blue")

    global login_page

    login_page = ctk.CTk()
    login_page.title("Arduca")
    login_page.resizable(width=False, height=False)
    # img = ImageTk.PhotoImage(Image.open('login page logo.png'))
    # bg = ImageTk.PhotoImage(img)

    login_page.geometry("400x500")

    label = ctk.CTkLabel(login_page, text="Arduca")
    label.pack(pady=20)

    frame = ctk.CTkFrame(master=login_page)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    # Add image
    # label_img = Label(frame, image=bg)
    # label_img.place(x = 0,y = -1010)

    label = ctk.CTkLabel(master=frame, text='Login', font=('Arial', 30, "bold"))
    label.pack(pady=12, padx=10)

    global user_entry

    user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
    user_entry.pack(pady=12, padx=10)

    def login():
        path = user_entry.get() + '.txt'
        path_clone = user_entry.get()
        global user_save
        user_save = path_clone

        if os.path.exists(path):
            tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
            login_page.destroy()
            main_menu()


        else:
            tkmb.showerror(title="Login Failed", message="Invalid Username")

    button = ctk.CTkButton(master=frame, text='Login', command=login)
    button.pack(pady=12, padx=10)

    frame_2 = ctk.CTkFrame(master=frame)
    frame_2.pack(pady=0, padx=40, fill='none', expand=True)

    unregistered = ctk.CTkLabel(master=frame_2, text="Not registered?")
    unregistered.pack(pady=20)

    register_button = ctk.CTkButton(master=frame_2, text='Register', command=register)
    register_button.pack(pady=12, padx=10)

    login_page.mainloop()


def move_login():
    register_page.destroy()
    login_pagetk()


login_pagetk()

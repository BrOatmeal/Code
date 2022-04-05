from tkinter import *
import csv
import os
import pandas as pd


def patientpage():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("patient profile")
    screen6.geometry("300x500")

    frame = Frame(screen6, height=66, width=200, highlightbackground="black", highlightthickness=2)
    frame.place(x=80, y=10)

    profilePic = Label(screen6, height=4, width=8, bg="green")
    profilePic.place(x=7, y=10)

    name = Label(frame, text="Name:       ")
    name.grid(column=0, row=0)
    sex = Label(frame, text="Sex:       ")
    sex.grid(column=0, row=1)
    DoB = Label(frame, text="DoB:       ")
    DoB.grid(column=0, row=2)

    settings = Button(text=u"\u2699", height=2, width=4)
    settings.place(x=260, y=15)

    Appointments = Label(screen6, text="Appointments", height=10, width=40, relief="solid")
    Appointments.place(x=7, y=80)

    CurPre = Label(screen6, text="Current Prescriptions", height=10, width=18, relief="solid")
    CurPre.place(x=7, y=240)

    CurPat = Label(screen6, text="Current Patients", height=10, width=18, relief="solid")
    CurPat.place(x=160, y=240)

    PatMedDat = Label(screen6, text="Patient Medical Records", height=8, width=40, relief="solid")
    PatMedDat.place(x=7, y=400)


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    Button(screen3, text="OK", command=screen3.withdraw()).pack()
    screen3.withdraw()
    screen3.withdraw()
    screen2.withdraw()
    screen.withdraw()

    patientpage()


def password_not_found():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password not found").pack()
    Button(screen4, text="OK", command=screen4.withdraw()).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User not found")
    screen5.geometry("150x100")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command=screen4.withdraw()).pack()
    screen5.withdraw()


def register_user():
    print("Working.....")
    username_info = username.get()
    password_info = password.get()

    file = open("info.csv", "a")
    file.write(username_info + "\n")
    file.write(password_info + "\n" + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registeration was a success", fg="White", font=("Arial", 11)).pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.config(show='*')
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    file = open("info.csv", "r")
    verify = file.read().splitlines()
    if username1 and password1 in verify:
        login_success()
    if username1 and password1 not in verify:
        user_not_found()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.config(show='*')
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main():
    global screen
    screen = Tk()
    screen.config(bg="grey38")
    screen.geometry("300x300")
    screen.title("Log in and register page")

    logo_frame = Frame(screen).pack()
    logo = PhotoImage(file="MicrosoftTeams-image-200.png")
    logo_label = Label(logo_frame, image=logo).pack()

    labels_frame = Frame(screen)
    labels_frame.pack()
    labels_frame.config(bg="grey38")

    mediapp = Label(labels_frame, text="MediApp", font=("Arials", 13),width=30,bg="grey38")
    mediapp.grid(row=0, column=0)

    loginbutton = Button(labels_frame, text="Login", command=login,width=30)
    loginbutton.grid(row=1, column=0)

    registerbutton = Button(labels_frame, text="Register", command=register,width=30)
    registerbutton.grid(row=2, column=0)

    screen.mainloop()


main()
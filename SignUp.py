from tkinter import *
import csv
import os
import pandas as pd


def delete2():
    screen3.withdraw()

def delete3():
    screen4.withdraw()

def delete4():
    screen5.withdraw()

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text="OK", command=delete2).pack()

def password_not_found():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password not found").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User not found")
    screen5.geometry("150x100")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command=delete3).pack()

def register_user():

    print("Working.....")
    username_info = username.get()
    password_info = password.get()


    file = open("info.csv", "a")
    file.write(username_info+"\n")
    file.write(password_info+"\n"+"\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registeration was a success", fg="gold2", font=("Arial", 11)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    screen1.config(bg="black")

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
    screen2.config(bg="black")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below").pack()
    Label(screen2, text = "").pack()

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
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width=10, height=1, command=login_verify).pack()

def main():
    global screen
    screen = Tk()
    screen.config(bg="black")
    screen.geometry("300x250")
    screen.title("Log in and register page")
    Label(text="MediApp", bg="grey", width="300", height=2, font=("Arials", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height=2, width=30, command=login).pack()
    Label(text="").pack()
    Button(text="Regiser", height="2", width="30", command=register).pack()

    screen.mainloop()

main()
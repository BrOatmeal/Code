# ------Imports--------

from tkinter import *
from tkinter import messagebox
import pandas as pd
import unittest

# -------Pandas------------

dataframe = pd.read_csv("CSV_New.csv")

# ------Windows-----------

MainPage = Tk()
MainPage.config(bg="grey38")
MainPage.geometry("300x300")
MainPage.title("Log in and register page")
MainPage.resizable(False, False)

patientWindow = Toplevel(MainPage)
patientWindow.title("patient profile")
patientWindow.geometry("300x550")
patientWindow.config(bg="grey38")
patientWindow.withdraw()

UserNotFoundPage = Toplevel(MainPage)
UserNotFoundPage.title("User not found")
UserNotFoundPage.geometry("150x100")
UserNotFoundPage.withdraw()

passwordNotFoundPage = Toplevel(MainPage)
passwordNotFoundPage.title("Success")
passwordNotFoundPage.geometry("150x100")
passwordNotFoundPage.withdraw()

registerPage = Toplevel(MainPage)
registerPage.title("Register")
registerPage.geometry("300x250")
registerPage.config(bg="grey38")
registerPage.withdraw()

LoginPage = Toplevel(MainPage)
LoginPage.title("Login")
LoginPage.geometry("300x250")
LoginPage.config(bg="grey38")
LoginPage.withdraw()

LoginSuccessPage = Toplevel(MainPage)
LoginSuccessPage.withdraw()
# -------Main Page-------

logo_frame = Frame(MainPage).pack()
logo = PhotoImage(file="MicrosoftTeams-image-200.png")
logo_label = Label(logo_frame, image=logo).pack()

labels_frame = Frame(MainPage)
labels_frame.pack()
labels_frame.config(bg="grey38")

mediapp = Label(labels_frame, text="MediApp", font=("Arial", 13), width=30, bg="grey38")
mediapp.grid(row=0, column=0)

docint = IntVar()
docint.set(0)
patint = IntVar()
patint.set(0)

# ------photo logo------

newlogo_frame = Frame(patientWindow).pack()
logonew = PhotoImage(file="MicrosoftTeams-image-smolish.png")
newlogo_label = Label(patientWindow, image=logonew)
newlogo_label.place(x=150, y=10)

settings = Button(patientWindow, text=u"\u2699", height=2, width=4, bg="grey48")
settings.place(x=260, y=15)


# --------unittest----
def test_file1_method():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"


print(test_file1_method)
def add(x, y):
    return x + y

class Test(unittest.TestCase):
    def addition(self):
        self.assertEquals(add(4, 5), 9)
    if __name__ == "__main":
        unittest.main()

print(unittest)




def login_verify():
    username1 = username_entry1.get()
    password1 = password_entry1.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    file = open("CSV_New.csv", "r")
    verify = dataframe.iloc[0, 1]
    if username1 and password1 in verify:
        login_success()
    elif username1 or password1 not in verify:
        user_not_found()


Label(LoginPage, text="Please enter details below", fg="white", bg="grey38").pack()
Label(LoginPage, text="", bg="grey38").pack()
Label(LoginPage, text="Username * ", fg="white", bg="grey38").pack()
username_entry1 = Entry(LoginPage)
username_entry1.pack()

Label(LoginPage, text="", bg="grey38").pack()
Label(LoginPage, text="Password * ", fg="white", bg="grey38").pack()
password_entry1 = Entry(LoginPage)
password_entry1.config(show='*')
password_entry1.pack()

Label(LoginPage, text="", bg="grey38").pack()
Button(LoginPage, text="Login", width=10, height=1, command=login_verify).pack()


# ------loginPage-------


def login():
    MainPage.withdraw()
    LoginPage.deiconify()


loginbutton = Button(labels_frame, text="Login", command=login, width=30)
loginbutton.grid(row=1, column=0)


# ------RegisterButton------
def register_user():
    username_info = username.get()
    password_info = password.get()

    if docint.get() == 1:
        dataframe.loc[len(dataframe.index)] = [username_info, password_info, "Doctor"]
        print(dataframe.to_string)
    elif patint.get() == 1:
        dataframe.loc[len(dataframe.index)] = [username_info, password_info, "Patient"]
        print(dataframe.to_string)
    else:
        print(docint.get())
        print(patint.get())
        print("neither")

    dataframe.to_csv("CSV_New.csv", index=False)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(registerPage, text="Registration was a success", fg="Black", font=("Arial", 11)).pack()


def show_register_page():
    registerPage.deiconify()
    MainPage.withdraw()


registerbutton = Button(labels_frame, text="Register", command=show_register_page, width=30)
registerbutton.grid(row=2, column=0)
# ------UsernameVerify------

username_verify = StringVar()
password_verify = StringVar()


# ------hideLoginSuccessPage-----


def hideloginsuccess():
    LoginSuccessPage.withdraw()


# --------LoginSuccessPage-------


def login_success():
    Button(LoginSuccessPage, text="OK", command=hideloginsuccess).pack()
    LoginSuccessPage.withdraw()
    LoginPage.withdraw()
    MainPage.withdraw()
    patientpage()


# --------verification----------


def user_not_found():
    messagebox.showerror("Incorrect", "Incorrect username/Password")
    Label(UserNotFoundPage, text="User not found").pack()
    Button(UserNotFoundPage, text="OK", command=UserNotFoundPage.withdraw).pack()


# --------LoginSuccess---------


def patientpage():
    # -------features-------------
    patientWindow.deiconify()

    frame = Frame(patientWindow, height=66, width=200, highlightbackground="gold2", highlightthickness=2, bg="gold2",
                  relief="solid")
    frame.place(x=80, y=10)

    profilePic = Label(patientWindow, height=4, width=8, bg="blue")
    profilePic.place(x=7, y=10)

    name = Label(frame, text="Name:   ", bg="gold2")
    name.grid(column=0, row=0)
    sex = Label(frame, text="Sex:   ", bg="gold2")
    sex.grid(column=0, row=1)
    DoB = Label(frame, text="DoB:   ", bg="gold2")
    DoB.grid(column=0, row=2)

    settings = Button(text=u"\u2699", height=2, width=4, bg="grey48")
    settings.place(x=260, y=15)

    appointments = Label(patientWindow, text="Appointments", height=10, width=40, relief="solid", bg="gold2")
    appointments.place(x=7, y=80)

    meddat = Label(patientWindow, text="Current Medical Data", height=10, width=18, relief="solid", bg="gold2")
    meddat.place(x=7, y=240)

    curmed = Label(patientWindow, text="Current Medication", height=10, width=18, relief="solid", bg="gold2")
    curmed.place(x=160, y=240)

    envdat = Label(patientWindow, text="Environmental Data", height=8, width=40, relief="solid", bg="gold2")
    envdat.place(x=7, y=400)


username = StringVar()
password = StringVar()

# ---------Labels---------

Label(registerPage, text="Please enter details below").pack()
Label(registerPage, text="").pack()
Label(registerPage, text="Username * ").pack()
username_entry = Entry(registerPage, textvariable=username)
username_entry.pack()
Label(registerPage, text="Password * ").pack()
password_entry = Entry(registerPage, textvariable=password)
password_entry.config(show='*')
password_entry.pack()
docbtn = Checkbutton(registerPage, text="Doctor", onvalue=1, offvalue=0, bg="grey38", variable=docint)
docbtn.pack()
patbtn = Checkbutton(registerPage, text="Patient", onvalue=1, offvalue=0, bg="grey38", variable=patint)
patbtn.pack()
Label(registerPage, text="").pack()
Button(registerPage, text="Register", width=10, height=1, command=register_user).pack()

mainloop()

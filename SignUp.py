# ------Imports--------

from tkinter import *

# ------Windows--------

MainPage = Tk()
MainPage.config(bg="grey38")
MainPage.geometry("300x300")
MainPage.title("Log in and register page")
MainPage.resizable(False, False)

patientWindow = Toplevel(MainPage)
patientWindow.title("patient profile")
patientWindow.geometry("300x500")
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
registerPage.withdraw()

LoginPage = Toplevel(MainPage)
LoginPage.title("Login")
LoginPage.geometry("300x250")
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

newlogo_frame=Frame(patientWindow).pack()
logonew=PhotoImage(file="MicrosoftTeams-image-smolish.png")
newlogo_label=Label(patientWindow,image=logonew)
newlogo_label.place(x=150,y=10)
# ------loginPage-------

def login():
    MainPage.withdraw()
    LoginPage.deiconify()
    Label(LoginPage, text="Please enter details below").pack()
    Label(LoginPage, text="").pack()
    Label(LoginPage, text="Username * ").pack()
    username_entry1 = Entry(LoginPage, textvariable=username_verify)
    username_entry1.pack()

    Label(LoginPage, text="").pack()
    Label(LoginPage, text="Password * ").pack()
    password_entry1 = Entry(LoginPage, textvariable=password_verify)
    password_entry1.config(show='*')
    password_entry1.pack()

    Label(LoginPage, text="").pack()
    Button(LoginPage, text="Login", width=10, height=1, command=login_verify).pack()


loginbutton = Button(labels_frame, text="Login", command=login, width=30)
loginbutton.grid(row=1, column=0)


# ------RegisterButton------
def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open("info.csv", "a")
    file.write(username_info + "\n")
    file.write(password_info + "\n" + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(registerPage, text="Registeration was a success", fg="Black", font=("Arial", 11)).pack()


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
    LoginSuccessPage.withdraw()
    LoginPage.withdraw()
    MainPage.withdraw()
    patientpage()


# --------LoginSuccess---------

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    file = open("info.csv", "r")
    verify = file.read().splitlines()
    if username1 and password1 in verify:
        login_success()
    if username1 and password1 not in verify:
        user_not_found()


# ----------Labels---------------

def patientpage():
    # -------features-------------
    patientWindow.deiconify()

    frame = Frame(patientWindow, height=66, width=200, highlightbackground="black", highlightthickness=2)
    frame.place(x=80, y=10)

    profilePic = Label(patientWindow, height=4, width=8, bg="green")
    profilePic.place(x=7, y=10)

    # -------PersonsAttributes-----

    name = Label(frame, text="Name:       ")
    name.grid(column=0, row=0)
    sex = Label(frame, text="Sex:       ")
    sex.grid(column=0, row=1)
    DoB = Label(frame, text="DoB:       ")
    DoB.grid(column=0, row=2)

    # --------settingsIcon---------

    settings = Button(text=u"\u2699", height=2, width=4)
    settings.place(x=260, y=15)

    # --------Options--------------

    Appointments = Label(patientWindow, text="Appointments", height=10, width=40, relief="solid")
    Appointments.place(x=7, y=80)

    CurPre = Label(patientWindow, text="Current Prescriptions", height=10, width=18, relief="solid")
    CurPre.place(x=7, y=240)

    CurPat = Label(patientWindow, text="Current Patients", height=10, width=18, relief="solid")
    CurPat.place(x=160, y=240)

    PatMedDat = Label(patientWindow, text="Patient Medical Records", height=8, width=40, relief="solid")
    PatMedDat.place(x=7, y=400)


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
Label(registerPage, text="").pack()
Button(registerPage, text="Register", width=10, height=1, command=register_user).pack()


def password_not_found():
    Label(passwordNotFoundPage, text="Password not found").pack()
    Button(passwordNotFoundPage, text="OK", command=passwordNotFoundPage.withdraw).pack()


def user_not_found():
    Label(UserNotFoundPage, text="User not found").pack()
    Button(UserNotFoundPage, text="OK", command=UserNotFoundPage.withdraw).pack()
    UserNotFoundPage.withdraw()



mainloop()

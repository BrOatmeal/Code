
# ------Imports--------

from tkinter import *

# ------Windows--------

MainPage = Tk()
MainPage.config(bg="grey38")
MainPage.geometry("300x300")
MainPage.title("Log in and register page")


patientWindow = Toplevel(MainPage)
patientWindow.title("patient profile")
patientWindow.geometry("300x500")
patientWindow.withdraw()

doctorWindow = Toplevel(MainPage)
doctorWindow.config(bg="grey38")
doctorWindow.title("MediApp")
doctorWindow.geometry("300x550")
doctorWindow.resizable(False, False)
doctorWindow.withdraw()

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

#---------Entries---------

username = StringVar()
password = StringVar()

# ------loginPage-------

def login():
    Label(LoginPage, text="Please enter details below").pack()
    Label(LoginPage, text="").pack()

    docbtn = Checkbutton(LoginPage, text="Doctor")
    docbtn.pack()

    patbtn = Checkbutton(LoginPage, text="Patient")
    patbtn.pack()

loginbutton = Button(labels_frame, text="Login", command=login, width=30)
loginbutton.grid(row=1, column=0)

# ------RegisterButton------
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

    Label(registerPage, text="Registration was a success", fg="White", font=("Arial", 11)).pack()

registerbutton = Button(labels_frame, text="Register", command=registerPage, width=30)
registerbutton.grid(row=2, column=0)

#-------Labels--------------

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
    Patientpage()


# --------LoginSuccess---------

def login_verify():
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

#--------Labels-------------------

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

#--------Patient Page-------------

def Patientpage():
    # -------features-------------

    frame = Frame(patientWindow, height=66, width=200, highlightbackground="black", highlightthickness=2, bg="gold2")
    frame.place(x=80, y=10)

    profilePic = Label(patientWindow, height=4, width=8, bg="green")
    profilePic.place(x=7, y=10)

    # -------PersonsAttributes-----

    name = Label(frame, text="Name:       ", bg="gold2")
    name.grid(column=0, row=0)
    sex = Label(frame, text="Sex:       ", bg="gold2")
    sex.grid(column=0, row=1)
    DoB = Label(frame, text="DoB:       ", bg="gold2")
    DoB.grid(column=0, row=2)

    # --------settingsIcon---------

    settings = Button(text=u"\u2699", height=2, width=4)
    settings.place(x=260, y=15)

    # --------Options--------------

    Appointments = Label(patientWindow, text="Appointments", height=10, width=40, relief="solid", bg="gold2")
    Appointments.place(x=7, y=80)

    CurPre = Label(patientWindow, text="Current Prescriptions", height=10, width=18, relief="solid", bg="gold2")
    CurPre.place(x=7, y=240)

    CurPat = Label(patientWindow, text="Current Patients", height=10, width=18, relief="solid", bg="gold2")
    CurPat.place(x=160, y=240)

    PatMedDat = Label(patientWindow, text="Patient Medical Records", height=8, width=40, relief="solid", bg="gold2")
    PatMedDat.place(x=7, y=400)
#--------Picture--------------
    logo_frame = Frame(doctorWindow).place(x=150, y=10)
    logo = PhotoImage(file="MicrosoftTeams-image-smolish.png")
    logo_label = Label(logo_frame, image=logo)
    logo_label.place(x=150, y=10)

def Doctorpage():
    # -------features-------------
    frame = Frame(doctorWindow, height=66, width=200, highlightbackground="gold2", highlightthickness=2, bg="gold2",
                  relief="solid")
    frame.place(x=80, y=10)

    profilePic = Label(doctorWindow, height=4, width=8, bg="blue")
    profilePic.place(x=7, y=10)
#-------PersonAttributes------
    name = Label(frame, text="Name:   ", bg="gold2")
    name.grid(column=0, row=0)
    sex = Label(frame, text="Sex:   ", bg="gold2")
    sex.grid(column=0, row=1)
    DoB = Label(frame, text="DoB:   ", bg="gold2")
    DoB.grid(column=0, row=2)
#-------SettingIcon------------
    settings = Button(text=u"\u2699", height=2, width=4, bg="grey48")
    settings.place(x=260, y=15)
#-------Options----------------
    appointments = Label(doctorWindow, text="Appointments", height=10, width=40, relief="solid", bg="gold2")
    appointments.place(x=7, y=80)

    meddat = Label(doctorWindow, text="Current Medical Data", height=10, width=18, relief="solid", bg="gold2")
    meddat.place(x=7, y=240)

    curmed = Label(doctorWindow, text="Current Medication", height=10, width=18, relief="solid", bg="gold2")
    curmed.place(x=160, y=240)

    envdat = Label(doctorWindow, text="Environmental Data", height=8, width=40, relief="solid", bg="gold2")
    envdat.place(x=7, y=400)
#--------Picture-----------

    logo_frame = Frame(doctorWindow).place(x=150, y=10)
    logo = PhotoImage(file="MicrosoftTeams-image-smolish.png")
    logo_label = Label(logo_frame, image=logo)
    logo_label.place(x=150, y=10)

# ---------Labels---------




def password_not_found():
    Label(passwordNotFoundPage, text="Password not found").pack()
    Button(passwordNotFoundPage, text="OK", command=passwordNotFoundPage.withdraw()).pack()


def user_not_found():
    Label(UserNotFoundPage, text="User not found").pack()
    Button(UserNotFoundPage, text="OK", command=UserNotFoundPage.withdraw()).pack()
    UserNotFoundPage.withdraw()



mainloop()
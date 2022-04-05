window = Toplevel()
window.config(bg="grey38")
window.title("MediApp")
window.geometry("300x550")
window.resizable(False, False)
window.withdraw()

screen = Toplevel()
screen.config(bg="grey38")
screen.geometry("300x300")
screen.title("Log in and register page")


screen1 = Toplevel(screen)
screen1.title("Register")
screen1.geometry("300x250")


screen2 = Toplevel(screen)
screen2.title("Login")
screen2.geometry("300x250")

screen3 = Toplevel(screen)

screen4 = Toplevel(screen)
screen4.title("Success")
screen4.geometry("150x100")

screen5 = Toplevel(screen)
screen5.title("User not found")
screen5.geometry("150x100")

screen6 = Toplevel(screen)
screen6.title("patient profile")
screen6.geometry("300x550")
screen6.config(bg="grey38")

screen7 = Toplevel(screen)
screen7.title("Error - Choose Type")
screen7.geometry("150x100")


docint = IntVar()
docint.set(0)

patint = IntVar()
patint.set(0)

########################################################################################################################

def Doctorpage():

    frame = Frame(screen6, height=66, width=200, highlightbackground="black", highlightthickness=2, bg="gold2")
    frame.place(x=80, y=10)

    profilePic = Label(screen6, height=4, width=8, bg="green")
    profilePic.place(x=7, y=10)

    name = Label(frame, text="Name:       ", bg="gold2")
    name.grid(column=0, row=0)
    sex = Label(frame, text="Sex:       ", bg="gold2")
    sex.grid(column=0, row=1)
    DoB = Label(frame, text="DoB:       ", bg="gold2")
    DoB.grid(column=0, row=2)

    settings = Button(text=u"\u2699", height=2, width=4)
    settings.place(x=260, y=15)

    Appointments = Label(screen6, text="Appointments", height=10, width=40, relief="solid", bg="gold2")
    Appointments.place(x=7, y=80)

    CurPre = Label(screen6, text="Current Prescriptions", height=10, width=18, relief="solid", bg="gold2")
    CurPre.place(x=7, y=240)

    CurPat = Label(screen6, text="Current Patients", height=10, width=18, relief="solid", bg="gold2")
    CurPat.place(x=160, y=240)

    PatMedDat = Label(screen6, text="Patient Medical Records", height=8, width=40, relief="solid", bg="gold2")
    PatMedDat.place(x=7, y=400)

    logo_frame = Frame(screen6).place(x=150, y=10)
    logo = PhotoImage(file="MicrosoftTeams-image-smolish.png")
    logo_label = Label(logo_frame, image=logo)
    logo_label.place(x=150, y=10)

    settings = Button(text=u"\u2699", height=2, width=4, bg="grey48")
    settings.place(x=260, y=15)


def Patientpage():

    frame = Frame(window, height=66, width=200, highlightbackground="gold2", highlightthickness=2, bg="gold2",
                  relief="solid")
    frame.place(x=80, y=10)

    profilePic = Label(window, height=4, width=8, bg="blue")
    profilePic.place(x=7, y=10)

    name = Label(frame, text="Name:   ", bg="gold2")
    name.grid(column=0, row=0)
    sex = Label(frame, text="Sex:   ", bg="gold2")
    sex.grid(column=0, row=1)
    DoB = Label(frame, text="DoB:   ", bg="gold2")
    DoB.grid(column=0, row=2)

    settings = Button(text=u"\u2699", height=2, width=4, bg="grey48")
    settings.place(x=260, y=15)

    appointments = Label(window, text="Appointments", height=10, width=40, relief="solid", bg="gold2")
    appointments.place(x=7, y=80)

    meddat = Label(window, text="Current Medical Data", height=10, width=18, relief="solid", bg="gold2")
    meddat.place(x=7, y=240)

    curmed = Label(window, text="Current Medication", height=10, width=18, relief="solid", bg="gold2")
    curmed.place(x=160, y=240)

    envdat = Label(window, text="Environmental Data", height=8, width=40, relief="solid", bg="gold2")
    envdat.place(x=7, y=400)

    logo_frame = Frame(window).place(x=150, y=10)
    logo = PhotoImage(file="MicrosoftTeams-image-smolish.png")
    logo_label = Label(logo_frame, image=logo)
    logo_label.place(x=150, y=10)

########################################################################################################################

    if docint == 1:
        screen3.withdraw()
        screen2.withdraw()
        screen.withdraw()
        Doctorpage()

    elif patint == 1:
        screen3.withdraw()
        screen2.withdraw()
        screen.withdraw()
        Patientpage()

    else:
        screen3.withdraw()
        screen3.withdraw()
        screen2.withdraw()
        screen.withdraw()
        Errorpage()

########################################################################################################################

    docbtn = Checkbutton(screen2, text="Doctor", onvalue=1, offvalue=0)
    docbtn.pack()

    patbtn = Checkbutton(screen2, text="Patient", onvalue=1, offvalue=0)
    patbtn.pack()

########################################################################################################################

def Errorpage():

    Choosetype = Label(screen7, text="---- Error - Please select the account type ----")
    Choosetype.pack()

########################################################################################################################

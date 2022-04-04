import tkinter as tk

login = tk.Tk()
login.title("MediApp Login")
login.geometry("200x125")

window = tk.Tk()
window.title("MediApp")
window.geometry("300x550")
window.resizable(False, False)

window.withdraw()


def loginfunc():

    username = "Doctor"
    password = "password"

    ubox = Username.get()
    pbox = Password.get()

    if ubox == username and pbox == password:
        login.withdraw()
        window.deiconify()

    else:
        print("wrong password")


Username = tk.Entry(login, width=20)
Username.grid(row=0, column=1)
usernameLabel = tk.Label(login, text="Username:")
usernameLabel.grid(row=0, column=0)

Password = tk.Entry(login, width=20)
Password.config(show="*")
Password.grid(row=1, column=1)
passwordLabel = tk.Label(login, text="Password:")
passwordLabel.grid(row=1, column=0)

loginButton = tk.Button(login, text="Login", width=5, command=loginfunc)
loginButton .grid(row=2, column=0, columnspan=2)

frame = tk. Frame(window, height=66, width=200, highlightbackground="black", highlightthickness=2)
frame.place(x=80, y=10)

profilePic = tk.Label(window, height=4, width=8, bg="green")
profilePic.place(x=7, y=10)

name = tk.Label(frame, text="Name:       ")
name.grid(column=0, row=0)
sex = tk.Label(frame, text="Sex:       ")
sex.grid(column=0, row=1)
DoB = tk.Label(frame, text="DoB:       ")
DoB.grid(column=0, row=2)

settings = tk.Button(text=u"\u2699", height=2, width=4)
settings.place(x=260, y=15)

Appointments = tk.Label(window, text="Appointments", height=10, width=40, relief="solid")
Appointments.place(x=7, y=80)

CurPre = tk.Label(window, text="Current Prescriptions", height=10, width=18, relief="solid")
CurPre.place(x=7, y=240)

CurPat = tk.Label(window, text="Current Patients", height=10, width=18, relief="solid")
CurPat.place(x=160, y=240)

PatMedDat = tk.Label(window, text="Patient Medical Records", height=8, width=40, relief="solid")
PatMedDat.place(x=7, y=400)

window.mainloop()
login.mainloop()
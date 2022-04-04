import tkinter as tk
import pandas as pd

import csv
window = tk.Tk()
window.config(bg="black")
window.title("MediApp")
window.geometry("300x550")
window.resizable(False, False)

def PatientView():

    frame = tk.Frame(window, height=66, width=200, highlightbackground="gold2", highlightthickness=2)
    frame.place(x=80, y=10)

    profilePic = tk.Label(window, height=4, width=8, bg="gold2")
    profilePic.place(x=7, y=10)

    name = tk.Label(frame, text="Name:       ")
    name.grid(column=0, row=0)
    sex = tk.Label(frame, text="Sex:       ")
    sex.grid(column=0, row=1)
    DoB = tk.Label(frame, text="DoB:       ")
    DoB.grid(column=0, row=2)

    settings = tk.Button(text=u"\u2699", height=2, width=4)
    settings.place(x=260, y=15)

    appointments = tk.Label(window, text="Appointments", height=10, width=40, relief="solid")
    appointments.place(x=7, y=80)

    meddat = tk.Label(window, text="Current Medical Data", height=10, width=18, relief="solid")
    meddat.place(x=7, y=240)

    curmed = tk.Label(window, text="Current Medication", height=10, width=18, relief="solid")
    curmed.place(x=160, y=240)

    envdat = tk.Label(window, text="Environmental Data", height=8, width=40, relief="solid")
    envdat.place(x=7, y=400)

window.mainloop()
from tkinter import *
import pandas as pd
import csv

window = Tk()
window.config(bg="grey38")
window.title("MediApp")
window.geometry("300x550")
window.resizable(False, False)



frame = Frame(window, height=66, width=200, highlightbackground="gold2", highlightthickness=2, bg="gold2", relief="solid")
frame.place(x=80, y=10)

profilePic = Label(window, height=4, width=8, bg="blue")
profilePic.place(x=7, y=10)

name = Label(frame, text="Name:   ", bg="gold2")
name.grid(column=0, row=0)
sex = Label(frame, text="Sex:   ", bg="gold2")
sex.grid(column=0, row=1)
DoB = Label(frame, text="DoB:   ", bg="gold2")
DoB.grid(column=0, row=2)

settings = Button(text=u"\u2699", height=2, width=4)
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



window.mainloop()
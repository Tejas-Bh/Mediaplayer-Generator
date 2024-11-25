import os
from natsort import natsorted
import glob
from tkinter import *
from tkinter import filedialog
import time

# Initializes window
root = Tk()
root.geometry("800x600")
root.title("Mediaplayer Generator")
text = "Choose Folder"


# Function for generating Html-Mediaplayer
def choosegen():
    file_path = filedialog.askdirectory()
    print(file_path)
    file = (file_path + "/mediaplayer.html")
    html = open(file, "w")
    html.write('<!DOCTYPE html>\n<html> <head>'
    '<style>body {background-color: rgb(31 41 55); font-family: "Segoe UI"; padding-left: 1.25rem } pre {font-family: "Segoe UI"; font-size: 0.875em; } label {display: flex; } </style>'
    '<title>Media Player</title></head> <body> <h2> <font color=lightblue> Media Line up </h2><p> <table cellpadding="5" style="width: 100%;">\n')
    files = os.listdir(file_path)
    files = natsorted(files)
    mp3_count = len(glob.glob1(file_path, "*.mp3"))
    wav_count = len(glob.glob1(file_path, "*.wav"))
    vid_count = len(glob.glob1(file_path, "*.mp4"))
    if mp3_count != 0:
        for mp3 in files:
            if mp3.endswith(".mp3"):
                print(mp3)
                input_window = Tk()
                input_window.title(mp3)
                input_window.geometry("400x400")
                input_header = Label(input_window, text=f"Add a remark for \n{mp3}", font=("Calibri", 15))
                input_header.pack()
                input_sub = Label(input_window, text='If you don\'t want to, just click "Done".', font=("Calibri", 10))
                input_sub.pack()
                entry = Entry(input_window)
                entry.pack()
                entry.focus_set()
                SubmitButton = Button(input_window, text="Done", command=input_window.quit)
                SubmitButton.pack()
                input_window.mainloop()
                remark = entry.get()
                input_window.destroy()
                if remark:
                    table = f'<tr><td><font color=white><b><label>{mp3}</label><br/><audio controls src= "{mp3}">Your browser does not support the <code>audio</code> element.</audio></td><td style="color:white;">{remark}</td></tr>\n'
                else:
                    table = f'<tr><td><font color=white><b><label>{mp3}</label><br/><audio controls src= "{mp3}">Your browser does not support the <code>audio</code> element.</audio>\n'
                html.write(table)
                time.sleep(1)
    if wav_count != 0:
        html.write('<h2 style="color: lightblue">Wav files</h2>')
        for wav in files:
            if wav.endswith(".wav"):
                print(wav)
                input_window = Tk()
                input_window.title(wav)
                input_window.geometry("400x400")
                input_header = Label(input_window, text=f"Add a remark for \n{wav}", font=("Calibri", 15))
                input_header.pack()
                input_sub = Label(input_window, text='If you don\'t want to, just click "Done".', font=("Calibri", 10))
                input_sub.pack()
                entry = Entry(input_window)
                entry.pack()
                entry.focus_set()
                SubmitButton = Button(input_window, text="Done", command=input_window.quit)
                SubmitButton.pack()
                input_window.mainloop()
                remark = entry.get()
                input_window.destroy()
                if remark:
                    table = f'<tr><td><font color=white><b><label>{wav}</label><br/><audio controls src= "{wav}">Your browser does not support the <code>audio</code> element.</audio></td><td style="color:white;">{remark}</td></tr>\n'
                else:
                    table = f'<tr><td><font color=white><b><label>{wav}</label><br/><audio controls src= "{wav}">Your browser does not support the <code>audio</code> element.</audio>\n'
                html.write(table)
                time.sleep(1)
    if vid_count != 0:
        html.write('<h2 style="color: lightblue">Videos</h2>')
        for vid in files:
            if vid.endswith(".mp4"):
                print(vid)
                input_window = Tk()
                input_window.title(vid)
                input_window.geometry("400x400")
                input_header = Label(input_window, text=f"Add a remark for \n{vid}", font=("Calibri", 15))
                input_header.pack()
                input_sub = Label(input_window, text='If you don\'t want to, just click "Done".', font=("Calibri", 10))
                input_sub.pack()
                entry = Entry(input_window)
                entry.pack()
                entry.focus_set()
                SubmitButton = Button(input_window, text="Done", command=input_window.quit)
                SubmitButton.pack()
                input_window.mainloop()
                remark = entry.get()
                input_window.destroy()
                if remark:
                    table = f'<tr><td><font color=white><b><label>{vid}</label><br/><video controls width="20%" src= "{vid}">Your browser does not support the <code>video</code> element.</video></td><td style="color:white;">{remark}</td></tr>\n'
                else:
                    table = f'<tr><td><font color=white><b><label>{vid}</label><br/><video controls width="20%" src= "{vid}">Your browser does not support the <code>video</code> element.</video>\n'
                html.write(table)
                time.sleep(1)

    html.close()
    Donelabel = Label(root, text=("Your html file has been generated in " + file))
    Donelabel.pack()
    os.startfile(f"{file}")


# Title
Title = Label(root, text="Mediaplayer Generator", font=("Calibri", 20))
Title.pack()

# Instructions
instructions = Label(root, text="This program will generate HTML in the selected folder adding mediaplayer capability "
                                "to all .mp3 and .wav files in the selected folder")
instructions.pack()


Space = Label(root, text=" ", font=("Calibri", 100))
Space.pack()

# Pack button
gen = Button(root, text=text, font=("Calibri", 15), command=choosegen)
gen.pack()

# Version
version = Label(root, text="v4; 2023 (tkinter)")
version.pack()


root.mainloop()

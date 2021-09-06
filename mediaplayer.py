import os
import glob
from tkinter import *
from tkinter import filedialog

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
    html.write('<!DOCTYPE html>\n<html> <head><title>Media '
               'Player</title></head> <body bgcolor=black> <h2> <font color=white> Media Line up '
               '<div id="txt"></div></h2><p> <table border=2>\n')
    files = os.listdir(file_path)
    Donelabel = Label(root, text=("Your html file has been generated in " + file))
    Donelabel.pack()
    mp3_count = len(glob.glob1(file_path, "*.mp3"))
    wav_count = len(glob.glob1(file_path, "*.wav"))
    if mp3_count != 0:
        for mp3 in files:
            if mp3.endswith(".mp3"):
                print(mp3)
                table = '<tr><td><font color=white><b><label>' + mp3 + '</label><br/><audio controls src= "' + mp3 + '">Your browser does not support the <code>audio</code> element.</audio>\n'
                html.write(table)
    if wav_count != 0:
        html.write('<h2 style="color: white;">Wav files</h2>')
        for wav in files:
            if wav.endswith(".wav"):
                print(wav)
                table = '<tr><td><font color=white><b><label>' + wav + '</label><br/><audio controls src= "' + wav + '">Your browser does not support the <code>audio</code> element.</audio>\n'
                html.write(table)


# Title
Title = Label(root, text="Mediaplayer Generator", font=("Trebuchet MS", 20))
Title.pack()


instructions = Label(root, text="This program will generate HTML in the selected folder adding mediaplayer capability "
                                "to all .mp3 and .wav files in the selected folder")
instructions.pack()


Space = Label(root, text=" ", font=("Trebuchet MS", 100))
Space.pack()


gen = Button(root, text=text, font=("Trebuchet MS", 15), command=choosegen)
gen.pack()


MadeBy = Label(root, text='Made by Tejas Bhagawatula')
MadeBy.pack()


version = Label(root, text="v0.1; 2021")
version.pack()


root.mainloop()

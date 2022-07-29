#!/usr/bin/env python3

import typer
from pytube import YouTube
import os
import  vlc
import time
import subprocess

app = typer.Typer()

@app.command()
def ytdl(link: str):
    # url input from user
    yt = YouTube(link)
    # yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
  
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
  
    # check for destination to save file
    # print("Enter the destination (leave blank for current directory)")
    # destination = str(input(">> ")) or '.'
    destination = './music'
  
    # download the file
    out_file = video.download(output_path=destination)
  
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
  
    # result of success
    print(yt.title + " has been successfully downloaded in the 'music' directory.")

@app.command()
def list():
    for x in os.listdir("./music"):
        if x.endswith(".mp3"):
            # Prints only mp3 files present in directory
            print(x)

@app.command()
def play(file: str):
    found = False
    for x in os.listdir("./music"):
        if x == file:
            found = True
            print("Playing requested file. Ctrl+C to abort or wait till time finishes.")
            p = vlc.MediaPlayer(os.path.join(os.getcwd(), "music", x))
            p.play()
            time.sleep(30)
            p.stop()

    if (found == False):
        print("Could not find requested file to play. Try again.")

@app.command()
def convert(file: str):
    found = False
    for x in os.listdir("./music"):
        if x == file:
            found = True
            inputFile = os.path.join(os.getcwd(), "music", x)
            outputFile = inputFile.split(".")[0] + ".wav"
            # Converts this mp3 file to wav and saves it in the same music directory.
            subprocess.call(['ffmpeg', '-i', inputFile, outputFile])
    if (found == False):
        print("Could not find requested file to convert. Try again.")

if __name__ == "__main__":
    app()


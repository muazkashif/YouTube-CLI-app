# YouTube-CLI-app 
A simple CLI app made for MacOS using Typer that utilizes the PyTube module to download, list, play and convert music files from YouTube music video links.

## Features
- Extracts mp3 files from YouTube music video links specified in the command prompt to the configured music directory.
- Lists exisiting mp3 files in the configured music directory.
- Plays desired mp3 file from within the configured music directory.
- Converts .mp3 files in the the configured music directory to .wav files as desired for other purposes.

## Installation
1. Clone the repository.
2. `pip install -r requirements.txt`
3. Edit the `#!/usr/bin/env python3` shebang with the relevant python version as needed to run commands without specifying python.
4. Edit the `./music` and `music` instances as needed to specify your desired directory in which to store music.

##  Usage
- `./ytmusic.py ytdl <YouTube URL>`: downloads the music video URL as an mp3 file and stores it in the configured music directory.
- `./ytmusic.py list`: lists all the music files stored in the configured music directory.
- `./ytmusic.py play <MP3 file name exactly as stored>`: plays specified .mp3 file stored in the configured music directory.
- `./ytmusic.py convert <MP3 file name exactly as stored>`: converts specified .mp3 file to .wav stores it in the same configured music directory.

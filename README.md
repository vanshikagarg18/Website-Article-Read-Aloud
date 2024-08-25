# Website-Article-Read-Aloud

## Overview
This project is a Python-based application that converts the text of a website article into speech. It utilizes the 'newspaper3k' library for web scraping, 'nltk' for natural language processing, and 'gTTS' (Google Text-to-Speech) for converting text to audio. The generated speech is saved as an MP3 file and played automatically.

The 'newspaper3k' library is designed for easy web scraping and article extraction but may not work perfectly with all websites. Test with different URLs to ensure compatibility.
The 'gTTS' library provides a simple interface to Google Text-to-Speech, but it requires an internet connection to function.
Ensure 'ffmpeg' is installed and added to your PATH to use 'pydub' for audio playback.

## Features
- Web Scraping: Downloads and parses an article from a given URL.
- Natural Language Processing: Uses nltk to process the text.
- Text-to-Speech: Converts the processed text into speech using gTTS.
- Audio Playback: Saves the speech as an MP3 file and plays it.

## Requirements
- Python: 3.x
- newspaper3k: Install using pip install newspaper3k
- nltk: Install using pip install nltk
- gTTS: Install using pip install gTTS
- pydub: Install using pip install pydub (required for playing the mp3 file)

## How to Use
1) Setup:
- Ensure Python and the required packages are installed on your system.
- Install ffmpeg and add it to your system's PATH.
2) Run the Script:
- Copy the provided code into a Python script file.
- Replace the article URL with the URL of the article you want to convert to speech.
- Execute the script to generate and play the audio.

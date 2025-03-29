# Website-Article-Read-Aloud

## Overview
This Python-based application allows users to convert the text of a webpage article into speech. It features a graphical user interface (GUI) built with Tkinter, enabling users to enter a URL and listen to the extracted text. The application utilizes the newspaper3k library for web scraping and pyttsx3 for text-to-speech conversion, allowing offline functionality.

## Features
- Web Scraping: Downloads and extracts an article from a given URL using newspaper3k.
- Text-to-Speech: Converts extracted text into speech using pyttsx3.
- Adjustable Speech Speed: Users can increase or decrease the speech speed.
- Gradient Background: A visually appealing gradient enhances the UI.
- Threading Support: Runs speech conversion in a separate thread to keep the GUI responsive.
- Copy & Clear: Users can easily clear the URL input box.

## GUI 
<img width="404" alt="image" src="https://github.com/user-attachments/assets/c2f98123-fa28-48c8-84a2-4aff6908cf39" />

## Requirements
- Python: 3.x
- newspaper3k: Install using pip install newspaper3k
- pyttsx3: Install using pip install pyttsx3
- ttkthemes: Install using pip install ttkthemes
- Additional Dependencies: Install ffmpeg (for better audio support on some systems)

## How to Use
1) Setup:
  - Ensure Python and the required packages are installed.
  - Install ffmpeg and add it to your system's PATH (if needed).
2) Run the Script:
  - Copy the provided code into a Python script file.
  - Run the script using: python script.py
3) Enter a URL:
  - Paste the URL of an article into the text box.
  - Click the "Convert & Play" button to start speech conversion.
4) Control Speech Speed:
  - Use the "➖ Slow" and "➕ Fast" buttons to adjust the speech speed.
5) Clear the Input:
  - Click "Clear" to remove the entered URL.

## Notes
- The newspaper3k library may not work on all websites. Test with different URLs.
- pyttsx3 runs offline, so an internet connection is not required.
- Speech speed ranges from 75 WPM to 250 WPM.

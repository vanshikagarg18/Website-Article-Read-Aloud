# Website-Article-Read-Aloud

## Overview
The Webpage to Speech Converter is a simple web application that extracts text from any online article and converts it into speech using Google Text-to-Speech (gTTS). The user enters a URL, and the app processes the webpage content, extracts readable text, and plays an audio version of it.

## Features
- Extracts text from any webpage
- Converts text into speech using gTTS
- Displays extracted text for reference
- Plays the generated speech directly in the browser
  
## GUI 
<img width="870" alt="image" src="https://github.com/user-attachments/assets/151cdd45-2b1f-43d4-b941-8db0a574c013" />

## Demo
https://huggingface.co/spaces/vanshika-garg/website_read_aloud

## Requirements
- Python (Backend processing)
- Gradio (User Interface)
- newspaper3k (Text extraction from articles)
- gTTS (Google Text-to-Speech) (Text-to-speech conversion)

## Notes
- The newspaper3k library may not work on all websites. Test with different URLs.
- gTTS runs online, so an internet connection is required.
- Speech speed ranges from 75 WPM to 250 WPM.

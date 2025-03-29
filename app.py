import gradio as gr
from newspaper import Article
import pyttsx3
import threading

# Initialize text-to-speech engine
engine = pyttsx3.init()
speech_speed = 150  # Default speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Softer female voice

is_speaking = False  # Global flag to track speaking status

# Function to extract text and read aloud
def process_url(url, speed):
    global is_speaking
    try:
        # Download and parse article
        article = Article(url)
        article.download()
        article.parse()

        if not article.text:
            return "No readable text found on this page."

        # Set speech speed and start speaking in a separate thread
        engine.setProperty('rate', speed)
        is_speaking = True

        def speak_text():
            global is_speaking
            engine.say(article.text)
            engine.runAndWait()
            is_speaking = False  # Reset flag after finishing

        speech_thread = threading.Thread(target=speak_text)
        speech_thread.start()

        return article.text  # Display extracted text
    
    except Exception as e:
        return f"Error: {e}"

# Function to stop speaking
def stop_speaking():
    global is_speaking
    if is_speaking:
        engine.stop()  # Stop the speech engine
        is_speaking = False
        return "Speech stopped."
    return "No speech in progress."

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# Webpage to Speech Converter")
    gr.Markdown("Convert any online article into speech! Just enter a URL and adjust the reading speed.")

    url_input = gr.Textbox(label="Enter URL", placeholder="Paste article URL here...")
    speed_slider = gr.Slider(75, 250, value=150, step=25, label="Speech Speed (WPM)")
    output_text = gr.Textbox(label="Extracted Text")

    speak_button = gr.Button("🎙 Convert & Play")
    stop_button = gr.Button("🛑 Stop")

    speak_button.click(process_url, inputs=[url_input, speed_slider], outputs=[output_text])
    stop_button.click(stop_speaking, outputs=[output_text])

demo.launch()

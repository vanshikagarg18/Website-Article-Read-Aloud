import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from newspaper import Article
import pyttsx3
import threading
from PIL import Image, ImageDraw, ImageTk

# Initialize pyttsx3 engine
engine = pyttsx3.init()
speech_speed = 150  # Default speech speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Softer female voice

# Function to extract text and speak
def process_url():
    url = url_entry.get("1.0", tk.END).strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    try:
        article = Article(url)
        article.download()
        article.parse()

        if not article.text:
            messagebox.showerror("Error", "No readable text found on this page.")
            return

        engine.setProperty('rate', speech_speed)
        engine.say(article.text)
        engine.runAndWait()
        messagebox.showinfo("Success", "Text extracted and reading started!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Function to run process_url in a separate thread
def run_in_thread():
    thread = threading.Thread(target=process_url)
    thread.start()

# Function to increase speed
def increase_speed():
    global speech_speed
    if speech_speed < 250:
        speech_speed += 25
        update_speed_label()

# Function to decrease speed
def decrease_speed():
    global speech_speed
    if speech_speed > 75:
        speech_speed -= 25
        update_speed_label()

# Function to update speed label
def update_speed_label():
    speed_label.config(text=f"Speed: {speech_speed} WPM")

# Function to clear the URL entry
def clear_url():
    url_entry.delete("1.0", tk.END)

# Function to create and apply a full-window gradient
def create_gradient(canvas, width, height, color1, color2):
    gradient = Image.new("RGB", (width, height), color1)
    draw = ImageDraw.Draw(gradient)
    
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * (y / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (y / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    gradient = ImageTk.PhotoImage(gradient)
    canvas.create_image(0, 0, anchor=tk.NW, image=gradient)
    canvas.image = gradient  # Prevent garbage collection

# Create main window
root = ThemedTk(theme="arc")
root.title("Webpage to Speech Converter")
root.geometry("550x450")

# Create a Canvas for full gradient background
canvas = tk.Canvas(root, width=550, height=450)
canvas.pack(fill="both", expand=True)

# Apply gradient background
create_gradient(canvas, 550, 450, (230, 240, 255), (245, 230, 255))

# Create a Frame for UI Elements
frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=400)

# Title Label
title_label = tk.Label(frame, text="Webpage to Speech", font=("Helvetica", 18, "bold"), fg="#34495E", bg="white")
title_label.pack(pady=10)

# URL Entry with Thin Border
url_entry = tk.Text(frame, font=("Arial", 12), width=50, height=3, bd=1, relief="solid", wrap="word")
url_entry.pack(pady=10, padx=20)

# Convert & Play Button
process_btn = tk.Button(frame, text="Convert & Play", font=("Arial", 12, "bold"), fg="white",
                        bg="#2ECC71", activebackground="#27AE60", bd=0, relief="ridge",
                        padx=10, pady=5, command=run_in_thread)
process_btn.pack(pady=10)

# Speed Label
speed_label = tk.Label(frame, text=f"Speed: {speech_speed} WPM", font=("Arial", 12), fg="#34495E", bg="white")
speed_label.pack(pady=5)

# Speed Buttons
speed_frame = tk.Frame(frame, bg="white")
speed_frame.pack()

dec_btn = tk.Button(speed_frame, text="➖ Slow", font=("Arial", 12, "bold"), fg="white",
                    bg="#E74C3C", activebackground="#C0392B", bd=0, relief="ridge",
                    padx=10, pady=5, command=decrease_speed)
dec_btn.grid(row=0, column=0, padx=10)

inc_btn = tk.Button(speed_frame, text="➕ Fast", font=("Arial", 12, "bold"), fg="white",
                    bg="#3498DB", activebackground="#2980B9", bd=0, relief="ridge",
                    padx=10, pady=5, command=increase_speed)
inc_btn.grid(row=0, column=1, padx=10)

# Clear Button
clear_btn = tk.Button(frame, text="Clear", font=("Arial", 12, "bold"), fg="white",
                      bg="#E67E22", activebackground="#D35400", bd=0, relief="ridge",
                      padx=10, pady=5, command=clear_url)
clear_btn.pack(pady=15)

# Run the application
root.mainloop()

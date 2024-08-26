from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import os
import database_file_1 as db
from database_file_2 import display_database_contents

def image_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def text_to_speech(text, output_audio_file):
    tts = gTTS(text)
    tts.save(output_audio_file)



def convert_image_to_audio():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    extracted_text = image_to_text(image_path)
    if not extracted_text:
        messagebox.showerror("Error", "No text found in the image.")
        return

    with open("extracted_text.txt", "w") as text_file:
        text_file.write("extracted_text.txt")

    audio_file_path = "output_audio.mp3"
    text_to_speech(extracted_text, audio_file_path)

    image_name = os.path.basename(image_path)
    db.insert_into_db(image_name, image_path, extracted_text, audio_file_path)

    messagebox.showinfo("Success", f"Text has been converted to speech and saved as {audio_file_path}.")

    os.system(f"start {audio_file_path}")


root = tk.Tk()
root.title("Image to Text and Speech Converter")

root.geometry("800x400")

label = tk.Label(root, text="Select an image to convert text to speech:", font=("Arial", 12))
label.pack(pady=20)


convert_button = tk.Button(root, text="Select Image and Convert", command=convert_image_to_audio, font=("Arial", 12),
                           bg="red", fg="white")
convert_button.pack(pady=20)


display_button = tk.Button(root, text="Show Database Contents", command=display_database_contents, font=("Arial", 12), bg="green", fg="white")
display_button.pack(pady=10)



#run
root.mainloop()

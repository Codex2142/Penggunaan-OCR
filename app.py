import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'F:\Tesseract OCR\tesseract.exe'

def upload_file():
    global filepath
    filepath = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    if filepath:
        output_text.insert(tk.END, f"File loaded: {filepath}\n")

def process_file():
    if filepath:
        try:
            img = Image.open(filepath)
            extracted_text = pytesseract.image_to_string(img)
            output_text.insert(tk.END, extracted_text + "\n")
        except Exception as e:
            output_text.insert(tk.END, f"An error occurred: {e}\n")
    else:
        output_text.insert(tk.END, "No file loaded.\n")

root = tk.Tk()
root.title("Simple File Processor")

frame = tk.Frame(root)
frame.pack(pady=20)

# Upload button
upload_button = tk.Button(frame, text="Upload File", command=upload_file)
upload_button.pack(side=tk.LEFT, padx=10)

# Bbutton proses
process_button = tk.Button(frame, text="Process File", command=process_file)
process_button.pack(side=tk.LEFT, padx=10)

# Textbox
output_text = Text(root, height=10, width=50)
output_text.pack(pady=20)

root.mainloop()

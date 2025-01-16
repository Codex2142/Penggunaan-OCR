import tkinter as tk
from tkinter import filedialog, Text

def upload_file():
    # Fungsi ini akan memungkinkan pengguna untuk memilih file dari sistem file mereka.
    global filepath
    filepath = filedialog.askopenfilename(initialdir="/", title="Select File")
    if filepath:
        output_text.insert(tk.END, f"File loaded: {filepath}\n")

def process_file():
    if filepath:
        try:
            with open(filepath, 'r', encoding='cp1252') as file:
                data = file.read()
                output_text.insert(tk.END, data + "\n")
        except UnicodeDecodeError as e:  # Mengganti Exception dengan UnicodeDecodeError untuk spesifik
            output_text.insert(tk.END, f"Failed to read file with UTF-8 encoding: {e}\n")
            output_text.insert(tk.END, "Try a different encoding if the error persists.\n")
        except Exception as e:
            output_text.insert(tk.END, f"An error occurred: {e}\n")
    else:
        output_text.insert(tk.END, "No file loaded.\n")


# Membuat jendela utama
root = tk.Tk()
root.title("Simple File Processor")

# Mengatur frame untuk tombol dan textbox
frame = tk.Frame(root)
frame.pack(pady=20)

# Tombol untuk mengunggah file
upload_button = tk.Button(frame, text="Upload File", command=upload_file)
upload_button.pack(side=tk.LEFT, padx=10)

# Tombol untuk memproses file
process_button = tk.Button(frame, text="Process File", command=process_file)
process_button.pack(side=tk.LEFT, padx=10)

# Textbox untuk menampilkan output
output_text = Text(root, height=10, width=50)
output_text.pack(pady=20)

# Menjalankan aplikasi GUI
root.mainloop()

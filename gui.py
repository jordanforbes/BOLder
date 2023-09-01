import tkinter as tk
import os
from tkinter import filedialog
from bolder import bolder
import html


def browse_input_file(entry_input_path):
    file_path = filedialog.askopenfilename(filetypes=[("EPUB Files","*.epub")])
    if file_path:
        entry_input_path.delete(0, tk.END)
        entry_input_path.insert(0, file_path)

def browse_output_folder(entry_output_folder):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_output_folder.delete(0, tk.END)
        entry_output_folder.insert(0, folder_path)

def convert(entry_input_path, entry_output_folder):
    input_path = entry_input_path.get()
    output_folder = entry_output_folder.get()
    book_title = os.path.splitext(os.path.basename(input_path))[0]

    if input_path and input_path.endswith('.epub') and output_folder:
        # output_folder = output_folder[:-5] + "_modified.epub"  # Generate output path
        output_path = os.path.join(output_folder, book_title + "_BOLded.epub")
        bolder(input_path, output_path)
        tk.messagebox.showinfo("Conversion Complete", "EPUB modification and repackaging completed.")
    else:
        tk.messagebox.showerror("Invalid Input", "Please select a valid EPUB file.")

def gui():

  root = tk.Tk()
  root.title = ("BOLder")

  browse_input_button = tk.Button(root, text="Browse", command=lambda: browse_input_file(entry_input_path))
  browse_input_button.pack()

  entry_input_path = tk.Entry(root, width=50)
  entry_input_path.pack()


  browse_output_button = tk.Button(root, text = "Browse Output Folder", command=lambda: browse_output_folder(entry_output_folder))
  browse_output_button.pack()

  entry_output_folder = tk.Entry(root, width=50)
  entry_output_folder.pack()

  convert_button = tk.Button(root, text="Bold It!", command=lambda: convert(entry_input_path, entry_output_folder) )
  convert_button.pack()

  root.mainloop()

gui()

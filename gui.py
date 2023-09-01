import tkinter as tk

def gui(browse_input_file, browse_output_folder, convert):

  root = tk.Tk()
  root.title("BOLder")

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


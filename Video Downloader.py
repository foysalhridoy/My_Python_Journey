import tkinter as tk
from tkinter import Label, Entry, Button, messagebox, filedialog, StringVar, GROOVE
from pytube import YouTube
import traceback

def browse_folder():
    folder_selected = filedialog.askdirectory(title="Select Download Folder")
    if folder_selected:
        download_path.set(folder_selected)

def download_video():
    url = video_url.get().strip()
    path = download_path.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL.")
        return

    if not path:
        messagebox.showerror("Error", "Please select a destination folder.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)
        messagebox.showinfo("Success", f"Video successfully downloaded to:\n{path}")
    except Exception as e:
        traceback.print_exc()  # Print full error to console for debugging
        messagebox.showerror("Error", f"Failed to download video.\nReason:\n{str(e)}")

# Create main window
root = tk.Tk()
root.geometry("520x280")
root.title("YouTube Video Downloader")
root.config(bg="PaleGreen1")
root.resizable(False, False)

# Tkinter variables
video_url = StringVar()
download_path = StringVar()

# Widgets
Label(root, text="YouTube Video Downloader", font="SegoeUI 16 bold", bg="PaleGreen1", fg="darkgreen").grid(row=0, column=0, columnspan=3, pady=15)

Label(root, text="YouTube URL:", bg="salmon", font="Arial 12").grid(row=1, column=0, sticky="e", padx=5, pady=5)
Entry(root, textvariable=video_url, width=40, font="Arial 12").grid(row=1, column=1, columnspan=2, padx=5, pady=5)

Label(root, text="Save to:", bg="salmon", font="Arial 12").grid(row=2, column=0, sticky="e", padx=5, pady=5)
Entry(root, textvariable=download_path, width=30, font="Arial 12").grid(row=2, column=1, padx=5, pady=5)
Button(root, text="Browse", command=browse_folder, width=10, bg="bisque", relief=GROOVE).grid(row=2, column=2, padx=5, pady=5)

Button(root, text="Download Video", command=download_video, width=20, font="Georgia 13", bg="thistle1", relief=GROOVE).grid(row=3, column=1, pady=25)

root.mainloop()

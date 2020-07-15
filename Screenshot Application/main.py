import pyautogui
import tkinter as tk
from tkinter import filedialog
import time

root = tk.Tk()
root.geometry("450x350")
root.title("Screen Shot App")
frame = tk.Frame(root)
frame.pack()

def takescreenshot():
    root.withdraw()
    time.sleep(1)

    myScreenshot = pyautogui.screenshot()

    file_path = filedialog.asksaveasfilename(defaultextension = ".png")

    myScreenshot.save(file_path)
    
    root.update()
    root.deiconify()

button = tk.Button(
    frame, 
    text = "Take Screenshot",
    command = takescreenshot,
    bg = 'blue',
    fg = 'white', 
    font = 10)

button.pack(side = tk.LEFT, pady = 130, padx = 20)

close = tk.Button(
    frame, 
    text = "Quit",
    command = quit,
    bg = 'blue',
    fg = 'white', 
    font = 10)

close.pack(side = tk.LEFT, pady = 130)


root.mainloop()
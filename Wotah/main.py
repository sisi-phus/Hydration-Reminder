from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font, PhotoImage, Canvas  #WE HATE USING * DO NOT IMPORT * GRRR
import timer


# IMPORTANT, DO NOT FORGET !!!!!!! :3
# widgets = GUI elements like buttons, textboxes labels, img, etc.
# windows = container for widgets ^.w.^

# placement guide for x: x=0 is the left side of the window, x=500 is the right side, x=270 is middle ^_^
# placement guide for y: 100 is higher than 300 (doom) think css padding type beat, 300 is middle

window = tk.Tk()  # makes window
window.geometry("550x600")
window.title("Water Reminder")
window.resizable(width=False, height=False)

def load_custom_font():
    custom_font = font.Font(family="Rubik Glitch", size=20)
    label.config(font=Rubix)

font_path = "C:\\Users\\User\\Documents\\RubikGlitch-Regular.ttf"
custom_font = font.Font(window, name="Rubik Glitch", size=20)
window.option_add("*Font", custom_font)

# i wanna put all img here :O

startimg = PhotoImage(file="Start.png")
logo = PhotoImage(file="kittilog.png")  # logo has to be photo img
window.iconphoto(True, logo)
bg_image = PhotoImage(file="background.png")

####################################################
canvas = Canvas(window, width=550, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, image=bg_image, anchor="nw")

def countdown():
    global total_secs

    if total_secs > 0:
        hours, remainder = divmod(total_secs, 3600)
        minutes, seconds = divmod(remainder, 60)
        timer_label.config(text=f"{hours:02}:{minutes:02}")
        total_secs -= 1
        window.after(1000, countdown)
    else:
        timer_label.config(text="Hydration time")
    

def on_button_click():
    label.config(text=f"Hydration Timer set every {timer.get_time()//3600}:{timer.get_time()//60}")
    global total_secs
    total_secs = timer.get_time()
    countdown()


label = tk.Label(window, text="meow",font=("Rubik Glitch", "16"), borderwidth=0, highlightthickness=0) # If i want to customize text, i have to do it here, not in the .pack
label.pack_configure(pady=10) # .pack is just for positioning and stuff ^.w.^
canvas.create_window(270, 100, window=label)

timer_label = tk.Label(window, text="00:00",font="Rubik Glitch", "16")
timer_label.pack(pady=10)
canvas.create_window(270, 200, window=timer_label)

WaterTracker = tk.Button (window, image=startimg, command=on_button_click)
WaterTracker.pack(pady=10)
canvas.create_window(270, 300, window=WaterTracker)




window.mainloop()  # wills the window into our plane of existance

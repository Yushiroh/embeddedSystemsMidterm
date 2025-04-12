
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial = GPIO.LOW)

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/yushiroh/coding/esMidterms/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def allOn():
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)

def allOff():
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)


window = Tk()

window.geometry("500x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    text="Living Room",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: GPIO.output(12, GPIO.HIGH), 
    relief="flat"
)
button_1.place(
    x=338.0,
    y=204.0,
    width=143.0,
    height=101.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    text="Kitchen",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: GPIO.output(10, GPIO.HIGH),
    relief="flat"
)

button_2.place( x=179.0, y=204.0, width=142.0, height=101.0)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    text="Master's Bedroom",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: GPIO.output(8, GPIO.HIGH),
    relief="flat"
)
button_3.place(
    x=19.0,
    y=204.0,
    width=143.0,
    height=101.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    text="ALL OFF",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: allOff(), 
    relief="flat"
)
button_4.place(
    x=92.0,
    y=376.0,
    width=143.0,
    height=94.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    text="ALL ON",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: allOn(), 
    relief="flat"
)
button_5.place(
    x=266.0,
    y=376.0,
    width=143.0,
    height=94.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    text="OFF1",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: GPIO.output(8, GPIO.LOW),
    relief="flat",
)
button_6.place(
    x=52.0,
    y=315.0,
    width=77.0,
    height=27.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    text= "OFF2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: GPIO.output(10, GPIO.LOW),

    relief="flat"
)
button_7.place(
    x=211.0,
    y=315.0,
    width=77.0,
    height=27.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    text = "OFF3",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: GPIO.output(12, GPIO.LOW),

    relief="flat"
)
button_8.place(
    x=370.0,
    y=315.0,
    width=77.0,
    height=27.0
)

canvas.create_text(
    179.0,
    243.0,
    anchor="nw",
    text="Kitchen",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    17.0,
    243.0,
    anchor="nw",
    text="Living Room",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    71.0,
    321.0,
    anchor="nw",
    text="OFF",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    121.0,
    415.0,
    anchor="nw",
    text="ALL ON",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    295.0,
    415.0,
    anchor="nw",
    text="ALL OFF",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    230.0,
    321.0,
    anchor="nw",
    text="OFF",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    389.0,
    321.0,
    anchor="nw",
    text="OFF",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    342.0,
    243.0,
    anchor="nw",
    text="Master’s Bedroom",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    19.0,
    121.0,
    481.0,
    170.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    83.0,
    129.0,
    anchor="nw",
    text="Home Automation System",
    fill="#000000",
    font=("Inter", 27 * -1)
)
window.resizable(False, False)
window.mainloop()


from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage

def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    # Calculate coordinates for the four corners of the rectangle
    x1_outer, y1_outer = x1 + radius, y1 + radius
    x2_outer, y2_outer = x2 - radius, y2 - radius

    # Create rounded corners using arcs
    canvas.create_arc(x1, y1, x1_outer, y1_outer, start=90, extent=90, **kwargs)
    canvas.create_arc(x2_outer, y1, x2, y1_outer, start=0, extent=90, **kwargs)
    canvas.create_arc(x2_outer, y2_outer, x2, y2, start=270, extent=90, **kwargs)
    canvas.create_arc(x1, y2_outer, x1_outer, y2, start=180, extent=90, **kwargs)

    # Create rectangles to connect the arcs
    canvas.create_rectangle(x1_outer, y1, x2_outer, y2, **kwargs)
    canvas.create_rectangle(x1, y1_outer, x2, y2_outer, **kwargs)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Activate_GUI():
    window = Tk()
    window.geometry("385x709")
    window.configure(bg="#E0E0E0")

    canvas = Canvas(
        window,
        bg="#E0E0E0",
        height=709,
        width=385,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    round_rectangle(
        canvas,
        12.0,
        29.0,
        373.0,
        691.0,
        70,
        fill="#000000",
        outline=""
    )

    round_rectangle(
        canvas,
        24.0,
        42.0,
        362.0,
        677.0,
        70,
        fill="orange",
        outline=""
    )

    # Other canvas elements go here

    window.resizable(True, True)
    window.mainloop()

# Define ASSETS_PATH here

# Call the Activate_GUI function to create the GUI
Activate_GUI()

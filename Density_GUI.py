
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import Density_Tracker
from tkinter import StringVar

def Activate_GUI():
    MaxDensity = 12
    grabData = Density_Tracker.peopleCount
    Density = (round((grabData / MaxDensity)*100),"%")


    def round_rectangle(x1, y1, x2, y2, radius, **kwargs):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)


    def create_gradient(canvas, x1, y1, x2, y2, start_color, end_color, num_segments):
        # Calculate color transition step for each segment
        r_step = (end_color[0] - start_color[0]) / num_segments
        g_step = (end_color[1] - start_color[1]) / num_segments
        b_step = (end_color[2] - start_color[2]) / num_segments

        # Create gradient segments
        for i in range(num_segments):
            r = int(start_color[0] + i * r_step)
            g = int(start_color[1] + i * g_step)
            b = int(start_color[2] + i * b_step)

            color = f"#{r:02X}{g:02X}{b:02X}"  # Convert RGB values to hexadecimal
            canvas.create_rectangle(x1, y1 + i, x2, y1 + i + 1, fill=color, outline="")

    def run_code():
        Density_Tracker.Run_Code()

    def updateDensity():
        canvas.itemconfig(Active_Density, text=Density)
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jmarshall/Library/Mobile Documents/com~apple~CloudDocs/Object_Tracker/build/assets/frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("385x709")
    window.configure(bg = "#E0E0E0")


    canvas = Canvas(
        window,
        bg = "#E0E0E0",
        height = 709,
        width = 385,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    round_rectangle(
        12.0,
        29.0,
        373.0,
        691.0,
        70,
        fill="#000000",
        outline="")
    print("hi")
    round_rectangle(
        24.0,
        42.0,
        362.0,
        677.0,
        70,
        fill="orange",
        outline="")

    round_rectangle(
        97.0,
        34.0,
        289.0,
        66.0,
        25,
        fill="#000000",
        outline="")
    round_rectangle(

    30.0,
    405.0,
    356.0,
    660.0,
        25,
    fill= "white",
    outline ="")

    canvas.create_rectangle(
        40.0,
        499.0,
        353.0,
        526.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        40.0,
        555.0,
        353.0,
        582.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        40.0,
        611.0,
        353.0,
        638.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        90.0,
        475.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("FiraSans Regular", 20 * -1)
    )

    canvas.create_text(
        245.0,
        475.0,
        anchor="nw",
        text="Density",
        fill="#000000",
        font=("FiraSans Regular", 20 * -1)
    )

    canvas.create_text(
        44.0,
        502.0,
        anchor="nw",
        text="Library",
        fill="#000000",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        44.0,
        558.0,
        anchor="nw",
        text="Science Building Main floor",
        fill="#000000",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        44.0,
        615.0,
        anchor="nw",
        text="Social Science Building",
        fill="#000000",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        44.0,
        585.0,
        anchor="nw",
        text="Bagwell Education Building",
        fill="#000000",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        44.0,
        529.0,
        anchor="nw",
        text="ALC Study Center",
        fill="#000000",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        263.0,
        502.0,
        anchor="nw",
        text="9%",
        fill="green",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        263.0,
        530.0,
        anchor="nw",
        text="20%",
        fill="green",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        263.0,
        558.0,
        anchor="nw",
        text="27%",
        fill="green",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        263.0,
        585.0,
        anchor="nw",
        text="32%",
        fill="green",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        263.0,
        615.0,
        anchor="nw",
        text="38%",
        fill="green",
        font=("FiraSans Regular", 16 * -1)
    )

    canvas.create_text(
        59.0,
        417.0,
        anchor="nw",
        text="Current Best Study Areas",
        fill="#000000",
        font=("FiraSans Regular", 24 * -1)
    )

    canvas.create_text(
        188.0,
        125.0,
        anchor="nw",
        text="Room Density",
        fill="#FFFFFF",
        font=("FiraSans SemiBold", 26 * -1)
    )

    Active_Density = canvas.create_text(
        193.0,
        159.0,
        anchor="nw",
        text = "88%",
        fill="#D32F2F",
        font=("FiraSans SemiBold", 80 * -1)
    )
    round_rectangle(
        258.0,
        289.0,
        265.0,
        312.0,
        10,
        fill="#59BF69",
        outline="")

    round_rectangle(
        272.0,
        283.0,
        279.0,
        322.0,
        10,
        fill="#D6D15D",
        outline="")

    round_rectangle(
        286.0,
        273.0,
        292.0,
        332.0,
        10,
        fill="white",
        outline="")

    round_rectangle(
        299.0,
        259.0,
        306.0,
        342.0,
        10,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        235.0,
        302.0,
        image=image_image_1
    )

    canvas.create_text(
        207.0,
        343.0,
        anchor="nw",
        text="Audio Level",
        fill="#FFFFFF",
        font=("FiraSans SemiBold", 24 * -1)
    )

    round_rectangle(
        30.0,
        120.0,
        180.0,
        382.0,
        25,
        fill="white",
        outline="")

    canvas.create_text(
        42.0,
        134.0,
        anchor="nw",
        text="Student Center",
        fill="#000000",
        font=("FiraSans Bold", 18 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        297.0,
        58.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        317.0,
        59.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        336.0,
        59.0,
        image=image_image_4
    )

    canvas.create_text(
        53.0,
        54.0,
        anchor="nw",
        text="12:24",
        fill="#000000",
        font=("Inter Bold", 11 * -1)
    )


    canvas.create_text(
        80.0,
        83.0,
        anchor="nw",
        text="Kennesaw Campus",
        fill="yellow",
        font=("FiraSans Bold", 24),
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        295.0,
        100.0,
        image=image_image_5
    )

    canvas.create_rectangle(
        119.5,
        452.5,
        264.0,
        454.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        73.0,
        166.0,
        135.0,
        168.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        44.0,
        170.0,
        anchor="nw",
        text="Max Capacity: 208",
        fill="#000000",
        font=("FiraSans Bold", 14 * -1)
    )

    canvas.create_rectangle(
        75.0,
        199.0,
        125.0,
        208.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        212.0,
        142.0,
        222.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        226.0,
        151.0,
        236.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        240.0,
        142.0,
        249.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        254.0,
        121.0,
        263.0,
        fill="#E83737",
        outline="")

    canvas.create_rectangle(
        75.0,
        268.0,
        104.0,
        277.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        281.0,
        94.0,
        291.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        295.0,
        96.0,
        305.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        309.0,
        108.0,
        318.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        323.0,
        117.0,
        332.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        337.0,
        108.0,
        346.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        350.0,
        94.0,
        360.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        75.0,
        364.0,
        88.0,
        374.0,
        fill="#79ACF6",
        outline="")

    canvas.create_rectangle(
        68.0,
        196.0,
        71.0,
        374.0,
        fill="#7F7B7B",
        outline="")

    canvas.create_rectangle(
        65.0,
        212.0,
        71.0,
        214.0,
        fill="#807C7C",
        outline="")

    canvas.create_rectangle(
        65.0,
        249.0,
        71.0,
        251.0,
        fill="#807C7C",
        outline="")

    canvas.create_rectangle(
        65.0,
        287.0,
        71.0,
        289.0,
        fill="#807C7C",
        outline="")

    canvas.create_rectangle(
        65.0,
        324.0,
        71.0,
        326.0,
        fill="#807C7C",
        outline="")

    canvas.create_rectangle(
        65.0,
        361.0,
        71.0,
        363.0,
        fill="#807C7C",
        outline="")

    canvas.create_text(
        43.0,
        206.0,
        anchor="nw",
        text="9 am",
        fill="#807C7C",
        font=("FiraSans Bold", 9 * -1)
    )

    canvas.create_text(
        40.0,
        243.0,
        anchor="nw",
        text="12 pm",
        fill="#807C7C",
        font=("FiraSans Bold", 9 * -1)
    )

    canvas.create_text(
        43.0,
        281.0,
        anchor="nw",
        text="3 pm",
        fill="#807C7C",
        font=("FiraSans Bold", 9 * -1)
    )

    canvas.create_text(
        42.0,
        318.0,
        anchor="nw",
        text="6 pm",
        fill="#807C7C",
        font=("FiraSans Bold", 9 * -1)
    )

    canvas.create_text(
        42.0,
        355.0,
        anchor="nw",
        text="9 pm",
        fill="#807C7C",
        font=("FiraSans Bold", 9 * -1)
    )

    canvas.create_text(
        146.0,
        275.0,
        anchor="nw",
        text="Busy",
        fill="#000000",
        font=("FiraSans Bold", 12 * -1)
    )
    canvas.create_line(
        123.20956420898438,
        262.1399841308594,
        141.9803009033203,
        276.9419250488281,
        fill="red",
        width=2)
    run_button = Button(
        window,
        text="Run Tracking",
        command=run_code
    )
    update_button = Button(
        window,
        text="Update Density",
        command=updateDensity
    )
    run_button.place(x=130, y=5)
   # update_button.place(x=130,y=650)
    window.resizable(True, True)
    window.mainloop()

Activate_GUI()

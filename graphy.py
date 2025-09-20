import customtkinter as ctk
import tkinter as tk


def find_equation():
    try:
        X1 = int(coord_x1.get())
        X2 = int(coord_x2.get())
        Y1 = int(coord_y1.get())
        Y2 = int(coord_y2.get())

        print("Point one:", (X1, Y1))
        print("Point two:", (X2, Y2))

        if X2 != X1:
            m = (Y2 - Y1) / (X2 - X1)   # slope
            b = Y1 - m * X1             # intercept
            final_ans = f"y = {m:.2f}x + {b:.2f}"
        else:
            final_ans = f"Vertical line: x = {X1}"

    except Exception as e:
        final_ans = f"Error: {e}"

    answer.configure(text=final_ans)


# Window
main_window = ctk.CTk()
main_window.geometry("700x480")
main_window.title("Graphy.ai")

# UI
info = ctk.CTkLabel(
    main_window,
    text="Insert the coordinates of your graph to find out the equation of the line"
)
info.pack(padx=10, pady=10)

# Input fields
coord_x1 = ctk.CTkEntry(main_window, placeholder_text="Coord x1")
coord_x2 = ctk.CTkEntry(main_window, placeholder_text="Coord x2")
coord_y1 = ctk.CTkEntry(main_window, placeholder_text="Coord y1")
coord_y2 = ctk.CTkEntry(main_window, placeholder_text="Coord y2")

coord_x1.pack(side="left", padx=10, pady=10, anchor="n")
coord_x2.pack(side="right", padx=10, pady=10, anchor="n")
coord_y1.pack(side="left", padx=10, pady=10, anchor="n")
coord_y2.pack(side="right", padx=10, pady=10, anchor="n")

# Button
calc_button = ctk.CTkButton(
    main_window, width=100, height=50, text="Calculate", command=find_equation
)
calc_button.place(relx=0.5, rely=0.3, anchor="center")

# Answer text
answer = ctk.CTkLabel(main_window, text="")
answer.place(relx=0.6, rely=0.3)

# Run
main_window.mainloop()

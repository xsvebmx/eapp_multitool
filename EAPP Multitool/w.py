from customtkinter import *
import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = CTk()
app.geometry("1280x720")

def home_button_event(self):
        self.select_frame_by_name("home")

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
logo = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Gimp.ico")), size=(50, 50))
logo_2 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Calculator.ico")), size=(50, 50))
logo_3 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "FileZilla.ico")), size=(50, 50))

tabview = customtkinter.CTkTabview(app, width=480,height=400)
tabview.grid(row=0, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")
tabview.add("CTkTabview")
tabview.add("Tab 2")
tabview.add("Tab 3")
tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

gipm = customtkinter.CTkButton(tabview.tab("CTkTabview"), corner_radius=0, height=20, border_spacing=0, text="gimp",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=logo, anchor="w", command=home_button_event)
gipm.grid(row=1, column=0, sticky="ew")

home_button = customtkinter.CTkButton(tabview.tab("CTkTabview"), corner_radius=0, height=20, border_spacing=0, text="Calculator",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=logo_2, anchor="w", command=home_button_event)
home_button.grid(row=2, column=0, sticky="ew")

filezilla = customtkinter.CTkButton(tabview.tab("CTkTabview"), corner_radius=0, height=20, border_spacing=0, text="FileZilla",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=logo_3, anchor="w", command=home_button_event)
filezilla.grid(row=3, column=0, sticky="ew")




navigation_frame_label = customtkinter.CTkLabel(tabview.tab("Tab 2"),text=" ", image=logo,compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

#optionmenu_1 = customtkinter.CTkOptionMenu(app, dynamic_resizing=False,values=["Value 1", "Value 2", "Value Long Long Long"])
#optionmenu_1.grid(row=0, column=0, padx=(0, 200), pady=(0, 0))

#combobox_1 = customtkinter.CTkComboBox(tabview.tab("CTkTabview"),values=["Value 1", "Value 2", "Value Long....."])
#combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))


# Runnig an event loop
app.mainloop()
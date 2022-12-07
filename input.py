import customtkinter
import requests
import os


customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title('Weather App')
root.geometry('500x350')

def open_file():
    os.system('weather.py')

def get_data():
    print(entry1.get())

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text='Enter City', font = ('Roboto', 30))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="ex: Miami")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Go", command=lambda:[open_file(),get_data()])
button.pack(pady=12, padx=10)

root.mainloop()
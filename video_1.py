from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# root = Tk()
root = customtkinter.CTk()

root.title('Prolific Code')
# root.iconbitmap('images/codemy.ico')
root.geometry('600x350')


my_button = customtkinter.CTkButton(root, text="Hello world")
my_button.pack(pady=80)


root.mainloop()

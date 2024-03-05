# https://www.youtube.com/watch?v=mwalgzuEfvw
from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# root = Tk()
root = customtkinter.CTk()

root.title('Code by DP Greaves')
root.iconbitmap('C:/gui/python.ico')
root.geometry('550x500')


def submit():
    my_label.configure(
        text=f'Hello {my_entry.get()}, \nyour function call \nis very important to us.\nEngaging ludicrous speed!!')
    my_entry.configure(state="disabled")
    my_button.configure(state="disabled")


def clear():
    my_label.configure(text="")
    my_entry.configure(state="normal")
    my_button.configure(state="normal")
    my_entry.delete(0, END)


my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root, placeholder_text="Enter Your Name", height=50, width=200,
                                  font=("Helvetica", 18), corner_radius=50, text_color="darkblue",
                                  # outer, inner
                                  placeholder_text_color="darkblue", fg_color=("blue", "lightblue"))

my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
my_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=10)


root.mainloop()

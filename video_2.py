# https://www.youtube.com/watch?v=WE1IuPOICxE&list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f&index=3
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


def hello():
    my_label.configure(text=my_button.cget("text"))


my_button = customtkinter.CTkButton(root,
                                    text="Hello world!!!",
                                    command=hello,
                                    height=100,
                                    width=200,
                                    font=("Helvetica", 24),
                                    text_color="black",
                                    fg_color="red",
                                    hover_color="green",
                                    corner_radius=50,
                                    bg_color="white",
                                    border_width=10,
                                    border_color="yellow",
                                    state="normal")


my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)


root.mainloop()

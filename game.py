from tkinter import *
import random
from tkinter import font

secret = random.randint(1, 100)

def check_guess():
    guess = int(entry.get())
    if guess == secret :
        result.config(text= "Congratulations, you've guessed the number!")
    elif guess < secret :
       result.config(text="Your guess is too low.")
    else:
       result.config(text="Your guess is too high.")


# Create a main window
window = Tk()
window.title("Number Guessing Game") # Set the title

custom_font = font.Font(family= "Consolas", size = 12)  # Change size to desired font size
window.option_add("*Font", custom_font)  # Apply custom font to all widgets

# Create widgets
label1 = Label(window, text="Let's play a guessing game! Try to guess a number between 1 and 100.")
entry = Entry(window, width = 50)
entry.insert(0, "Input your guess here (after deleting this text)")
button = Button(window, text="Check", command=check_guess)
result = Label(window, text="")

# Using grid to place widgets
label1.grid(row=0, column=0, columnspan=5)
entry.grid(row=1, column=0)
button.grid(row=1, column=1)
result.grid(row=2, column=0)

# Start the main loop
window.mainloop()

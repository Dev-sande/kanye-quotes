# Tapiwa Sande

from tkinter import *
import requests

# Fetch a quote from the REST API
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

# Create the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Displaying background and text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Hit the button below for quotes", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Button to trigger the get_quote function when clicked
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
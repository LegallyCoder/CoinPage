import tkinter as tk
import json
import requests
import time

window = tk.Tk()
canvas = tk.Canvas(window, width=800, height=600)
window.iconphoto(True, tk.PhotoImage(file="CoinPage.png"))
window.title("CoinPage")
window.geometry("800x600")
options = ["Bitcoin", "Dogecoin", "Etherium"]

label = tk.Label(window, text="Chose a Coin:")
label.pack()

selected_option = tk.StringVar(window)
selected_option.set(options[0])

option_menu = tk.OptionMenu(window, selected_option, *options)
option_menu.pack()


def save_selection():
    selection = selected_option.get()
    if(selection == "Bitcoin"):
        
            key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
            data = requests.get(key)  
            data = data.json()
            label.config(text=f"Bitcoin Price: {data['price']} USD")
            
    if(selection == "Dogecoin"):
        
            key = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT"
            data = requests.get(key)  
            data = data.json()
            label.config(text=f"Dogecoin Price: {data['price']} USD")
            
    if(selection == "Etherium"):
        
            key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
            data = requests.get(key)  
            data = data.json()
            label.config(text=f"Etherium Price: {data['price']} USD")
            
    

button = tk.Button(window, text="Save", width=20, height=5, command=save_selection)
button.pack()
image = tk.PhotoImage(file="CoinPage.png")
canvas.create_image(292, 50, anchor=tk.NW, image=image)
canvas.pack()


window.mainloop()

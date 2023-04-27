import tkinter as tk
import pypokedex
import PIL.Image, PIL.ImageTk
import json
import requests
from io import BytesIO


combat = tk.Tk()
combat.geometry("600x500")
combat.title("Pokedex")
combat.config(padx=10, pady=10)

title_label = tk.Label(combat, text="Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(combat)
pokemon_image.pack()

pokemon_information = tk.Label(combat)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(combat)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

http = requests.Session()

def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    response = http.get(pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.content))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

label_id_name = tk.Label(combat, text="ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(combat, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(combat, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

combat.mainloop()
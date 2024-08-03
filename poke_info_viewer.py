"""
Description:
  Graphical user interface that displays select information about a
  user-specified Pokemon fetched from the PokeAPI

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk, messagebox
from poke_api import get_pokemon_info

# Function to fetch and display Pokémon info
def get_info():
    poke_name = enter_name.get().strip().lower()
    if not poke_name:
        return
    
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        height_val["text"] = f"{poke_info['height']} dm"
        weight_val["text"] = f"{poke_info['weight']} hg"
        
        types_str = ", ".join([type_data["type"]["name"].capitalize() for type_data in poke_info["types"]])
        type_val["text"] = types_str    

        hp_bar["value"] = poke_info["stats"][0]["base_stat"]
        att_bar["value"] = poke_info["stats"][1]["base_stat"]
        def_bar["value"] = poke_info["stats"][2]["base_stat"]
        spatt_bar["value"] = poke_info["stats"][3]["base_stat"]
        spdef_bar["value"] = poke_info["stats"][4]["base_stat"]
        speed_bar["value"] = poke_info["stats"][5]["base_stat"]
    else:
        messagebox.showerror(title="Error", message=f"Unable to fetch information for {poke_name} from the PokeAPI.")
        return

# Create the main window
root = Tk()
root.title("Pokemon Information Viewer")
root.resizable(False, False)

# Create the frames
frame_input1 = ttk.Frame(root)
frame_input1.grid(row=0, column=0, columnspan=2, pady=(20,10))

frame_info1 = ttk.LabelFrame(root, text="Info")
frame_info1.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

frame_stats1 = ttk.LabelFrame(root, text="Stats")
frame_stats1.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

# Populate the user input frame with widgets
lbl_name = ttk.Label(frame_input1, text='Pokemon Name')
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

enter_name = ttk.Entry(frame_input1)
enter_name.grid(row=0, column=1, padx=5, pady=10)

input_btn = ttk.Button(frame_input1, text="Get Info", command=get_info)
input_btn.grid(row=0, column=2, padx=(5, 10), pady=10)

# Populate the info frame
height_lbl = ttk.Label(frame_info1, text="Height:")
weight_lbl = ttk.Label(frame_info1, text="Weight:")
type_lbl = ttk.Label(frame_info1, text="Type:")

height_lbl.grid(row=0, column=0, sticky="E", padx=(10, 5), pady=(10, 5))
weight_lbl.grid(row=1, column=0, sticky="E", padx=(10, 5), pady=5)
type_lbl.grid(row=2, column=0, sticky="E", padx=(10, 5), pady=(5, 10))

height_val = ttk.Label(frame_info1, width=20)
weight_val = ttk.Label(frame_info1, width=20)
type_val = ttk.Label(frame_info1, width=20)

height_val.grid(row=0, column=1, sticky="W", padx=(5, 10), pady=(10, 5))
weight_val.grid(row=1, column=1, sticky="W", padx=(5, 10), pady=5)
type_val.grid(row=2, column=1, sticky="W", padx=(5, 10), pady=(5, 10))

# Populate the stats frame 
hp_lbl = ttk.Label(frame_stats1, text="HP:")
att_lbl = ttk.Label(frame_stats1, text="Attack:")
def_lbl = ttk.Label(frame_stats1, text="Defense:")
spatt_lbl = ttk.Label(frame_stats1, text="Special Attack:")
spdef_lbl = ttk.Label(frame_stats1, text="Special Defense:")
speed_lbl = ttk.Label(frame_stats1, text="Speed:")

hp_lbl.grid(row=0, column=0, sticky="E", padx=(10, 5), pady=(10, 5))
att_lbl.grid(row=1, column=0, sticky="E", padx=(10, 5), pady=5)
def_lbl.grid(row=2, column=0, sticky="E", padx=(10, 5), pady=5)
spatt_lbl.grid(row=3, column=0, sticky="E", padx=(10, 5), pady=5)
spdef_lbl.grid(row=4, column=0, sticky="E", padx=(10, 5), pady=5)
speed_lbl.grid(row=5, column=0, sticky="E", padx=(10, 5), pady=(5, 10))

MAX_STAT = 255
BAR_LENGTH = 200
hp_bar = ttk.Progressbar(frame_stats1, maximum=MAX_STAT, length=BAR_LENGTH)
att_bar = ttk.Progressbar(frame_stats1, maximum=MAX_STAT, length=BAR_LENGTH)
def_bar = ttk.Progressbar(frame_stats1, maximum=MAX_STAT, length=BAR_LENGTH)
spatt_bar = ttk.Progressbar(frame_stats1, maximum=MAX_STAT, length=BAR_LENGTH)
spdef_bar = ttk.Progressbar(frame_stats1, maximum=MAX_STAT, length=BAR_LENGTH)
speed_bar = ttk.Progressbar(frame_stats1, maximum=MAX_STAT, length=BAR_LENGTH)

hp_bar.grid(row=0, column=1, padx=(5, 10), pady=(10, 5))
att_bar.grid(row=1, column=1, padx=(5, 10), pady=5)
def_bar.grid(row=2, column=1, padx=(5, 10), pady=5)
spatt_bar.grid(row=3, column=1, padx=(5, 10), pady=5)
spdef_bar.grid(row=4, column=1, padx=(5, 10), pady=5)
speed_bar.grid(row=5, column=1, padx=(5, 10), pady=(5, 10))

root.mainloop()

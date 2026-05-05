import tkinter as tk
import tkintermapview as tkm

root = tk.Tk()
root.title('R4Sport')
header = tk.Frame(root, bg="#000000", height=80)
header.pack(side='top', fill='x')
container = tk.Frame(root)
container.pack(fill='both',expand=True)
sidebar = tk.Frame(container,bg="#242424", width=250)
sidebar.pack(side="left",fill="y")
selected = tk.StringVar(value="OSM")
toolbar = tk.Frame(container, bg="#606060", height=40)
toolbar.pack(side='top', fill='x')
dropdown = tk.OptionMenu(toolbar, selected, "OSM", "Satellite")
dropdown.config(bg="#ff0000", fg="#ffffff")
dropdown.pack(pady=5,padx=5,side='right')
map_area = tk.LabelFrame(container)
map_area.pack(pady=10, padx=10, fill='both',expand=True)
map_widget = tkm.TkinterMapView(map_area)
map_widget.pack(fill='both',expand=True)

def change_map_tile(*args):
    choice = selected.get()
    if choice == "OSM":
        map_widget.set_tile_server(
            "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
        )

    elif choice == "Satellite":
        map_widget.set_tile_server(
            "https://mt0.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
        )

selected.trace_add("write", change_map_tile)
root.mainloop()
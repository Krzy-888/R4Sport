import tkinter as tk
import tkintermapview as tkm
root = tk.Tk()
root.title('R4Sport')
toolbar = tk.Frame(root, bg="grey", height=40)
toolbar.pack(side='top', fill='x')
selected = tk.StringVar(value="OSM")
dropdown = tk.OptionMenu(toolbar, selected, "OSM", "Satellite")
dropdown.pack(pady=5,padx=5,side='right')
map_area = tk.LabelFrame(root)
map_area.pack(pady=20, padx=20, fill='both',expand=True)
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
# text_area = tk.Text(root, wrap=tk.WORD)
# text_area.pack(pady=10, padx=10, fill='both', expand=True)
root.mainloop()
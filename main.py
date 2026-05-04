import tkinter as tk
root = tk.Tk()
root.title('R4Sport')
toolbar = tk.Frame(root, bg="grey", height=40)
toolbar.pack(side='top', fill='x')
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(pady=10, padx=10, fill='both', expand=True)
root.mainloop()
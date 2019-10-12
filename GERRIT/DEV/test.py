import tkinter as tk
root = tk.Tk()
root.title("Welcome Message")
label = tk.Label(root, text="Welcome Praneeth Alaghari")
label.pack(side="top", fill="both", expand=True, padx=50, pady=50)
button = tk.Button(root, text="OK", command=lambda: root.destroy())
button.pack(side="bottom", fill="none", expand=True)
root.mainloop()
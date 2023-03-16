import tk as tk
from tk import messagebox, filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad")
        self.file_path = None

        # Create Text Widget
        self.text = tk.Text(self.master, wrap="word")
        self.text.pack(expand=True, fill="both")

        # Create Menu Bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Create File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.file_path = None

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", f.read())
            self.file_path = file_path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as f:
                f.write(self.text.get("1.0", tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text.get("1.0", tk.END))
            self.file_path = file_path

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()

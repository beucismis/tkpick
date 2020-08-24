import tkinter as tk


__version__ = "1.8.0"
__author__ = "adlgrbz"
__contact__ = "adlgrbz@tutamail.com"
__source__ = "https://github.com/adlgrbz/Tkpick"


class About(tk.Toplevel):
    def __init__(self):
        super().__init__()

    def _init_window(self, icon) -> None:
        self.title(type(self).__name__)
        self.resizable(0, 0)
        self.wm_iconphoto(self._w, icon)

        tk.Label(
            self, text=f"Tkpick {__version__}", compound=tk.LEFT, image=icon
        ).pack(padx=5, pady=5)

        content = (
            f"Author: {__author__}\n"
            f"Contact: {__contact__}\n\n"
            f"Source: {__source__}"
        )
        tk.Label(self, text=content, padx=5, pady=5, relief=tk.RIDGE).pack()

        tk.Button(self, text="Close", command=lambda: self.destroy()).pack(
            padx=5, pady=5, side=tk.RIGHT
        )
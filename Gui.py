import tkinter as tk
from tkinter import filedialog
from tkinter import font

# debug
from tkinter import messagebox


class Gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("mangalek Donload")
        self.geometry('480x480')
        
        font_title = font.Font(family="Helvetica", weight="bold" ,size=18)
        font_ask = font.Font(family='arial',weight="normal",size=12)
        
        self.label_titl = tk.Label(self , 
                                text="Hello to the manga \n downloader from mangalek",
                                bg="lightgreen",
                                font=font_title,
                            )
        self.label_titl.pack()
        
        self.label_ask_name = tk.Label(self,text="give the name of the manga",font=font_ask)
        self.input_ask_name = tk.Entry(self)
        self.button_submit = tk.Button(self, text="Submit", command=self.submit_name_manga)
        
        self.label_ask_name.pack()
        self.input_ask_name.pack()
        self.button_submit.pack()
        
    def askdirectory(self):
        self.download_Path = filedialog.askdirectory()
        
    def submit_name_manga(self):
        self.manga = self.input_ask_name.get()
        self.manga = self.manga.strip().replace(" ", "-")


if __name__ == "__main__":
    window = Gui()
    window.mainloop()
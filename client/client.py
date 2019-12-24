import config
import socket
import tkinter as tk
import tkinter.messagebox

class Application():
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)

    def creat_widgets(self):
        img = tk.PhotoImage(file = 'made_by_python.gif')
        self.label1 = tk.Label(self.root, text = 'Name:')
        self.label1.grid(row=0, column=0, sticky=tk.E, pady = 10)
        self.entry1 = tk.Entry(self.root)
        self.entry1.grid(row=0,column=1)
        self.button1 = tk.Button(self.root, text = 'Check in', command = self.send)
        self.button1.grid(row=1, column=1, sticky = tk.E, pady = 0)
        self.imgwidget = tk.Label(image = img)
        self.imgwidget.image = img
        self.imgwidget.grid(row=0,column=2,
                            sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
        self.about = tk.Button(self.root, text = 'About', command = show_about)
        self.about.grid(row = 1, column = 2)
    def send(self):
        name = self.entry1.get()
        send_data(name)


def send_data(name):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(config.IP_PORT)
    except socket.error as error:
        raise error
    s.send(name.encode())
    s.close()
def show_about():
    tkinter.messagebox.showinfo('About', "This is GUI window is totally handmade.")
def main():
    root = tk.Tk()
    app = Application(root, 'Check In')
    app.creat_widgets()
    root.mainloop()

if __name__ == '__main__':
    main()

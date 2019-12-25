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
    STATUS = s.recv(1024)
    STATUS = int.from_bytes(STATUS, byteorder='big')
    if STATUS == 1:
        show_messagebox('Failure', "You've already checked.")
    elif STATUS == 0:
        show_messagebox('Success', 'Welcome.')
    elif STATUS == 2:
        show_messagebox('Failure', 'No such a name, please check the text box.')


    s.close()
def show_about():
    tkinter.messagebox.showinfo('About', "This GUI window is totally handmade.")

def show_messagebox(title, msg):
    tkinter.messagebox.showinfo(title, msg)
def main():
    root = tk.Tk()
    app = Application(root, 'Check In')
    app.creat_widgets()
    root.mainloop()

if __name__ == '__main__':
    main()

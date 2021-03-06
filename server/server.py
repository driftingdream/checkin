import socket
from datetime import datetime
import xlwt

STATUS = 0
'''
define the status whether the information is required. The value: 0 is required, 1 is not.
'''
LOCALIP_PORT = ('127.0.0.1', 6666)

class STATUS():
    def __init__(self):
        self.value = 0
        self.expect = 'm'
        '''
        self.expect present as a flag, 'm' means morning, 'a' means afternoon.
        '''
    def get(self):

        return self.value

def check_name(name):
    if datetime.now().weekday()>=0 and datetime.now().weekday()<=4:
        with open('./namelist', 'r') as f:
            for line in f.readlines():
                if line == name:
                    return 0
            return 2

    else:
        return 3
'''
the value of return:
                    0: success,
                    2: failure, no such a name,
                    3: failure: wrong time.
'''

def commandhandler(line):
    parts = line.split(' ', 1)
    if parts[0] == ' ':
        return 3 #error
    else:
        meth = parts[0]
        name = parts[1]
        if meth == 'checkin':
            checkin(name)
        elif meth == 'checkout':
            checkout()
        else:
            return 2 #method not found
    return 0


def checkin(name):
    if check_name(name) == 0:
        checkin_excel_wbk = wlwt.Workbook()
        sheet = checkin_excel_wbk.add_sheet('checkin')
        sheet.



def main():
    global STATUS
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(LOCALIP_PORT)
        s.listen()
        print('Waiting for connection')
    except socket.error as msg:
        raise msg
    while True:
        sock, addr = s.accept()
        data = sock.recv(1024)
        data = data.decode()
        commandhandler(data)


        """
        if STATUS:
            sock.sendall(bytes([STATUS]))
        else:
            if check_name(data) == 1:
                sock.sendall(bytes([STATUS]))
                STATUS = 1
            elif check_name(data) == 2:
                sock.sendall(bytes([2]))
        """




if __name__ == '__main__':
    main()

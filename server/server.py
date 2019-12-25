import socket


STATUS = 0
'''
define the status whether the information is required. The value: 0 is required, 1 is not.
'''
LOCALIP_PORT = ('127.0.0.1', 6666)

def check_name(name):
    pass

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
        if STATUS:
            sock.sendall(bytes([STATUS]))
        else:
            if check_name(data) == 1:
                sock.sendall(bytes([STATUS]))
                STATUS = 1
            elif check_name(data) == 2:
                sock.sendall(bytes([2]))




if __name__ == '__main__':
    main()

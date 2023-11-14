import socket
import configparser


def server_program():
    config = configparser.ConfigParser()
    config.read('config.ini')

    host = config['DEFAULT']['Host']
    port = int(config['DEFAULT']['Port']) # initiate port no above 1024
    listeners_amount = int(config['DEFAULT']['Listeners_amount'])

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(listeners_amount)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    data = conn.recv(1024)
    print(data)
    conn.send(f'{data.decode("utf-8")}, Hello hello!'.encode())
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
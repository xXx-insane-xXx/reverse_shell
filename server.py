import socket
import sys


# Create a Socket (Connect two computers)
def create_socket():

    # Sometimes socket might have problem getting created
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print(f"Socket creation error : {msg}")


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s   

        print(f"Binding the port {port}")

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print(f"Socket binding error {msg}.\nRetrying....")
        bind_socket()


# Establish connection with a client (socket must be listening)
def socket_accept():

    # Gives obj of a connection and list (ip and port of client)
    conn, addr = s.accept() # Wont move to the next line until acceptance is completed
    print(f"Connection has been established! | IP: {addr[0]} | Port: {addr[1]}")
    
    #send_command(conn)
    
    conn.close()
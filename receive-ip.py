# runs on linode

import socket


def receive_connection():
    FILE_NAME = "home-ip.txt"

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set up host and port
    host = ""  # Leave it empty to accept connections from any IP address
    port = 1100

    # Bind the socket to the host and port
    s.bind((host, port))

    # Listen for incoming connections
    s.listen(1)
    print("Waiting for a connection...")

    # Accept a connection
    conn, addr = s.accept()
    print("Connected with", addr)
    with open(FILE_NAME, "r") as f:
        address_on_file=f.readline().strip()
        if (address_on_file!=addr[0])

    # Print the IP address it came from
    print("IP Address:", addr[0])

    # Close the connection
    conn.close()


if __name__ == "__main__":
    # Call the function to receive the connection
    receive_connection()

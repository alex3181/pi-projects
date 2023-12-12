# Runs on home raspberry pi

import socket, time


def run():
    LINODE_SERVER = "23.92.20.219"
    LINODE_SERVER = "127.0.0.1"

    LINODE_PORT = 1100

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((LINODE_SERVER, LINODE_PORT))
        except:
            pass
        time.sleep(30)


if __name__ == "__main__":
    run()

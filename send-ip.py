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


<<<<<<< HEAD
if __name__ == "__main__":
    run()
=======
while (True):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((LINODE_SERVER, LINODE_PORT))    
    except:
        print (f"Unable to connect to {LINODE_SERVER}:{LINODE_PORT}")
    time.sleep(300)
>>>>>>> 3857931f6d7728d9b316582c8d1cfa197817e876

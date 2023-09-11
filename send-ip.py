import socket, time

LINODE_SERVER="23.92.20.219"

LINODE_PORT=1100

while (True):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((LINODE_SERVER, LINODE_PORT))    
    except:
        print (f"Unable to connect to {LINODE_SERVER}:{LINODE_PORT}")
    time.sleep(300)
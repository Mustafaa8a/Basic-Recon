import socket

def bannerGrab(ip,port):
    try:
        # SOCK_STREAM. AF_INET refers to the address ipv4
        # The SOCK_STREAM means connectionoriented TCP protocol
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # Max time to connect is 5
        s.settimeout(5)

        # Try to connect
        s.connect((ip,port))

        # Send request 
        s.sendall(b"GET / HTTP/1.1\r\n\r\n")

        # Receive banner
        banner = s.recv(1024)

        if banner:
            print(f"Banner: {banner.decode('utf-8', errors='ignore').strip()}")
        else : print("Did not recieve a banner")

        s.close()

    except socket.timeout:
        print("Time out")
    except ConnectionRefusedError:
        print("Connection refused")
    except Exception as e:
        print(f"Error: {e}")

if __name__=="__main__":
    ip = input("Enter ip address: ")
    port = int(input("Enter port number: "))
    bannerGrab(ip,port)

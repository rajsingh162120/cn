import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, UDP Server!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("Message:", MESSAGE.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.close()

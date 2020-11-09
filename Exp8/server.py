import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.bind(('localhost',12345))
  while True:
    data, addr = s.recvfrom(1024)
    print('Connection w address',addr)
    s.sendto(b'',addr)
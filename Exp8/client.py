import socket
from time import time

addr = socket.getaddrinfo(
  'localhost', 12345,
  socket.AF_INET, socket.SOCK_DGRAM)[0]
with socket.socket(*addr[:3]) as s:
  s.connect(addr[4])
  for i in range(500):
    t1 = time()
    s.send(b'')
    t2 = time()
    s.recv(1024)
    t3 = time()
    if i % 100 == 0:
      print('{:.3f}ms {:.3f}ms'.format((t2 - t1) * 1000, (t3 - t2) * 1000))

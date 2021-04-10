#Mock socket program with multithreading
import threading
import time

PORT = 5050
SERVER = "195.888.756"
ADDR = (SERVER, PORT)

names = ["steven", "jon", "sarah"]
address = [("195.888.7.56", 4040), ("192.168.1.26", 3030), ("196.888.1.56", 2020)]
messages = ["steven: Sent a concern", "jon: Ordered a package", "sarah: Making a transaction"]

def handle_client(addr, i):
  print(f"[NEW CONNECTION] {addr} connected.")
  print("I am waiting for a message from " + names[i])

  time.sleep(3)

  msg = client_send(i)
  print(f"[{addr}] {msg}")
  print("Msg received")


def server_accept(i):
  return address[i]  

def start():
  print(f"[LISTENING] Server is listening on {SERVER}")
  i = 0
  while i < 3:
    #time consuming as it waits for a cient server to accept
    time.sleep(1)
    addr = server_accept(i)

    thread = threading.Thread(target=handle_client, args=(addr, i))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    i += 1

def client_send(i):
    return messages[i]

t1 = time.perf_counter()
print("[STARTING] server is starting...")
start()
t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
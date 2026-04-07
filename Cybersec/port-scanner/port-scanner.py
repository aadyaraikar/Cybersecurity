import socket
import sys
import time
import threading

usage = "python3 port-scanner.py TARGET START_PORT END_PORT"

if(len(sys.argv)!=4):
    print(usage)
    sys.exit()

print("-"*70)
print("Port Scanner")
print("-"*70)

start_time = time.time()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error.")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target", target)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((target, port))
    if(conn == 0):
        print("port {} is OPEN".format(port))
    s.close()

for thread in range(start_port, end_port+1):

    thread = threading.Thread(target = scan_port, args = (thread,))
    thread.start()

import sys
import socket
import datetime
import time
from threading import Thread

target_url = input("[+] Enter Target URL (e.g. example.com) : ")
port_range = input("[+] Enter Ports to scan (e.g. 1-65565) : ")
open_ports = []
closed_ports = []
threads = []
print("")
start_time = time.time()
print("[+] Determining Target IP...")

target_ip = socket.gethostbyname(str(target_url))

ports = port_range.split('-')

print("[+] Scanning URL: " + str(target_url) + " (" +str(target_ip)+ ") | Ports: " + str(port_range))

def scan(port):
    s = socket.socket()
    result = s.connect_ex((target_ip, port))
    if result == 0:
        open_ports.append(port)
        print(('[+] Port ' + str(port)) + ': open')
        s.close()
    else:
        closed_ports.append(port)
        print(('[-] Port ' + str(port)) + ': closed')
        s.close()

for i in range(int(ports[0]), int(ports[1]) + 1):
    print(">> Scanning Port: " + str(i))
    t = Thread(target=scan, args=(i,))
    threads.append(t)
    t.start()

[x.join() for x in threads]

print("Open Port(s) " + str(open_ports))
elapsed_time = time.time() - start_time
print('Completed Scan at: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
print('Elapsed Time: ' + str(elapsed_time) + ' seconds')
print('Portscanner by PengSec, Report for ' + str(target_url) + ' (' +str(target_ip)+ ')')

import socket #communicate w others in TCP & UDP
import termcolor #to print statement in diff colors

#func for scan multiple port
def Sccan(targets, ports):
        for port in range(1, ports):
            Scan_port(targets, port)

#func for connect and check
def Scan_port(ipadress, port):
        try:    
            sock = socket.socket()
            sock.connect(ipadress, port)
            print("[+] Port OPEN " + str(port))
            sock.close()
        except:
            pass

targets = input("[?] Enter Target to Scan ") 
ports = input("[?] Enetr number of Ports to Scan ")    
if ',' in targets:
    print("Scanning multiple ports:: ")
    for ip_adr in targets.split(','):
         
import socket #communicate w others in TCP & UDP
import termcolor #to print statement in diff colors

#func for scan multiple port
def Sccan(targets, ports):
        print("\n" + "Starting scan for" + str(targets))    
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

targets = input("[?] Enter Targets to Scan (split by ',' :  ) ") 
ports = int(input("[?] Enetr how many Ports to Scan : "))    
if ',' in targets:
    print(termcolor.colored(("Scanning multiple ports:: "), 'green'))
    for ip_adr in targets.split(','):
        Sccan(ip_adr.strip(' '), ports)
else:
    Scan_port(targets, ports)
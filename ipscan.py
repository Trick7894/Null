import nmap
import socket
from prettytable import PrettyTable
import time


def port_scanner(ip, start_port, end_port, protocol="tcp"):
    table = PrettyTable()
    sttime = time.time()
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == "tcp" else socket.SOCK_DGRAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service_name = socket.getservbyport(port, protocol)
            nm = nmap.PortScanner()
            nm.scan(ip, port, port)
            for host in nm.all_hosts():
                os_name = nm[host].os_nmap.os_class.name
                table.field_names = ["Status", "Name ports", "Protocol", "OS"]
                table.add_row(["Port open", port, service_name, os_name])

        else:
            pass
        sock.close()
    print(colored(table, 'magenta'))
    endtime = time.time()
    timeerscan = endtime - sttime
    print(colored(f"Scanning time: {timeerscan:.2f} s", 'yellow'))


ip = input("Enter IP : ")
start_port = int(input("Enter port: "))
end_port = int(input("Enter port: "))
port_scanner(ip, start_port, end_port)
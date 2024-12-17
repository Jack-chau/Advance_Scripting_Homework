import nmap
target_ip = '192.168.254.144'
target_ports = '21,22,80'

namp_scanner = nmap.PortScanner()
namp_scanner.scan( target_ip, target_ports, ' -sS -O', sudo = True )

print( '\n' )
open_ports = namp_scanner[ target_ip ][ 'tcp' ].keys()
print( open_ports )
from telnetlib import Telnet

'''Basic example... single host'''

HOST = '192.168.254.144'
USERNAME = 'jackchau'
PASSWORD = 'Jack0303'

# Return logged in users
def show_users_telnet():
    tn = Telnet( HOST )
    tn.read_until( b'jackchau login:') #read until respond # b for byte
    tn.write( USERNAME.encode( 'ascii' ) + b'\n' ) #encode('ascii') turn USERNAME to byte

    tn.read_until( b'Password: ')
    tn.write( PASSWORD.encode( 'ascii' ) + b'\n' )

    tn.write( b'hostname\n' )
    tn.write( b'exit\n' )
    stdout = tn.read_all().decode( 'utf-8' )
    print( stdout )

show_users_telnet()



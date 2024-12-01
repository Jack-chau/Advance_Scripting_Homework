from telnetlib import Telnet
#Config
HOST = '127.0.0.1'
USERNAME = 'JackChau'
PASSWORD = 'Jack0303'

def main( ):
#Telnet to host
    with Telnet( HOST ) as tn:
        try:
            tn.read_until( b'Jackchau login: ') #b'' to byte
            # Enter username
            tn.write( USERNAME.encode( 'ascii' ) + '\n' ) #encode USERNAME to telnet readable format
            # Enter password
            tn.read_until( b'Password: ')
            tn.write( PASSWORD.encode( 'ascii' ) + b'\n' )
            '''
            #Check user logined
            #tn.write( b'hostname\n')
            #stdout = tn.read_all( ).decode( 'utf-8' )
            '''
            # List user who can be remote connect
            tn.write( b"cat /etc/passwd | grep /bin/zsh | cut -d ':' -f 1 ")

        except :
            print( 'Cannot connect' )

if __name__ == "__main__":
    main()
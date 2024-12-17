from ftplib import FTP

HOST = '192.168.254.144'
USER = 'jackchau'
PASSWORD = 'Jack0303'

with FTP( HOST ) as ftp :
    ftp.login( user=USER, passwd=PASSWORD )
    print( ftp.getwelcome() )
    '''
    print( ftp.pwd() )
    ftp.cwd( '/etc' )
    print( ftp.dir() )
    '''
    '''
    # Retrieve
    with open ( 'test.txt', 'wb' ) as f : #test.txt is the new name you retrieve locally
        ftp.retrbinary( 'RETR ' + '/home/jackchau/Desktop/ftp/mytest.txt', f.write, 1024 )
    '''
    # Send
    with open( 'myupload.txt', 'rb' ) as f:
        ftp.storbinary( 'STOR ' + '/home/jackchau/Desktop/ftp/killZombie.txt', f )

    ftp.quit()
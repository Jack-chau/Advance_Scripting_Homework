import paramiko

HOST = '192.168.254.144'
USER = 'jackchau'
PASSWORD = 'Jack0303'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect( HOST, username=USER, password=PASSWORD, look_for_keys=False, allow_agent=False )

stdin, stdout, stderr = ssh.exec_command( 'cat /etc/passwd' )
for line in stdout :
    print( line )
ssh.close()
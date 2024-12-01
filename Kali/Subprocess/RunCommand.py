import subprocess

#subprocess.run('ls -l', shell=True)
#p1 = subprocess.run( ['ls', '-la'], capture_output=True, text=True ) #completed process object add in p1
#print( p1.args )
#print( p1.returncode ) #print err
#print( p1.stdout.decode() ) #capture output (decode convert output to string)
#print( p1.stdout ) #add text=True
# p1 = subprocess.run( ['ls', '-la'], stdout=subprocess.PIPE, text=True )
# print( p1.stdout )

#save to a file
# with open( 'output.txt', 'w' ) as f :
#     p1 = subprocess.run( [ 'ls', '-la' ], stdout=f, text=True )

# p1 = subprocess.run( ['ls', '-la', 'fakefile'], capture_output=True, text=True, check=True )
# print( p1.returncode )
# print( p1.stderr )

# if p1.returncode != 0 :
#     print( p1.stderr )
#Ignore error
p1 = subprocess.run( ['cat', 'test.txt'], capture_output=True, text=True )
#print( p1.stdout )

p2 = subprocess.run( ['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout )
print( p2.stdout )
import hashlib
import time 

# set start timer
start = time.perf_counter()

# Initiation
hashed_list = list()
my_password = '9bff9f1f77ae1cd58a83bc38e7161808'

# Read wordlist file
file = open( 'wordlist.txt', 'r' )
word_list = file.readlines()

# Use md5 algorithm
md5_hash = hashlib.md5()

# brute force password
for hash in word_list :
    #hash = hash.rstrip('\n')
    md5_hash.update( hash.encode( 'utf-8' ) )
    hashed_line = md5_hash.hexdigest()
    if hashed_line == my_password :
        print( hashed_line )
        break
finish = time.perf_counter()

print( f"Finished in { round( finish - start, 2 ) } second(s).")
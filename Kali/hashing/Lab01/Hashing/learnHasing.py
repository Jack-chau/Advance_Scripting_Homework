import hashlib

# print( hashlib.algorithms_available ) # shows hash function available in hashlib
# print( hashlib.algorithms_guaranteed ) # shows hash function available in your OS
"""
h = hashlib.sha256()
h.update( b'FuckYou' )

print( h.digest() ) #byte
print( h.hexdigest() ) #hax(Recommended)
"""
correct_password = "ILoveYouNora"
h = hashlib.new( "SHA256" )
h.update( correct_password.encode() )
password_hash = h.hexdigest()
print( password_hash )

user_input = "ILoveNora"
h = hashlib.new( 'SHA256' )
h.update( user_input.encode() )
user_password = h.hexdigest()
print( user_password ) # The hash is not the same( password wrong i)

# example01-telnetlib.py
import sys
import telnetlib

hostip = '192.168.254.144'
user = "jackchau"
password = "Jack0303"
tn = telnetlib.Telnet(hostip)
tn.read_until(b"jackchau login:")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
    tn.write(b"hostname\n")
    tn.write(b"exit\n")
    output = tn.read_all().decode("ascii")
    print(output)
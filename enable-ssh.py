import getpass
import telnetlib

user = input('Enter telnet username: ')
password = getpass.getpass()

f = open('devices')

for IP in f:
    IP=IP.strip()
    print ('Enabiling SSH on ' + (IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b"enable\n")
    tn.write(b"\n")
    tn.write(b'config t\n')
    tn.write(b"username netadmin pass Tr1D3nt!!!\n")
    tn.write(b"username netadmin priv 15\n")
    tn.write(b"line vty 0 4\n")
    tn.write(b"login local\n")
    tn.write(b"transport input all\n")
    tn.write(b"ip domain-name cisco.com\n")
    tn.write(b"crypto key generate rsa\n")
    tn.write(b"1024\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")

print(tn.read_all().decode('ascii'))

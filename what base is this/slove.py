import socket
from  pwn import *
import re


def main():
    s = remote('2018shell.picoctf.com', 14390)
    binary_ans=''
    binary = s.recvuntil('word.')
    print binary
    data = re.findall(r'(\d+)',binary)
    for i in data:
        binary_ans += chr(int(i,2))
    print 'SENDING > ' + binary_ans
    s.sendline(binary_ans)

    hexa = s.recvuntil('word.')
    print hexa
    hexa = re.findall(r'([0-9a-f]+) as ', hexa)[0]
    hex_ans = hexa.decode('hex')
    print 'SENDING > ' + hex_ans
    s.sendline(hex_ans)

    octal = s.recvuntil('word.')[2:]
    print octal

    octal = re.findall(r'[0-9]+', octal)

    ans = ''
    for i in octal:
                ans += chr(int(i, 8))

    print 'SENDING > ' + ans
    s.sendline(ans)

    print s.recvuntil('}\n')

    s.close()



main()

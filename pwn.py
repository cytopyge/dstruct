from pwn import *
# https://github.com/Gallopsled/pwntools

command = "sudo dd if=/dev/urandom bs=4M count=`sudo blockdev --getsize64 /dev/sda` iflag=count_bytes | pv -n -s `sudo blockdev --getsize64 /dev/sda` | sudo dd of=/dev/sda bs=4M conv=notrunc,noerror 2>&1"


sh = process('/bin/sh')

# sh.sendline(command)

sh.sendline('sleep 3; echo hello world;')
sh.recvline(timeout=1)

# sudo dd if=/dev/urandom bs=4M count=`sudo blockdev --getsize64 /dev/sda` iflag=count_bytes | pv -n -s `sudo blockdev --getsize64 /dev/sda` | sudo dd of=/dev/sda bs=4M conv=notrunc,noerror 2>&1

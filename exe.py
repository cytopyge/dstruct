import subprocess
import time
import sys
# from subprocess import call
# time.sleep(3)
print(sys.argv[1])

def dstruct(dd_of):
    dd_if = '/dev/urandom'
    dd_bs = '1M'
    dd_status = 'progress'
    dd_command = ['dd', 'if=' + dd_if, 'of=' + dd_of, 'bs=' + dd_bs, 'status=' + dd_status]


    #sudo dd if=/dev/urandom bs=4M count=`sudo blockdev --getsize64 /dev/sda` iflag=count_bytes | pv -n -s `sudo blockdev --getsize64 /dev/sda` | sudo dd of=/dev/sda bs=4M conv=notrunc,noerror 2>&1


    print('ERAWQER')
    # while dd_command is running ask pv for progress percentage
    # dd_progress = call(dd_command)
    p = subprocess.Popen(dd_command,stdout=out_fd)
    while True:
        print(">>>>")
        print(p.communicate()[0])

dstruct(sys.argv[1])

# dstruct
destruct data on devices

# installing libs
```
sudo apt-get update
sudo apt-get install python-dev python-rpi.gpio

pip install adafruit-ws2801
```

```
python test_led.py
```


# installing pwntools 
```
https://github.com/Gallopsled/pwntools
```


```
sudo dd if=/dev/urandom bs=4M count=`sudo blockdev --getsize64 /dev/sda` iflag=count_bytes | pv -n -s `sudo blockdev --getsize64 /dev/sda` | sudo dd of=/dev/sda bs=4M conv=notrunc,noerror 2>&1
```

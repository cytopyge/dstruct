import subprocess
import time
import pyudev

context = pyudev.Context()
path = pyudev.Devices.from_sys_path

def wipe(dev_id):
    subprocess.Popen(["python", "exe.py", dev_id], stdout=subprocess.PIPE)
    # print p.communicate()[0]

#[TEST] def enumerate(device.device_node)
def getDevices():
    output = []
    for device in context.list_devices(subsystem='block'):
      # if 'ID_FS_TYPE' in device:
        if device.device_node[5:7] == 'sd':
          # set dd parameters; input file, output file, block size, status
          print(device.device_node)
          dd_of = device.device_node
          output.append(dd_of)
    return output

# give devices (list)
devs = getDevices()
print(devs)
wipe(devs[0])

# time.sleep(5)
# [TODO] tmpDev = getDevices()
#[TODO] monitoring on UUID or PUID

while True:
    print("still there")
    #[TODO] getDevices()
    time.sleep(5)

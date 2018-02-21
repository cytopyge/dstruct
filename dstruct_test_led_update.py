import pyudev
from subprocess import call

context = pyudev.Context()

path = pyudev.Devices.from_sys_path

#[TEST] def enumerate(device.device_node)
def enumerate():
    output = []
    for device in context.list_devices(subsystem='block'):
      if 'ID_FS_TYPE' in device:
        if device.device_node[5:7] == 'sd':
          # set dd parameters; input file, output file, block size, status
          print(device.device_node)
          dd_of = device.device_node
          output.append(dd_of)
    return output

def destruct(dd_of):
          print(device.sys_name)
          #[TODO] led update
          dd_command = ['dd', 'if=' + dd_if, 'of=' + dd_of, 'bs=' + dd_bs, 'status=' + dd_status]
          while call(dd_command):
            # while dd_command is running ask pv for progress percentage
            dd_progress = call(dd_command + ' | pv -n')
            print(dd_progress)
            # use dd_progress for led status
          print('completed')
          exit

print(enumerate()[0])

#[TEST]END

# enumerate at startup
# for device in context.list_devices(subsystem='block'):
#   if 'ID_FS_TYPE' in device:
#     if device.device_node[5:7] == 'sd':
#       # set dd parameters; input file, output file, block size, status
#       dd_if = '/dev/urandom'
#       dd_of = device.device_node
#       dd_bs = '1M'
#       dd_status = 'progress'
#
#       print(device.sys_name)
#       call(['dd', 'if=' + dd_if, 'of=' + dd_of, 'bs=' + dd_bs, 'status=' + dd_status])
#       print('completed')
#       exit
#
# monitor = pyudev.Monitor.from_netlink(context)
# monitor.filter_by('block')
#
# # enumerate at device connection
# for device in iter(monitor.poll, None):
#   if 'ID_FS_TYPE' in device:
#     if device.action == 'add':
#       if device.device_node[5:7] == 'sd':
#         # set dd parameters; input file, output file, block size, status
#         dd_if = '/dev/urandom'
#         dd_of = device.device_node
#         dd_bs = '1M'
#         dd_status = 'progress'
#
#         print(device.sys_name)
#         call(['dd', 'if=' + dd_if, 'of=' + dd_of, 'bs=' + dd_bs, 'status=' + dd_status])
#         print('completed')
#         exit

#[TODO] led status light control
#[TODO] connect multiple devices
#[TODO] error: 'dd: failed to open '/dev/sda': Read-only file system'
